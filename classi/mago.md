---
layout: default
title: Mago
permalink: /classi/mago/
excerpt: Studio arcano con libro e scuole di magia
---

# Mago

> Torna a [Indice classi](/classi/)

<img src="{{ '/assets/images/mago.webp' | relative_url }}" alt="mago" style="float: right; width: 45%; max-width: 320px; height: auto; margin: 0 0 1rem 1.5rem; border-radius: 10px;" />

Nessuno gli ha regalato niente. Ogni incantesimo che conosce se l'è guadagnato tra libri, pratica e notti insonni, perché per il mago la magia è scienza e linguaggio, non dono. Fragile all'inizio, devastante quando ingrana.

**Ruolo:** la mente, prepara e risolve. **Allineamento:** qualsiasi. **Dado Vita:** d6.
**Abilità di classe:** Artigianato, tutte le Conoscenze, Parlare linguaggi, Professione, Sapienza Magica, Valutare, Volare.
**Competenze:** balestre, bastone ferrato, pugnali, randello. Armature: nessuna.

<div style="clear: both;"></div>

## Privilegi di classe

### Libro degli incantesimi
Tutto il potere del mago passa dal Libro: senza, può lanciare solo gli incantesimi già memorizzati o conservati nelle pergamene.

### Scrivere Pergamene (1°)
Al 1° livello il mago ottiene in automatico il talento Scrivere Pergamene.

### Talenti bonus (5°, 10°…)
Ogni cinque livelli il mago riceve un talento bonus, da scegliere tra metamagia e padronanza degli incantesimi.

### Specializzazione (1°)
Al 1° livello il mago può specializzarsi in una scuola tra Abiurazione, Ammaliamento, Evocazione, Illusione, Divinazione, Invocazione, Necromanzia e Trasmutazione, con maggiore affinità per i suoi incantesimi. In cambio rinuncia per sempre a due scuole proibite (una sola per il Divinatore); l'Universale non si può né proibire né specializzare. Al `.pgstart` riceve gratis 3 + INT incantesimi di 1° nel Libro.

### Famiglio
Il mago ha un animale addestrato al suo servizio, gestito con i comandi dedicati.

## Competenze

**Armi:** balestra pesante e leggera, bastone ferrato, pugnale, pugnale da lancio, randello · **Armature:** mai.

## Incantesimi al giorno

Prepari dal Libro con `.memo` dopo il riposo. Specialista: +1 slot per livello. Bonus da INT alta: +1 al 1° con 12, +1 al 1°-2° con 14, +1 al 1°-3° con 16, +1 al 1°-4° con 18, +2 al 1° e +1 al 2°-5° con 20.

| Liv | 0° | 1° | 2° | 3° | 4° | 5° | 6° |
|---|---|---|---|---|---|---|---|
| 1° | 3 | 1 | — | — | — | — | — |
| 2° | 4 | 2 | — | — | — | — | — |
| 3° | 4 | 2 | 1 | — | — | — | — |
| 4° | 4 | 3 | 2 | — | — | — | — |
| 5° | 4 | 3 | 2 | 1 | — | — | — |
| 6° | 4 | 3 | 3 | 2 | — | — | — |
| 7° | 4 | 4 | 3 | 2 | 1 | — | — |
| 8° | 4 | 4 | 3 | 3 | 2 | — | — |
| 9° | 4 | 4 | 4 | 3 | 2 | 1 | — |
| 10° | 4 | 4 | 4 | 3 | 3 | 2 | — |
| 11° | 4 | 4 | 4 | 4 | 3 | 2 | 1 |
| 12° | 4 | 4 | 4 | 4 | 3 | 3 | 2 |

## Progressione 1-12

| Liv | BAB | T / R / V | Privilegi |
|---|---|---|---|
| 1° | +0 | +0 / +0 / +2 | Scrivere Pergamene, specializzazione, libro |
| 2° | +1 | +0 / +0 / +3 | — |
| 3° | +1 | +1 / +1 / +3 | — |
| 4° | +2 | +1 / +1 / +4 | — |
| 5° | +2 | +1 / +1 / +4 | Talento bonus |
| 6° | +3 | +2 / +2 / +5 | — |
| 7° | +3 | +2 / +2 / +5 | — |
| 8° | +4 | +2 / +2 / +6 | — |
| 9° | +4 | +3 / +3 / +6 | — |
| 10° | +5 | +3 / +3 / +7 | Talento bonus |
| 11° | +5 | +3 / +3 / +7 | — |
| 12° | +6/+1 | +4 / +4 / +8 | — |

## Comandi di classe

* **Libro e magia:** `.castamago` per lanciare (`.casta` generico), `.memo` e `.preparaspells` per preparare, `.spells` per la lista, `.metamagia` per armare le metamagie possedute (anche `intensificati N`), `.controincantesimo`
* **Duelli e trucchi:** `.duellomagico` contro altri incantatori, `.ven`, `.visibile`, `.fermaritirata`
* **Famiglio:** `.famigliomago`, `.evocafamigliomago`, `.famigliomiglioratomago`, `.famigliononmortomago`

## Vai oltre

[Creazione](/manuale/#creazione) · Nota: scuola e 3 + INT incantesimi gratuiti si scelgono al `.pgstart`. · [Magia](/sistemi/magia.html)


