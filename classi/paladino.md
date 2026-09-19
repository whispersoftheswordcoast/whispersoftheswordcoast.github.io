---
layout: default
title: Paladino
permalink: /classi/paladino/
excerpt: Guerriero sacro Legale Buono che punisce il male
---

# Paladino

> Torna a [Indice classi](/classi/)

<img src="{{ '/assets/images/paladino.webp' | relative_url }}" alt="paladino" style="float: right; width: 45%; max-width: 320px; height: auto; margin: 0 0 1rem 1.5rem; border-radius: 10px;" />

Il paladino ha giurato, e il giuramento è tutto. Onore, verità, pietà: non slogan, ma regole di vita che gli dei ripagano con potere vero. In battaglia è un guerriero completo, fuori è il faro a cui i compagni guardano quando le cose si fanno scure.

**Ruolo:** campione sacro, scudo dei deboli. **Allineamento:** Legale Buono, senza eccezioni nel codice. **Dado Vita:** d10.
**Abilità di classe:** Addestrare Animali, Artigianato, Cavalcare, Conoscenze (nobiltà, religione), Diplomazia, Guarire, Intuizione, Professione, Sapienza Magica.
**Competenze:** armi semplici e da guerra; armature leggere, medie, pesanti e scudi.

<div style="clear: both;"></div>

## Privilegi di classe

### Individuazione del male
A volontà, come l'incantesimo.

### Grazia divina (2°)
Mod CAR, se positivo, a tutti i TS.

### Punire il male
**Usi al giorno:** 1 + (livello−1)/3 (+2 per talento Punire Extra) · **Effetto:** CAR al colpire e alla CA contro di lui, livello ai danni (doppio contro non morti, draghi ed esterni malvagi) · **Attenzione:** contro non malvagi l'uso è sprecato ma consumato.

### Imposizione delle mani (2°)
**Usi al giorno:** livello/2 + CAR · cura o danni ai non morti a contatto.

### Aura di coraggio (3°)
Immune alla paura · **Alleati entro 6 m:** +4 ai TS contro paura finché sei cosciente e non CADUTO.

### Aura di fermezza (8°)
Immune agli charme · **Alleati vicini:** +4 ai TS contro charme finché sei cosciente e non CADUTO.

### Crociata (11°)
**Costo:** 2 usi di Punire · **Effetto:** condivide il tuo punire con gli alleati non malvagi entro 3 m, coi tuoi bonus · **Durata:** 1 minuto · serve un nemico già punito da te.

### Legame divino (5°)
**Usi:** 1 + (livello−5)/4 · **Scelta esclusiva:** cavalcatura speciale (si chiama con `.cavalcatura`, si congeda e richiama con `.legamedivino`) oppure arma legata (`.legamearma`, bonus +1 +(livello−5)/3).

### Scacciare non morti
Come un chierico di due livelli inferiori.

### Incantesimi (4°)
Divini, livello incantatore pari a metà livello.

### Incanalare energia
**Costo:** 2 usi di imposizione · cura o ferisce ad area secondo la polarità scelta con `.converti`.

### Indulgenze
**Quante:** livello/3 · **3°:** affaticato, infermo, scosso · **6°:** ammalato, barcollante, frastornato · **9°:** avvelenato, esausto, maledetto, nauseato, spaventato (gli ultimi tre vogliono i minori) · **12°:** accecato, assordato, paralizzato, stordito. Si applicano con l'imposizione.

### Rimuovi malattia
Cariche settimanali · `.rimuovimalattia rimasti` per contarle.

### Codice di condotta
Da CADUTO perdi tutto: niente aura, punire, imposizione né incantesimi.

## Competenze

**Armi:** tutte le semplici e da guerra · **Armature:** leggere, medie e pesanti · **Scudi:** sì.

## Incantesimi al giorno

Divini dal 4°, livello incantatore pari a metà livello. B = slot solo con CAR alto.

| Liv | 1° | 2° | 3° |
|---|---|---|---|
| 1°-3° | — | — | — |
| 4° | B | — | — |
| 5°-6° | 1 | — | — |
| 7° | 1 | B | — |
| 8° | 1 | 1 | — |
| 9° | 2 | 1 | — |
| 10° | 2 | 1 | B |
| 11° | 2 | 1 | 1 |
| 12° | 2 | 2 | 1 |

## Progressione 1-12

| Liv | BAB | T / R / V | Privilegi datati |
|---|---|---|---|
| 1° | +1 | +2 / +0 / +2 | Individuazione, punire |
| 2° | +2 | +3 / +0 / +3 | Grazia divina, imposizione |
| 3° | +3 | +3 / +1 / +3 | Aura di coraggio, indulgenze |
| 4° | +4 | +4 / +1 / +4 | Incantesimi divini |
| 5° | +5 | +4 / +1 / +4 | Legame divino |
| 6° | +6/+1 | +5 / +2 / +5 | — |
| 7° | +7/+2 | +5 / +2 / +5 | — |
| 8° | +8/+3 | +6 / +2 / +6 | Aura di fermezza |
| 9° | +9/+4 | +6 / +3 / +6 | — |
| 10° | +10/+5 | +7 / +3 / +7 | — |
| 11° | +11/+6/+1 | +7 / +3 / +7 | Crociata |
| 12° | +12/+7/+2 | +8 / +4 / +8 | — |

## Comandi di classe

`.distruggimale` per punire, `.imposizione` per curare, `.indivmale` per fiutare, `.cavalcatura` per chiamarla, `.legamedivino` e `.legamearma` per il legame, `.incanala` per l'energia divina, `.crociata` dall'11°, `.indulgenze` per sceglierle, `.rimuovimalattia` (e `rimasti` per le cariche), `.castapaladino` per lanciare dal 4°, `.metamagia` per armare le metamagie.

## Vai oltre

[Creazione](/manuale/#creazione) · Razze adatte: [Mezzelfo](/razze/mezzelfo/), [Nano](/razze/nano/), [Umano](/razze/umano/)

