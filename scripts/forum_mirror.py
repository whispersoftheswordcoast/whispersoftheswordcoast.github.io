#!/usr/bin/env python3
"""Mirror dei racconti dal forum ForumCommunity in pagine Jekyll.

Idempotente: riscrive una pagina solo se il contenuto cambia,
scarica un'immagine solo se non esiste gia'.

Uso locale (Edge headed):  python scripts/forum_mirror.py --browser edge [--limit N] [--only TOPICID]
Uso CI (Chrome headed sotto xvfb): python scripts/forum_mirror.py --browser chrome
"""
import argparse
import hashlib
import html as htmlmod
import io
import os
import re
import sys
import time
import urllib.request
from datetime import datetime
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(SITE_DIR, 'racconti')
IMG_DIR = os.path.join(SITE_DIR, 'assets', 'images', 'racconti')

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

FEEDS = {
    'racconti': 'https://whispersofswoardcoast.forumcommunity.net/rss.php?f=9150281&nc=1',
    'voci': 'https://whispersofswoardcoast.forumcommunity.net/rss.php?f=9151202&nc=1',
}

GROUP_NAMES = {
    'racconti': 'Racconti dal Faerun',
    'voci': 'Voci&Chiacchere',
}

SLEEP_TOPIC = 4
SLEEP_PAGE = 3


def fetch(url, binary=False, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        ctype = r.headers.get('Content-Type', '')
    return (data, ctype) if binary else data.decode('windows-1252', errors='ignore')


def rss_items(feed_url):
    raw, _ = fetch(feed_url, binary=True)
    root = ET.fromstring(raw)
    items = []
    for it in root.iter('item'):
        title = (it.findtext('title') or '').strip()
        creator = ''
        for child in it:
            if child.tag.endswith('creator'):
                creator = (child.text or '').strip()
        link = (it.findtext('link') or '').strip()
        pub = (it.findtext('pubDate') or '').strip()
        m = re.search(r'\?t=(\d+)', link)
        if not m:
            continue
        try:
            dt = parsedate_to_datetime(pub)
            date = dt.strftime('%Y-%m-%d %H:%M:%S %z')
        except Exception:
            date = pub
        items.append({'topic_id': m.group(1), 'title': htmlmod.unescape(title),
                      'author': creator, 'link': link, 'date': date})
    return items


def slugify(text, maxlen=40):
    s = text.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')[:maxlen].strip('-') or 'racconto'


def get_driver(browser):
    from selenium import webdriver
    if browser == 'edge':
        from selenium.webdriver.edge.options import Options
        opts = Options()
        opts.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        return webdriver.Edge(options=opts)
    from selenium.webdriver.chrome.options import Options
    opts = Options()
    # niente --headless: gira headed (sotto xvfb in CI)
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument('--window-size=1366,768')
    return webdriver.Chrome(options=opts)


def topic_page_urls(driver, topic_url, topic_id):
    driver.get(topic_url)
    time.sleep(SLEEP_TOPIC)
    html = driver.page_source
    if 'act=Login' in driver.current_url:
        raise RuntimeError('redirect al login per ' + topic_url)
    sts = {int(x) for x in re.findall(r'\?t=' + topic_id + r'(?:&amp;|&)st=(\d+)', html)}
    pages = [0] + sorted(s for s in sts if s > 0)
    return pages


def parse_posts(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    posts = []
    for li in soup.select('ol.List > li.post'):
        entry = ''
        anchor = li.find('a', id=re.compile(r'^entry\d+$'))
        if anchor:
            entry = anchor['id'].replace('entry', '')
        nick = li.select_one('div.nick a')
        author = nick.get_text(strip=True) if nick else '?'
        when = li.select_one('span.when')
        date = when.get('title', '').strip() if when and when.has_attr('title') else (
            when.get_text(strip=True) if when else '')
        dt = None
        try:
            dt = datetime.strptime(date, '%d/%m/%Y, %H:%M:%S')
        except Exception:
            dt = None
        color = li.select_one('table.color')
        if not color:
            continue
        # taglia firma e separatori
        for cut in color.select('div.bottomborder, div.signature'):
            for sib in list(cut.find_next_siblings()):
                sib.decompose()
            cut.decompose()
        tds = color.find_all('td')
        body_td = max(tds, key=lambda t: len(t.get_text(strip=True))) if tds else None
        body = ''.join(str(x) for x in body_td.contents) if body_td else ''
        posts.append({'entry': entry, 'author': author, 'date': date, 'dt': dt, 'body': body})
    return posts


def download_image(url, topic_id):
    if url.startswith('data:'):
        return None
    name = hashlib.sha1(url.encode('utf-8')).hexdigest()[:12]
    path = re.sub(r'[?#].*$', '', url)
    ext = os.path.splitext(path)[1].lower()
    if ext not in ('.jpg', '.jpeg', '.png', '.gif', '.webp'):
        ext = '.jpg'
    dest = os.path.join(IMG_DIR, topic_id, name + ext)
    if os.path.exists(dest) or os.path.exists(os.path.splitext(dest)[0] + '.webp'):
        webp = os.path.splitext(dest)[0] + '.webp'
        return webp if os.path.exists(webp) else dest
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    for _ in range(3):
        try:
            data, _ = fetch(url, binary=True, timeout=30)
            if len(data) < 100:
                return None
            with open(dest, 'wb') as f:
                f.write(data)
            return maybe_webp(dest)
        except Exception:
            time.sleep(2)
    return None


def maybe_webp(path):
    """Converte in webp leggero (max 1280px). Ritorna il path finale."""
    if path.endswith(('.gif', '.webp')):
        return path
    try:
        from PIL import Image
        im = Image.open(path)
        if im.mode in ('RGBA', 'LA', 'PA'):
            pass  # webp gestisce l'alpha
        elif im.mode != 'RGB':
            im = im.convert('RGB')
        if im.width > 1280:
            im = im.resize((1280, int(im.height * 1280 / im.width)), Image.LANCZOS)
        out = os.path.splitext(path)[0] + '.webp'
        im.save(out, 'WEBP', quality=82, method=6)
        os.remove(path)
        return out
    except Exception:
        return path


def clean_body(body_html, topic_id, stats):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(body_html, 'html.parser')

    # spoiler -> details
    for sp in soup.select('div.spoiler'):
        code = sp.select_one('div.code')
        details = soup.new_tag('details', attrs={'class': 'racconto-spoiler'})
        summary = soup.new_tag('summary')
        summary.string = 'Spoiler'
        details.append(summary)
        if code:
            for child in list(code.children):
                details.append(child.extract())
        else:
            for child in list(sp.children):
                details.append(child.extract())
        sp.replace_with(details)

    # immagini -> download locale
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if not src or src.startswith('data:'):
            continue
        if not src.startswith('http'):
            continue
        dest = download_image(src, topic_id)
        stats['img_ok' if dest else 'img_ko'] += 1
        if dest:
            rel = os.path.relpath(dest, SITE_DIR).replace(os.sep, '/')
            img['src'] = "{{ '/" + rel + "' | relative_url }}"
            img.attrs.pop('width', None)
            img.attrs.pop('height', None)

    # iframe youtube -> embed nocookie responsive
    for fr in soup.find_all('iframe'):
        src = fr.get('src', '')
        m = re.search(r'youtube\.com/embed/([A-Za-z0-9_-]{11})', src)
        if not m:
            fr.decompose()
            continue
        vid = m.group(1)
        wrap = BeautifulSoup(
            '<div class="racconto-video"><iframe src="https://www.youtube-nocookie.com/embed/'
            + vid + '" title="Video" style="position:absolute;top:0;left:0;width:100%;height:100%;'
            'border:0;" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" '
            'allowfullscreen loading="lazy"></iframe></div>', 'html.parser')
        fr.replace_with(wrap)

    out = str(soup)
    out = re.sub(r'\[/?font[^\]]*\]', '', out)  # residui BBCode
    out = re.sub(r'(<br\s*/?>\s*){3,}', '<br><br>', out)  # a-capo multipli
    return out.strip()


def render_md(topic, posts_html):
    def esc(s):
        return s.replace('"', '\\"')
    head = ('---\nlayout: racconti\ntitle: "%s"\ndate: %s\nauthor: "%s"\n'
            'topic_url: "%s"\ngroup: "%s"\nlastdate: %s\nlastauthor: "%s"\n'
            'lastentry: "%s"\nposts: %d\n---\n\n') % (
                esc(topic['title']), topic['date'], esc(topic['author']),
                topic['link'], GROUP_NAMES.get(topic['group'], topic['group']),
                topic['lastdate'], esc(topic['lastauthor']),
                topic['lastentry'], topic['nposts'])
    parts = [head]
    for p in posts_html:
        parts.append('<div class="racconto-post"%s>\n'
                     '<p class="racconto-autore"><strong>%s</strong> · <span>%s</span></p>\n'
                     '<div class="racconto-testo">\n%s\n</div>\n</div>\n' % (
                         ' id="p-%s"' % p['entry'] if p['entry'] else '',
                         htmlmod.escape(p['author']), htmlmod.escape(p['date']), p['body']))
    return ''.join(parts)


def process_topic(driver, topic, stats):
    pages = topic_page_urls(driver, topic['link'], topic['topic_id'])
    seen, posts = set(), []
    for n, st in enumerate(pages):
        if n > 0:
            driver.get(topic['link'] + ('&' if '?' in topic['link'] else '?') + 'st=%d' % st)
            time.sleep(SLEEP_PAGE)
        for p in parse_posts(driver.page_source):
            key = p['entry'] or (p['author'], p['date'], hash(p['body']))
            if key in seen:
                continue
            seen.add(key)
            p['body'] = clean_body(p['body'], topic['topic_id'], stats)
            posts.append(p)
    stats['posts'] += len(posts)
    return posts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--browser', default='edge', choices=['edge', 'chrome'])
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--only', default='')
    ap.add_argument('--fresh-only', action='store_true',
                    help='salta i topic con pagina gia generata (bulk import)')
    args = ap.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    topics = []
    for group, feed in FEEDS.items():
        try:
            items = rss_items(feed)
        except Exception as e:
            print('FEED KO', group, e)
            continue
        for it in items:
            it['group'] = group
            topics.append(it)
    print('topic RSS:', len(topics))
    if args.only:
        topics = [t for t in topics if t['topic_id'] == args.only]
    if args.limit:
        topics = topics[:args.limit]
    if args.fresh_only:
        topics = [t for t in topics
                  if not os.path.exists(os.path.join(
                      OUT_DIR, '%s-%s.md' % (t['topic_id'], slugify(t['title']))))]

    driver = get_driver(args.browser)
    stats = {'posts': 0, 'img_ok': 0, 'img_ko': 0, 'wrote': 0}
    try:
        # scalda la sessione sulla sezione
        driver.get('https://whispersofswoardcoast.forumcommunity.net/?f=9150281')
        time.sleep(SLEEP_TOPIC)
        for t in topics:
            fname = '%s-%s.md' % (t['topic_id'], slugify(t['title']))
            dest = os.path.join(OUT_DIR, fname)
            try:
                posts = process_topic(driver, t, stats)
            except Exception as e:
                print('KO', t['topic_id'], t['title'][:40], e)
                continue
            if not posts:
                print('VUOTO', t['topic_id'], t['title'][:40])
                continue
            dated = [p for p in posts if p.get('dt')]
            last = max(dated, key=lambda p: p['dt']) if dated else posts[-1]
            tz = t['date'].split()[-1] if re.match(r'^[+-]\d{4}$', t['date'].split()[-1]) else '+0200'
            t['lastdate'] = last['dt'].strftime('%Y-%m-%d %H:%M:%S ') + tz if last.get('dt') else t['date']
            t['lastauthor'] = last['author']
            t['lastentry'] = last['entry']
            t['nposts'] = len(posts)
            content = render_md(t, posts)
            old = open(dest, encoding='utf-8').read() if os.path.exists(dest) else None
            if old != content:
                open(dest, 'w', encoding='utf-8').write(content)
                stats['wrote'] += 1
                print('WRITE', fname, len(posts), 'post')
            else:
                print('SAME', fname)
    finally:
        driver.quit()
    print('posts:%(posts)d img_ok:%(img_ok)d img_ko:%(img_ko)d wrote:%(wrote)d' % stats)


if __name__ == '__main__':
    main()
