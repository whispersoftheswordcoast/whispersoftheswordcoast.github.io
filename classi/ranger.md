---
layout: default
title: Ranger
permalink: /classi/ranger/
excerpt: Caccia, tracce e nemico prescelto nelle terre selvagge
---

# Ranger

> Torna a [Indice classi](/classi/)

<img src="{{ '/assets/images/ranger.webp' | relative_url }}" alt="ranger" style="float: right; width: 45%; max-width: 320px; height: auto; margin: 0 0 1rem 1.5rem; border-radius: 10px;" />

Il ranger sa leggere il terreno come gli altri leggono i libri. Boschi, colline, rovine dimenticate: ovunque ci sia natura, lui ci passa senza farsi notare e ne esce con la preda. Cacciatore, ricognitore, guardiano dei confini.

**Ruolo:** occhi e gambe del gruppo. **Allineamento:** qualsiasi. **Dado Vita:** d10.
**Abilità di classe:** Addestrare Animali, Artigianato, Cavalcare, Conoscenze (Dungeon, Geografia, Natura), Furtività, Guarire, Intimidire, Nuotare, Percezione, Professione, Sapienza Magica, Scalare, Sopravvivenza.
**Competenze:** armi semplici e da guerra; armature leggere e medie.

<div style="clear: both;"></div>

## Privilegi di classe

### Seguire Tracce
Talento gratuito dal 1°: tracce anche in condizioni difficili.

### Nemico Prescelto (1°)
**Effetto:** +2 a colpire, ai danni e alle prove contro la categoria scelta (Ascoltare, Osservare, seguire tracce…) · **Crescita:** +2 ogni 5 livelli, su un nemico nuovo o uno esistente · **Nota:** scelta obbligatoria al `.pgstart`, senza non si prosegue · **Extra:** il compagno animale usa la tua stessa lista.

### Stile di combattimento (2°)
**Quando:** 2°, 6° e 10° · **Come:** scegli uno stile, per sempre · **Effetto:** a ogni tappa un talento dello stile gratis, senza prerequisiti.

* **Due Armi** — 2°: Attacco con lo scudo migliorato, Combattere con Due Armi, Doppio taglio, Estrazione Rapida · 6°: + Due Armi migliorato, Difendere con Due Armi · 10°: + Attacco lacerante, Due Armi superiore.
* **Arco** — 2°: Tiro Concentrato, Tiro Rapido, Tiro Preciso, Tiro Ravvicinato · 6°: + Padronanza delle balestre, Tiro Preciso migliorato, Tiro Multiplo, Maestro ravvicinato · 10°: + Tiro in Movimento.
* **Due Mani** — 2°: Assalto respingente, Attacco Poderoso, Incalzare, Scudo di fendenti · 6°: + Furia Focalizzata, Incalzare potenziato · 10°: + Spaccare arma potenziato.
* **Arma e Scudo** — 2°: Attacco con lo scudo migliorato, Botta di scudo, Combattere con Due Armi, Scudo focalizzato · 6°: + Maestria negli scudi · 10°: + Chiusura con scudo, Scudo focalizzato superiore.
* **Arma Naturale** — 2°: Arma focalizzata automatica · 6°: + Artigli arcani, Colpo Vitale · 10°: + Colpo vitale migliorato, Multiattacco.
* **Lancio** — 2°: Combattere con Due Armi, Estrazione Rapida, Tiro a distanza, Tiro Preciso · 6°: + Tiro Ravvicinato · 10°: + Tiro in Movimento.
* **Balestra** — 2°: Mira Letale, Ricarica Rapida, Tiro Concentrato, Tiro Preciso · 6°: + Padronanza delle balestre, Tiro Preciso migliorato · 10°: + Tiro in Movimento.
* **Sella** — 2°: Attacco, Combattere e Tirare in Sella, Cavallerizzo · 6°: + Carica Devastante · 10°: + Cavallerizzo da Guerra.

### Compagno animale (4°)
**Livello effettivo:** ranger − 3 · **Come:** `.compagnoanimaleranger` su aquila, cane, lupo, cavallo e simili, che ti deve accettare.

### Preda (11°)
Designi una preda viva a vista con `.preda`, solo del tipo di un tuo Nemico Prescelto · **In mischia:** +2 per colpire la preda designata · **Se muore:** nuova tra 1 ora · **Se l'abbandoni:** 24 ore di attesa · `.preda stato` per controllare.

### Incantesimi (4°)
Divini dal legame con la natura.

## Competenze

**Armi:** tutte le semplici e da guerra · **Armature:** leggere e medie · **Scudi:** sì.

## Incantesimi al giorno

Divini dal 4° livello. B = slot solo con SAG alta.

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

| Liv | BAB | T / R / V | Privilegi |
|---|---|---|---|
| 1° | +1 | +2 / +2 / +0 | Seguire Tracce, Nemico Prescelto |
| 2° | +2 | +3 / +3 / +0 | Stile di combattimento |
| 3° | +3 | +3 / +3 / +1 | — |
| 4° | +4 | +4 / +4 / +1 | Incantesimi, compagno animale |
| 5° | +5 | +4 / +4 / +1 | Nemico: nuovo o bonus maggiore |
| 6° | +6/+1 | +5 / +5 / +2 | Stile (2° talento) |
| 7° | +7/+2 | +5 / +5 / +2 | — |
| 8° | +8/+3 | +6 / +6 / +2 | — |
| 9° | +9/+4 | +6 / +6 / +3 | — |
| 10° | +10/+5 | +7 / +7 / +3 | Nemico, stile (3° talento) |
| 11° | +11/+6/+1 | +7 / +7 / +3 | Preda |
| 12° | +12/+7/+2 | +8 / +8 / +4 | — |

## Comandi di classe

`.compagnoanimaleranger` dal 4° per il compagno, `.ricompagno` per richiamarlo, `.preda` dall'11° per designarlo (`.preda stato`, `.preda abbandona`), `.castaranger` per lanciare dal 4°.

## Vai oltre

[Creazione](/manuale/#creazione) · Nota: il Nemico Prescelto va scelto al `.pgstart`, senza non si prosegue. Razze adatte: [Elfo](/razze/elfo/), [Mezzelfo](/razze/mezzelfo/), [Halfling](/razze/halfling/)

