---
layout: default
title: Bardo
permalink: /classi/bardo/
excerpt: Musica, parole e magia per sostenere gli alleati
---

# Bardo

> Torna a [Indice classi](/classi/)

<div class="wotsc-scheda-top">
<p class="wotsc-difficolta"><strong>Difficoltà</strong>:
<span class="wotsc-diff-item">Iniziale <span class="wotsc-stelle">★★★★☆</span></span>
<span class="wotsc-diff-item">Meccaniche <span class="wotsc-stelle">★★★★☆</span></span>
<span class="wotsc-diff-item">Ruolo <span class="wotsc-stelle">★★★☆☆</span></span></p>

<img class="wotsc-scheda-img" src="{{ '/assets/images/bardo.webp' | relative_url }}" alt="bardo" />
<div class="wotsc-scheda-clear"></div>
</div>

Sconosciuti e meravigliosi segreti esistono per chi è abbastanza abile da scoprirli. Il bardo li cerca con ingegno, esperienza e magia: persuasione, manipolazione e ispirazione sono le sue armi, e le usa per tenere sé e gli alleati un passo avanti al pericolo. Studioso o intrattenitore, capo o furfante, spesso tutto insieme.

**Ruolo:** confonde i nemici e ispira gli alleati, fuori dalla mischia. [**Allineamento**](/sistemi/allineamenti/): qualsiasi. **Dado Vita:** d8.
**Abilità di classe:** Acrobazia, Artigianato, Artista della Fuga, Camuffare, tutte le Conoscenze, Diplomazia, Furtività, Intimidire, Intrattenere, Intuizione, Parlare linguaggi, Percezione, Professione, Raggirare, Rapidità di Mano, Sapienza Magica, Scalare, Utilizzare Congegni Magici, Valutare.
**Competenze:** armi semplici più arco corto e composito, frusta, manganello, spada corta e lunga, stocco; armature leggere e scudi.

<div style="clear: both;"></div>

## Privilegi di classe

### Incantesimi e Carisma
Il bardo lancia incantesimi arcani senza prepararli, pescando dai conosciuti finché ha slot: per impararli e lanciarli serve Carisma pari a 10 più il livello, e la CD per resistervi è 10 più livello più Carisma. Ai livelli 5, 8 e 11 può scambiare un conosciuto con un altro: solo trucchetti al 5°, fino al 1° all'8°, fino al 2° all'11°.

### Esibizione bardica
Il bardo è addestrato a usare Intrattenere per creare effetti magici su chi gli sta vicino, compreso sé stesso se lo desidera. Dispone di una riserva di punti pari a 4 + Carisma + 2 per livello dopo il 1°, che torna col riposo. Attivare un'esibizione è un'azione standard (di movimento dal 7°), mantenerla è gratuito ogni round; non se ne tiene più di una attiva alla volta, e termina subito se il bardo muore o resta paralizzato, stordito o privo di sensi. In combattimento, Coraggio, Grandezza e Terrore costano 1 punto ogni due round (quattro con Canzone persistente). Si avvia con `.canzonebardo` e si chiude con `.canzonebardo fine`. Ogni esibizione ha componenti sonore, visive o entrambe: i bersagli devono poter sentire o vedere il bardo perché abbia effetto.

### Repertorio
Le esibizioni si sbloccano salendo di livello. Quasi tutte raggiungono 9 caselle e chiedono che i bersagli possano sentire o vedere il bardo.

* **Ispirare Coraggio (1°)**: gli alleati che ascoltano ricevono Bonus Morale +1 ai TS contro charme e paura e Bonus di Competenza +1 a colpire e ai danni; +2 al 5°, +3 all'11°. Capacità di influenza mentale, sonora o visiva a scelta all'avvio.
* **Controcanto (1°) e Distrazione (1°)**: gratis, senza costo in punti. Il primo contrasta le magie basate sul suono, la seconda le illusioni di trama e finzione: ogni round gli alleati possono usare il risultato di Intrattenere del bardo al posto del proprio Tiro Salvezza.
* **Affascinare (1°)**: solo PNG fuori combattimento, fino a 1 + un terzo del livello bersagli, per un numero di round pari al doppio del livello. Chi fallisce il TS su Volontà (CD 10 + metà livello + CAR) resta a guardare senza agire, con penalità –4 alle prove di abilità come reazioni; una minaccia potenziale concede un nuovo TS, una evidente spezza l'effetto. Chi resiste non ritentabile per 24 ore.
* **Ispirare Competenza (3°)**: un alleato riceve Bonus di Competenza +2 alle prove di una singola abilità (+3 al 7°, +4 all'11°), per 3 cariche (6 con Canzone persistente). Il bardo non può ispirarla a sé stesso.
* **Maestro del Sapere (5°)**: prendere 10 alle Conoscenze in cui si hanno gradi, oppure prendere 20 una volta al giorno (due all'11°).
* **Suggestione (6°)**: su un PNG affascinato, una sola volta per fascinazione: "resta qui e attendi" per 2 minuti, e il controllo cade se viene aggredito. Costa 1 punto più l'azione standard; Volontà nega (CD 10 + metà livello + CAR).
* **Ispirare Terrore (8°)**: i nemici in lotta entro 9 caselle restano scossi finché restano a portata. Effetto di paura che influenza la mente.
* **Ispirare Grandezza (9°)**: fino a 1 + un terzo dei livelli oltre il 9° alleati ricevono 2 Dadi Vita bonus (d10) con i relativi punti ferita temporanei, +2 a colpire e +1 ai TS su Tempra.
* **Musica Lenitiva (12°)**: costa 2 punti e 4 round ininterrotti; gli alleati che vedono e ascoltano recuperano come una Cura Ferite Gravi di massa (3d8 + livello, max 35) e si liberano da affaticamento, malessere e scosse.
* **Canto di Libertà (12°)**: costa 4 punti e 5 round; dissolve le magie sul bersaglio e rimuove charme, blocchi, dominazioni, comandi e maledizioni.

### Esecuzione Versatile (2°)
Al 2° livello, poi al 6° e al 10°, il bardo sceglie un tipo di Intrattenere e ne usa il bonus totale, compreso quello come abilità di classe, al posto del bonus delle abilità associate. Si completa con `.canzonebardo` (voce apposita).

| Tipo | Al posto di |
|---|---|
| Canto | Intuizione, Raggirare |
| Commedia | Intimidire, Raggirare |
| Danza | Acrobazia, Volare |
| Oratoria | Diplomazia, Intuizione |
| Recitazione | Camuffare, Raggirare |
| Corde | Diplomazia, Raggirare |
| Fiati | Addestrare Animali, Diplomazia |
| Percussioni | Addestrare Animali, Intimidire |
| Tastiera | Diplomazia, Intimidire |

### Strumento e oratoria
Con `.suona` si sceglie lo strumento e lo si suona nota per nota (do, re, mi e diesis): chi non è bardo tira Intrattenere CD 20 o stecca a caso. Con `.oratore` si passa alla performance oratoria.

## Competenze

**Armi:** semplici più arco corto e composito, frusta, manganello, spada corta e lunga, stocco · **Armature:** leggere · **Scudi:** sì, tranne torre.

## Incantesimi al giorno

Ogni giorno il bardo conosce pochi incantesimi ma li lancia al momento, senza prepararli; i numeri dei conosciuti non dipendono dal Carisma. B = slot solo con CAR alto. Bonus da CAR alto: +1 al 1° con 12, +1 al 1°-2° con 14, +1 al 1°-3° con 16, +1 al 1°-4° con 18.

**Slot al giorno**

| Liv | 0° | 1° | 2° | 3° | 4° |
|---|---|---|---|---|---|
| 1° | 2 | — | — | — | — |
| 2° | 3 | B | — | — | — |
| 3° | 3 | 1 | — | — | — |
| 4° | 3 | 2 | B | — | — |
| 5° | 3 | 3 | 1 | — | — |
| 6° | 3 | 3 | 2 | — | — |
| 7° | 3 | 3 | 2 | B | — |
| 8° | 3 | 3 | 3 | 1 | — |
| 9° | 3 | 3 | 3 | 2 | — |
| 10° | 3 | 3 | 3 | 2 | B |
| 11° | 3 | 3 | 3 | 3 | 1 |
| 12° | 3 | 3 | 3 | 3 | 2 |

**Incantesimi conosciuti**

| Liv | 0° | 1° | 2° | 3° | 4° |
|---|---|---|---|---|---|
| 1° | 4 | — | — | — | — |
| 2° | 5 | 2 | — | — | — |
| 3° | 6 | 3 | — | — | — |
| 4° | 6 | 3 | 2 | — | — |
| 5° | 6 | 4 | 3 | — | — |
| 6° | 6 | 4 | 3 | — | — |
| 7° | 6 | 4 | 4 | 2 | — |
| 8° | 6 | 4 | 4 | 3 | — |
| 9° | 6 | 4 | 4 | 3 | — |
| 10° | 6 | 4 | 4 | 4 | 2 |
| 11° | 6 | 4 | 4 | 4 | 3 |
| 12° | 6 | 4 | 4 | 4 | 3 |

## Progressione 1-12

| Liv | BAB | T / R / V | Privilegi |
|---|---|---|---|
| 1° | +0 | +0 / +2 / +2 | Coraggio, controcanto, distrazione, affascinare, trucchetti |
| 2° | +1 | +0 / +3 / +3 | Esecuzione versatile |
| 3° | +2 | +1 / +3 / +3 | Competenza |
| 4° | +3 | +1 / +4 / +4 | — |
| 5° | +3 | +1 / +4 / +4 | Coraggio +2, maestro del sapere, scambio conosciuto |
| 6° | +4 | +2 / +5 / +5 | Suggestione, versatile |
| 7° | +5 | +2 / +5 / +5 | Competenza +3, avvio di movimento |
| 8° | +6/+1 | +2 / +6 / +6 | Terrore, scambio conosciuto |
| 9° | +6/+1 | +3 / +6 / +6 | Grandezza |
| 10° | +7/+2 | +3 / +7 / +7 | Versatile |
| 11° | +8/+3 | +3 / +7 / +7 | Coraggio +3, competenza +4, scambio conosciuto |
| 12° | +9/+4 | +4 / +8 / +8 | Lenitiva, libertà |

## Comandi di classe

* **Musica:** `.canzonebardo` per le esibizioni (`.canzonebardo fine` per chiudere), `.suona` con lo strumento selezionato, `.oratore` per la performance oratoria
* **Magia:** `.casta` e `.castabardo` per lanciare, `.spells` e `.spellsbardo` per le liste, `.metamagia` per armare le metamagie (i lanci spontanei rallentano di un round)

## Vai oltre

[Creazione](/manuale/#creazione) · [Magia](/sistemi/magia.html)
