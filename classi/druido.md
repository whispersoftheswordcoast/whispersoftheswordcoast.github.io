---
layout: default
title: Druido
permalink: /classi/druido/
excerpt: Natura, animali ed elementi con forme mutevoli
---

# Druido

> Torna a [Indice classi](/classi/)

<div class="wotsc-scheda-top">
<p class="wotsc-difficolta"><strong>Difficoltà</strong>:
<span class="wotsc-diff-item">Iniziale <span class="wotsc-stelle">★★★☆☆</span></span>
<span class="wotsc-diff-item">Meccaniche <span class="wotsc-stelle">★★★☆☆</span></span>
<span class="wotsc-diff-item">Ruolo <span class="wotsc-stelle">★★★★☆</span></span></p>

<img class="wotsc-scheda-img" src="{{ '/assets/images/druida.webp' | relative_url }}" alt="druido" />
<div class="wotsc-scheda-clear"></div>
</div>

Nella purezza degli elementi e dell'ordine selvaggio giace un potere oltre le meraviglie della civiltà. Il druido lo custodisce: alleato delle creature animali e manipolatore della natura, protegge le terre selvagge da chi le minaccia e comprova la forza del mondo selvaggio a chi si chiude dietro le mura della città. Metamorfosi senza pari, compagnia di animali potenti e collera della natura al suo comando.

**Ruolo:** protettore della natura incontaminata e dell'equilibrio. [**Allineamento**](/sistemi/allineamenti/): neutrale su almeno un asse (LN, NN, CN, NG, NE), sempre. **Dado Vita:** d8.
**Abilità di classe:** Addestrare Animali, Artigianato, Cavalcare, Conoscenze (geografia, natura), Guarire, Nuotare, Percezione, Professione, Sapienza Magica, Scalare, Sopravvivenza, Volare.
**Competenze:** bastone ferrato, dardo, falcetto, fionda, lancia, pugnale, randello, scimitarra e tutti gli attacchi naturali delle forme assunte. Armature e scudi solo in materiali naturali, il metallo è bandito. **Linguaggi:** Silvano tra i bonus e Druidico gratuito dal 1°, mai da insegnare ai non druidi.

<div style="clear: both;"></div>

## Privilegi di classe

### Incantesimi e meditazione
Il druido lancia gli incantesimi divini della sua lista e li prepara tutti, purché abbia Saggezza pari a 10 più il livello dell'incantesimo: ogni giorno trascorre un'ora in trance meditativa sui misteri della natura per riguadagnarli. La Classe Difficoltà per resistervi è 10 più il livello più Saggezza. Si sceglie con `.preparaspells`, si memorizza al riposo, si controlla con `.memo` e `.spells`, si lancia con `.castadruido`.

### Empatia selvatica
Il druido migliora l'atteggiamento degli animali come con una prova di Diplomazia, tirando livello da druido più Carisma. È una capacità automatica: non si acquista a gradi e vale il livello di classe, con quello da ranger che si cumula. Un'empatia alta aiuta anche ad addestrare, con bonus di sinergia ad Addestrare Animali.

### Compagno animale (1°)
Dal 1° livello un compagno animale lo accompagna e cresce con lui. Lo si sceglie dal catalogo con `.compagnoanimale` (`.compagnoanimaledruido` apre lo stesso menu), senza fasce da sbloccare: conta solo il livello effettivo, pari al livello da druido. Lo si materializza con `.ricompagno` e lo si gestisce dal pannello `.compagni`. Ricovero e compagno designato sono spiegati nella [guida al compagno animale](/sistemi/compagni/).

### Passo senza tracce (3°)
Dal 3° livello il druido non lascia tracce negli ambienti naturali e non può essere seguito alle tracce. Vale per lui, su qualsiasi superficie: chi lo insegue deve trovare altri modi.

### Forma selvatica (4°)
Dal 4° livello il druido assume forma di animale e torna indietro con un'azione standard che non provoca attacchi di opportunità. Dura 1 ora di mondo per livello e gli usi tornano col riposo: 1 al 4°, 2 al 6°, 3 all'8°, 4 al 10°, 5 al 12°. Si cambia con `.formaselvaggia [nome]`, si torna indietro con `.formaselvaggia umana`, si controllano gli usi con `.formaselvaggia rimanenti`.

| Livello | Animali | Elementali | Vegetali |
|---|---|---|---|
| 4° | Piccoli e Medi | — | — |
| 6° | Grandi e Minuscoli | Piccoli | — |
| 8° | Enormi e Minuti | Medi | Piccoli e Medi |
| 10° | — | Grandi | Grandi |
| 12° | — | Enormi | Enormi |

L'equipaggiamento si fonde nella forma senza dare nuovi poteri passivi; le armi naturali seguono il profilo. In forma non parlante non si parla né si forniscono componenti verbali, ma si comunica normalmente con gli animali dello stesso genere. Le varianti planari (celestiale, immondo) costano 2 usi e richiedono talento e allineamento adatti; con Forma selvatica rapida e livello 8 si cambia come azione di movimento o veloce. Comandi utili in forma: `.formaselvaggia talenti`, `.formaselvaggia punire`, `.formaselvaggia capacita` (fiuto, afferrare, stritolare, balzare, volare, nuotare, scalare e gli altri).

### Lingua selvaggia
Con il talento Lingua Selvaggia, sei livelli da druido e una Forma Selvatica attiva, `.linguaselvaggia` permette di comunicare con un animale dello stesso genere della forma assunta, per minuti al giorno pari al livello da druido. L'animale risponde comunicando il proprio stato — benessere, dolore, pericolo o fame — senza che la comunicazione ne cambi l'atteggiamento o gli imponga ordini. Con `.linguaselvaggia stato` si consultano i minuti residui.

### Immunità ai veleni (9°)
Dal 9° livello il druido è immune a tutti i veleni, naturali e magici.

### Il caduto
Chi smette di venerare la natura perde i privilegi — forma, passo, compagno, empatia e immunità — finché non espia: la scheda lo segnala come caduto.

## Competenze

**Armi:** bastone ferrato, dardo, falcetto, fionda, lance, pugnale, randello, scimitarra · **Armature e scudi:** solo in materiali naturali (cuoio, borchie, imbottite, pelle, corallo, scaglie; elmi di cuoio e ossa; scudi di legno e pelle), metallo mai. I fedeli di Mielikki possono spingersi oltre.

## Incantesimi al giorno

Ogni giorno, dopo la meditazione, il druido prepara dall'intera lista con `.preparaspells`: gli slot base sono quelli in tabella. Un'alta Saggezza concede slot bonus che crescono col punteggio: con 12 uno di 1° in più, con 14 anche uno di 2°, con 16 anche uno di 3°, con 18 anche uno di 4°, con 20 due di 1° e uno in più dal 2° al 5°.

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

| Liv | BAB | T / R / V | Privilegi |
|---|---|---|---|
| 1° | +0 | +2 / +0 / +2 | Compagno animale, empatia, incantesimi, druidico |
| 2° | +1 | +3 / +0 / +3 | — |
| 3° | +2 | +3 / +1 / +3 | Passo senza tracce |
| 4° | +3 | +4 / +1 / +4 | Forma selvatica 1/giorno (Piccoli, Medi) |
| 5° | +3 | +4 / +1 / +4 | — |
| 6° | +4 | +5 / +2 / +5 | Forma 2/giorno (Grandi, Minuscoli, elementali Piccoli), lingua selvaggia |
| 7° | +5 | +5 / +2 / +5 | — |
| 8° | +6/+1 | +6 / +2 / +6 | Forma 3/giorno (Enormi, Minuti, elementali Medi, vegetali Piccoli e Medi) |
| 9° | +6/+1 | +6 / +3 / +6 | Immunità ai veleni |
| 10° | +7/+2 | +7 / +3 / +7 | Forma 4/giorno (elementali e vegetali Grandi) |
| 11° | +8/+3 | +7 / +3 / +7 | — |
| 12° | +9/+4 | +8 / +4 / +8 | Forma 5/giorno (elementali e vegetali Enormi) |

## Comandi di classe

* **Compagno:** `.compagnoanimale` per sceglierlo dal catalogo, `.ricompagno` per richiamarlo, `.compagni` per gestirlo (ricovero e designazione nella guida)
* **Forme:** `.formaselvaggia [nome|rimanenti|umana|movimento|veloce]` per cambiare pelle, `.linguaselvaggia` per parlare agli animali, `.traslazione` con Traslazione Arborea attiva per viaggiare tra alberi gemelli entro 50 caselle
* **Magia:** `.castadruido` per lanciare, `.preparaspells` per scegliere (memorizza al riposo), `.memo` per gli slot residui, `.spells` per la lista, `.metamagia` per armare le metamagie

## Vai oltre

[Creazione](/manuale/#creazione) · [Magia](/sistemi/magia.html) · [Compagno animale](/sistemi/compagni/)
