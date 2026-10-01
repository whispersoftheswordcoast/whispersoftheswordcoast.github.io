---
layout: default
title: Chierico
permalink: /classi/chierico/
excerpt: Magia divina, cure e domini del suo dio
---

# Chierico

> Torna a [Indice classi](/classi/)

<div class="wotsc-scheda-top">
<p class="wotsc-difficolta"><strong>Difficoltà</strong>:
<span class="wotsc-diff-item">Iniziale <span class="wotsc-stelle">★★☆☆☆</span></span>
<span class="wotsc-diff-item">Meccaniche <span class="wotsc-stelle">★★★☆☆</span></span>
<span class="wotsc-diff-item">Ruolo <span class="wotsc-stelle">★★★★☆</span></span></p>

<img class="wotsc-scheda-img" src="{{ '/assets/images/chierico.webp' | relative_url }}" alt="chierico" />
<div class="wotsc-scheda-clear"></div>
</div>

Quando il gruppo è in ginocchio, è al chierico che tutti guardano. Ponte tra gli dei e il campo di battaglia, incanala poteri che nessuna magia arcana può replicare. E ogni chierico ha il volto del suo dio: luce e rinascita con Lathander, dominio e forza con Bane.

**Ruolo:** pilastro del gruppo, cura e decide. [**Allineamento**](/sistemi/allineamenti/): entro una casella da quello del dio, mai in diagonale. **Dado Vita:** d8.
**Abilità di classe:** Artigianato, Conoscenze (arcane, nobiltà, piani, religioni, storia), Diplomazia, Guarire, Intuizione, Parlare linguaggi, Professione, Sapienza Magica, Valutare.
**Competenze:** solo armi semplici; armature leggere e medie; scudi.

<div style="clear: both;"></div>

## Privilegi di classe

### Incantesimi divini
Il chierico riceve ogni potere dalla fede nel suo dio: al mattino prega impugnando il simbolo sacro e prepara gli incantesimi con `.preparaspells`. La Saggezza misura la forza di quella fede e decide quanti slot hai e quanto è difficile resistervi; a ogni livello di incantesimo ricevi anche uno slot di dominio, concesso dal dio. Le scuole opposte alla fede restano vietate: bene contro male, legge contro caos. Una volta preparati, controlli gli slot con `.memo`, sfogli la lista con `.spells` e lanci con `.castachierico`.

### Conversione spontanea
Con `.converti` muti un incantesimo preparato in cura o ferita dello stesso livello. La polarità cura/infliggi è permanente e condivisa con `.incanala`: i buoni sono obbligati alla cura, i malvagi a infliggere, i neutrali scelgono una volta per sempre.

### Scacciare non morti
Fin dal 1° livello il chierico sa scacciare i non morti. Con `.scacciare`, a simbolo sacro impugnato e come azione standard, investi i non morti entro 6 caselle (9 metri): chi supera il TS su Volontà (CD 10 + metà livello + CAR) resiste, chi fallisce fugge con energia positiva o resta intimorito con energia negativa per 1 minuto. Se il tuo livello è almeno il doppio dei DV del bersaglio, lo distruggi con energia positiva o lo comandi con energia negativa, fino a DV comandati pari al tuo livello. Ogni tentativo costa 1 uso di Incanalare (`.scacciare rimanenti` per contarli).

### Incanalare energia
Il chierico riversa la fede intorno a sé attraverso il simbolo sacro: con `.incanala cura` risana, con `.incanala danneggia` ferisce, sempre nel raggio di 6 caselle e come azione standard. L'energia positiva cura i viventi e ferisce i non morti, quella negativa fa il contrario, e chi subisce danno può dimezzarlo superando il TS. La potenza in dadi cresce col livello (vedi tabella sotto) e ogni uso attinge alla stessa riserva di Scacciare: 3 + CAR al giorno, +2 per talento Incanalare Extra (`.incanala rimanenti` per contarli). Con `.incanala punizione` carichi invece l'energia sul prossimo attacco contro un singolo bersaglio.

### Domini
Il dio concede al chierico due domini, scelti al `.pgstart` tra quelli del culto con filtro per allineamento su Bene/Male/Legge/Caos. Ogni dominio è un insieme di poteri legati a un tema: elementi, luce, guerra, inganno e gli altri. In tutto sono 59 domini fino al 12°, con usi al giorno che tornano solo col riposo. Si attivano con `.poteredominio nome [potere]` (menu se ometti il potere); alcuni poteri hanno comandi dedicati, elencati nella guida [Domini del chierico](/sistemi/domini/).

### Talenti e arma della divinità
I domini assegnano anche talenti bonus e la competenza nell'arma del culto (dettagli nella guida).

## Competenze

**Armi:** solo semplici · **Armature:** leggere e medie · **Scudi:** sì.

## Incantesimi al giorno

Gli slot base sono in tabella, più uno slot di dominio per ogni livello di incantesimo che sai lanciare. Con Saggezza alta ricevi slot bonus: più è alta, più livelli ne beneficiano (tabella completa nella pagina [Magia](/sistemi/magia.html)).

| Liv | 0° | 1° | 2° | 3° | 4° | 5° | 6° |
|---|---|---|---|---|---|---|---|
| 1° | 3 | 1 | — | — | — | — | — |
| 2° | 4 | 2 | — | — | — | — | — |
| 3° | 4 | 2 | 1 | — | — | — | — |
| 4° | 5 | 3 | 2 | — | — | — | — |
| 5° | 5 | 3 | 2 | 1 | — | — | — |
| 6° | 5 | 3 | 3 | 2 | — | — | — |
| 7° | 6 | 4 | 3 | 2 | 1 | — | — |
| 8° | 6 | 4 | 3 | 3 | 2 | — | — |
| 9° | 6 | 4 | 4 | 3 | 2 | 1 | — |
| 10° | 6 | 4 | 4 | 3 | 3 | 2 | — |
| 11° | 6 | 5 | 4 | 4 | 3 | 2 | 1 |
| 12° | 6 | 5 | 4 | 4 | 3 | 3 | 2 |

## Progressione 1-12

Incanalare: 3 + CAR usi al giorno (+2 per talento Incanalare Extra); la potenza in dadi cresce come in tabella.

| Liv | BAB | T / R / V | Incanalare | Privilegi |
|---|---|---|---|---|
| 1° | +0 | +2 / +0 / +2 | 1d6 | Domini, incantesimi, scacciare, conversione |
| 2° | +1 | +3 / +0 / +3 | 1d6 | — |
| 3° | +2 | +3 / +1 / +3 | 2d6 | — |
| 4° | +3 | +4 / +1 / +4 | 2d6 | — |
| 5° | +3 | +4 / +1 / +4 | 3d6 | — |
| 6° | +4 | +5 / +2 / +5 | 3d6 | — |
| 7° | +5 | +5 / +2 / +5 | 4d6 | — |
| 8° | +6/+1 | +6 / +2 / +6 | 4d6 | Poteri di dominio dell'8° |
| 9° | +6/+1 | +6 / +3 / +6 | 5d6 | — |
| 10° | +7/+2 | +7 / +3 / +7 | 5d6 | — |
| 11° | +8/+3 | +7 / +3 / +7 | 6d6 | — |
| 12° | +9/+4 | +8 / +4 / +8 | 6d6 | Poteri di dominio potenziati |

## Comandi di classe

* **Divini:** `.scacciare` e `.scacciare rimanenti`, `.poteredominio nome [potere]`, `.converti`, `.incanala cura/danneggia` · `.incanala punizione` · `.incanala rimanenti`
* **Magia:** `.castachierico` (`.casta` generico), `.memo` e `.preparaspells`, `.spells`, `.metamagia`

## Vai oltre

[Creazione](/manuale/#creazione) · [Magia](/sistemi/magia.html) · [Domini del chierico](/sistemi/domini/)
