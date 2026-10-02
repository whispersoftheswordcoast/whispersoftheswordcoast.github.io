---
layout: default
title: Stregone
permalink: /classi/stregone/
excerpt: Magia innata e spontanea da Carisma
---

# Stregone

> Torna a [Indice classi](/classi/)

<div class="wotsc-scheda-top">
<p class="wotsc-difficolta"><strong>Difficoltà</strong>:
<span class="wotsc-diff-item">Iniziale <span class="wotsc-stelle">★★★★☆</span></span>
<span class="wotsc-diff-item">Meccaniche <span class="wotsc-stelle">★★★★☆</span></span>
<span class="wotsc-diff-item">Ruolo <span class="wotsc-stelle">★★☆☆☆</span></span></p>

<img class="wotsc-scheda-img" src="{{ '/assets/images/stregone.webp' | relative_url }}" alt="stregone" />
<div class="wotsc-scheda-clear"></div>
</div>

C'è chi la magia la studia sui libri e chi la porta nel sangue da prima di nascere. Lo stregone appartiene alla seconda schiera: il potere gli scorre nelle vene per retaggio o per un evento che lo ha segnato per sempre, e lo evoca d'istinto, senza formule né preparazioni. Per lui la magia non è uno studio: è un destino scritto nel sangue.

**Ruolo:** artiglieria spontanea. [**Allineamento**](/sistemi/allineamenti/): qualsiasi. **Dado Vita:** d6.
**Abilità di classe:** Artigianato, Conoscenze (arcane), Intimidire, Professione, Raggirare, Sapienza Magica, Utilizzare Oggetti Magici, Valutare, Volare.
**Competenze:** tutte le armi semplici. Armature: nessuna.

<div style="clear: both;"></div>

## Privilegi di classe

### Incantesimi spontanei
Lo stregone non prepara nulla: conosce un numero limitato di incantesimi e li lancia d'istinto, scegliendo di volta in volta quale usare, finché ha slot liberi del livello giusto. Ogni slot lanciato è andato fino al riposo, come per tutti gli incantatori.

### Carisma chiave
Il Carisma è tutto per lo stregone: decide gli slot bonus giornalieri e quanto è difficile resistere ai suoi incantesimi. Un Carisma alto significa più lanci e tiri salvezza più duri per chi sta davanti.

### Nuovi conosciuti
A ogni livello lo stregone aggiunge nuovi incantesimi alla lista dei conosciuti, secondo la tabella sotto. Sono pochi e restano quelli: ogni scelta pesa, perché non si torna indietro con facilità.

### Escludere Materiali
Alla creazione lo stregone riceve gratis il talento Escludere Materiali: lancia senza componenti materiali povere.

### Stirpe
1 stirpe tra 9, scelta al 1° livello con `.poterestirpe` e mai più cambiabile (la draconica sceglie anche il drago). Dà poteri con `.poterestirpe [potere]`, resistenze, talenti e 5 incantesimi bonus al 3°, 5°, 7°, 9° e 11°. Dettagli nella guida [Stirpi dello stregone](/sistemi/stirpi/).

### Metamagia spontanea
Le metamagie armate con `.metamagia` si applicano al momento del lancio, ma il lancio si allunga di un round, salvo Incantesimi rapidi. Vanno comunque pagate con lo slot maggiorato.

### Famiglio
Anche lo stregone ha il suo animale: `.famigliostregone`, `.evocafamigliostregone`, `.famigliomiglioratostregone`, `.famigliononmortostregone`.

## Competenze

**Armi:** tutte le semplici · **Armature:** mai.

## Incantesimi al giorno

Slot a sinistra, conosciuti a destra: li lanci senza preparare. Con Carisma alto ricevi slot bonus: più è alto, più livelli ne beneficiano (tabella completa nella pagina [Magia](/sistemi/magia.html)).

| Liv | Slot 0°-6° | Conosciuti 0°-6° |
|---|---|---|
| 1° | 5, 3 | 4, 2 |
| 2° | 6, 4 | 5, 2 |
| 3° | 6, 5 | 5, 3 |
| 4° | 6, 6, 3 | 6, 3, 1 |
| 5° | 6, 6, 4 | 6, 4, 2 |
| 6° | 6, 6, 5, 3 | 7, 4, 2, 1 |
| 7° | 6, 6, 6, 4 | 7, 5, 3, 2 |
| 8° | 6, 6, 6, 5, 3 | 8, 5, 3, 2, 1 |
| 9° | 6, 6, 6, 6, 4 | 8, 5, 4, 3, 2 |
| 10° | 6, 6, 6, 6, 5, 3 | 9, 5, 4, 3, 2, 1 |
| 11° | 6, 6, 6, 6, 6, 4 | 9, 5, 5, 4, 3, 2 |
| 12° | 6, 6, 6, 6, 6, 5, 3 | 9, 5, 5, 4, 3, 2, 1 |

## Progressione 1-12

| Liv | BAB | T / R / V | Privilegi |
|---|---|---|---|
| 1° | +0 | +0 / +0 / +2 | Stirpe, poteri base, famiglio |
| 2° | +1 | +0 / +0 / +3 | — |
| 3° | +1 | +1 / +1 / +3 | Resistenze 5, incantesimo di stirpe |
| 4° | +2 | +1 / +1 / +4 | — |
| 5° | +2 | +1 / +1 / +4 | Incantesimo di stirpe, artigli magici |
| 6° | +3 | +2 / +2 / +5 | — |
| 7° | +3 | +2 / +2 / +5 | Talento di stirpe, incantesimo di stirpe, artigli 1d6 |
| 8° | +4 | +2 / +2 / +6 | — |
| 9° | +4 | +3 / +3 / +6 | Grandi poteri, resistenze 10, incantesimo di stirpe |
| 10° | +5 | +3 / +3 / +7 | — |
| 11° | +5 | +3 / +3 / +7 | Incantesimo di stirpe |
| 12° | +6/+1 | +4 / +4 / +8 | — |

## Comandi di classe

* **Stirpe:** `.poterestirpe` e `.poterestirpe [potere]` per poteri e scelta iniziale
* **Magia:** `.castastregone` per lanciare (`.casta` generico), `.spells` per i conosciuti, `.metamagia` per armare le metamagie
* **Famiglio:** `.famigliostregone`, `.evocafamigliostregone`, `.famigliomiglioratostregone`, `.famigliononmortostregone`

## Vai oltre

[Creazione](/manuale/#creazione) · [Magia](/sistemi/magia.html) · [Stirpi dello stregone](/sistemi/stirpi/)
