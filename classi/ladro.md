---
layout: default
title: Ladro
permalink: /classi/ladro/
excerpt: Ombre, scasso e colpi decisivi con più abilità di tutti
---

# Ladro

> Torna a [Classi e Razze](/classi-e-razze/) · [Indice classi](/classi/)

<img src="{{ '/assets/images/ladro.webp' | relative_url }}" alt="ladro" style="float: right; width: 45%; max-width: 320px; height: auto; margin: 0 0 1rem 1.5rem; border-radius: 10px;" />

Dove il guerriero sfonda la porta, il ladro era già dentro da un'ora. Astuzia, precisione, adattabilità: si muove inosservato, capisce le persone al volo e sfrutta ogni spiraglio, in combattimento come fuori.

**Ruolo:** ombra del gruppo, apre e scopre l'impossibile. **Allineamento:** qualsiasi. **Dado Vita:** d8.
**Abilità di classe:** praticamente tutte, da Acrobazia a Valutare passando per Furtività, Disattivare congegni, Raggirare, Rapidità di mano e Utilizzare oggetti magici.
**Competenze:** arco corto, balestre, pugnali, spade corte e armi leggere simili; solo armature leggere.

<div style="clear: both;"></div>

## Privilegi di classe

### Attacco furtivo
Danni extra a chi è colto alla sprovvista o indifeso · **Non funziona su:** non morti, costrutti, melme (niente punti vitali).

### Trappole
Individua e disattiva ogni tipo, anche magiche · **Solo tu oltre CD 20.**

### Percepire trappole
**3°:** +1 ai Riflessi contro trappole e alla CA · **6°:** +2 · **9°:** +3 · **12°:** +4.

### Eludere (2°)
Automatico al passaggio di livello: con Riflessi superato contro aree, zero danni · **Migliorato:** via dote dal 10°.

### Schivare prodigioso (4°)
DES alla CA anche se colto alla sprovvista · **Migliorato (8°):** versione superiore automatica.

### Doti da ladro
**Quante:** 1 ogni 2 livelli da Ladro (livello ÷ 2), dal 2° al 20° · **Come:** al `.passalivello` il gioco ti apre da solo il gump di scelta · **Vedi le tue:** con `.dotiladro` · **Dal 10°:** al posto della dote puoi prendere un talento · **Extra:** col talento Dote da ladro extra (`.abilitaladro` è comando staff).
**Alcune hanno prerequisiti:** Magia Minore vuole INT 10, Magia Maggiore INT 11 più la Minore, le avanzate (42-59) vogliono il 10° livello, altre si concatenano (Furtivo mortale vuole Furtivo potenziato, Attacco dissolvente vuole Magia Maggiore, Famiglio vuole entrambe le Magie).

#### Doti base (dal 2° livello)

| Dote | Effetto |
|---|---|
| Magia Minore | Trucchetto 3/giorno, LI = livelli da Ladro, CD da INT · vuole INT 10 |
| Magia Maggiore | Incantesimo di 1° 2/giorno · vuole INT 11 e Magia Minore |
| Accuratezza | Talento Arma Accurata gratis |
| Addestramento | Arma Focalizzata a scelta gratis |
| Armi da fuoco | Competenza piena |
| Acuto Osservatore | +4 Percezione per conversazioni, segreti e trappole |
| Arrampicamuri | Doppio tiro a Scalare, prendi il migliore |
| Attacco improvviso | Nel round di sorpresa i bersagli restano impreparati |
| Attacco silenziante | Il furtivo ammutolisce 1 round (Volontà nega) · usi = metà livello |
| Camuffamento rapido | Tempi ridotti: azione completa o 1 minuto |
| Disattivare rapido | Tempo dimezzato, minimo 1 round |
| Distogliere | Cedi i danni furtivi: bersaglio impreparato contro un alleato fino al tuo prossimo turno |
| Dita rapide | Doppio tiro a Rapidità di mano · 1/giorno +1 ogni 5 livelli, via `.dotaladro dita` |
| Esperto di sopravvivenza | Guarire e Sopravvivenza diventano di classe |
| Falso amico | +4 Raggirare per fingersi conoscenti · solo Kitsune |
| Forte bracciata | Doppio tiro a Nuotare |
| Furtività rapida | Piena velocità in furtività senza penalità |
| Genio della fuga | Addestrare, Cavalcare e Volare di classe · +2 alle prove di guida |
| Maestro delle corde | Movimento normale sulle corde, prendi 10 in equilibrio |
| Manovra senza pari | Doppio tiro ad Acrobazia · 1/giorno +1 ogni 5 livelli, via `.dotaladro manovra` |
| Occhio del cecchino | Furtivo a 9 m anche con occultamento non totale |
| Parvenza impressionante | Prodezza Intimidatrice come talento bonus |
| Recupero | 1/giorno: sotto 0 PF, temporanei pari al livello per 1 minuto |
| Rialzarsi | Da prono gratis, ma provoca AdO |
| Scassinare rapido | Serratura come azione standard |
| Subdolo | +4 a occultare armi · furtivo massimizzato in sorpresa, usi = CAR |
| Tiro immediato | In sorpresa, iniziativa 20 per un attacco a distanza |
| Tramortire | Il bersaglio del furtivo prende −2 contro di te per 1d4 round |
| Trucco della forcina | Niente penalità con improvvisati, bonus doppi con perfetti |
| Ammaliatore | Doppio dado a Diplomazia (ruolo) |
| Bugie convincenti | Chi ci crede le ripete come vere (ruolo) |
| Equilibrista | Acrobazie su strettoie (ruolo) |
| Attacco Sanguinante | 1 danno + 1 round per ogni dado furtivo |
| Furtivo potenziato | Nel furtivo gli 1 valgono 2 |
| Difesa Offensiva | +1 CA per dado furtivo contro il colpito |
| Espediente | Un talento da combattimento di cui hai i prerequisiti |
| Difficile da ingannare | Doppio dado a Intuizione (ruolo) |
| Estorcere informazioni | Usa il migliore tra Intimidire, Diplomazia e Raggirare |
| Parole Melliflue | Doppio dado a Raggirare (ruolo) |
| Scaltro Poliglotta | 2 lingue, 4 con Linguistica |
| Seguire Indizi | Percezione per seguire tracce |

#### Doti avanzate (dal 10° livello)

| Dote | Effetto |
|---|---|
| Alleato involontario | `.alleatoinvolontario`: fiancheggi usando la posizione del nemico ingannato |
| Attacco dissolvente | `.settafurtivo`: dissolve l'incantesimo più basso · vuole Magia Maggiore |
| Furtivo mortale | Nel potenziato, 1 e 2 valgono 3 · vuole Furtivo potenziato |
| Attutire il colpo | 1/giorno: Riflessi con CD = danni per dimezzare il letale |
| Bersagliatore furtivo | `.bersagliatorefurtivo`: cecchino a −10 invece di −20 |
| Borseggia armi | Con `.disarma`, Rapidità al posto della manovra |
| Colpo menomante | `.settafurtivo`: anche 2 danni a FOR |
| Eludere migliorato | Zero danni col superato, metà col fallito · vuole Eludere |
| Famiglio | Livello effettivo −4 · vuole Minore e Maggiore |
| Lame confondenti | `.settafurtivo`: niente AdO al bersaglio per 1d4+1 round |
| Maestro del travestimento | 1/giorno: `.maestrotravestimento` dà +10 Camuffare |
| Mente nascosta | Anti-divinazione con LI = livello |
| Mente sfuggente | Ritenta l'ammaliamento fallito dopo 1 round |
| Opportunismo | 1/round contro chi l'alleato ha appena ferito |
| Ridirezionare | 1/giorno: devia il colpo su una creatura adiacente |
| Riesame oculato | 1/giorno: ripete l'ultima Conoscenze, Intuizione o Percezione |
| Schivata estrema | 1/giorno: passo da 1,5 m che evita il letale se esce di portata |
| Sorpresa del cacciatore | 1/giorno: tutto furtivo per 1 round contro un adiacente |

### Capacità speciali (10°)
Le doti avanzate qui sopra, oppure un talento al posto della dote.

## Competenze

**Armi semplici** più, da guerra: arco corto e composito, balestre a mano e leggera, dardo, manganello, mazze leggere, pugnali, spada corta. Da taglia Media anche balestra pesante, bastone ferrato, mazza pesante, randello e stocco · **Armature:** solo leggere · **Scudi:** no.

## Progressione 1-12

| Liv | BAB | T / R / V | Privilegi |
|---|---|---|---|
| 1° | +0 | +0 / +2 / +0 | Attacco furtivo |
| 2° | +1 | +0 / +3 / +0 | Eludere, dote da ladro |
| 3° | +2 | +1 / +3 / +1 | Percepire trappole +1 |
| 4° | +3 | +1 / +4 / +1 | Schivare prodigioso, dote |
| 5° | +3 | +1 / +4 / +1 | — |
| 6° | +4 | +2 / +5 / +2 | Percepire +2, dote |
| 7° | +5 | +2 / +5 / +2 | — |
| 8° | +6/+1 | +2 / +6 / +2 | Schivare migliorato, dote |
| 9° | +6/+1 | +3 / +6 / +3 | Percepire +3 |
| 10° | +7/+2 | +3 / +7 / +3 | Dote o talento, doti avanzate |
| 11° | +8/+3 | +3 / +7 / +3 | — |
| 12° | +9/+4 | +4 / +8 / +4 | Percepire +4, dote |

## Comandi di classe

`.dotiladro` per vedere le tue doti; le scelte arrivano da sole al `.passalivello` nei livelli pari (`.abilitaladro` è comando staff). `.dotaladro dita` e `.dotaladro manovra` attivano Dita Rapide e Manovra Senza Pari (usi 1 + livello/5 al giorno). Dalle doti: `.subdolo`, `.settafurtivo`, `.alleatoinvolontario`, `.bersagliatorefurtivo`, `.maestrotravestimento`, `.ridirezionare`, `.riesame`, `.schivataestrema`, `.sorpresacacciatore`, `.disarma`.

## Vai oltre

[Creazione](/manuale/#creazione) · [Classi e Razze](/classi-e-razze/) · Razze adatte: [Halfling](/razze/halfling/), [Elfo](/razze/elfo/), [Gnomo](/razze/gnomo/)
