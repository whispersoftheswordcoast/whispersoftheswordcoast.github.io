---
layout: default
title: Mago
permalink: /classi/mago/
excerpt: Studio arcano con libro e scuole di magia
---

# Mago

> Torna a [Indice classi](/classi/)

<div class="wotsc-scheda-top">
<p class="wotsc-difficolta"><strong>Difficoltà</strong>:
<span class="wotsc-diff-item">Iniziale <span class="wotsc-stelle">★★★★★</span></span>
<span class="wotsc-diff-item">Meccaniche <span class="wotsc-stelle">★★★★★</span></span>
<span class="wotsc-diff-item">Ruolo <span class="wotsc-stelle">★★★★☆</span></span></p>

<img class="wotsc-scheda-img" src="{{ '/assets/images/mago.webp' | relative_url }}" alt="mago" />
<div class="wotsc-scheda-clear"></div>
</div>

Nessuno gli ha regalato niente. Ogni incantesimo che conosce se l'è guadagnato tra libri, pratica e notti insonni, perché per il mago la magia è scienza e linguaggio, non dono. Fragile all'inizio, devastante quando ingrana.

**Ruolo:** la mente, prepara e risolve. [**Allineamento**](/sistemi/allineamenti/): qualsiasi. **Dado Vita:** d6.
**Abilità di classe:** Artigianato, tutte le Conoscenze, Parlare linguaggi, Professione, Sapienza Magica, Valutare, Volare.
**Competenze:** balestre, bastone ferrato, pugnali, randello. Armature: nessuna.

<div style="clear: both;"></div>

## Privilegi di classe

### Libro degli incantesimi e preparazione
Tutto il potere del mago passa dal grimorio, che deve trovarsi nello zaino: gli incantesimi si scelgono con `.preparaspells` e vengono memorizzati automaticamente al termine del riposo. Gli slot residui si controllano con `.memo`, le scelte con `.spells`. Senza grimorio, può lanciare solo gli incantesimi già memorizzati o conservati nelle pergamene.

### Specializzazione e scuole proibite
Al 1° livello il mago sceglie se specializzarsi in una scuola o restare universalista:

* **Specialista**: una scuola tra Abiurazione, Ammaliamento, Divinazione, Evocazione, Illusione, Invocazione, Necromanzia e Trasmutazione, selezionando altre due scuole come scuole opposte, a rappresentare le conoscenze sacrificate per la padronanza in un altro campo. Chi prepara un incantesimo di una scuola opposta deve usare due slot di quel cerchio; in compenso riceve uno slot addizionale di ogni cerchio che lancia, da usare ogni giorno per un incantesimo della propria scuola scritto nel libro.
* **Universalista**: nessuna scuola e nessuna proibizione, ma nessuno slot addizionale.

Al `.pgstart` riceve gratis 3 + INT incantesimi di 1° nel Libro. La scelta va completata con `.poterescuola`: senza, il riposo non ricostruisce le preparazioni.

### Poteri di scuola
Ogni scuola concede poteri attivabili con `.poterescuola`, dal menu che mostra gli usi rimasti sul totale: un potere di 1° livello, utilizzabile un numero di volte al giorno pari a 3 + il proprio modificatore di Intelligenza, e uno di 8°, per un numero di round al giorno pari al proprio livello da mago. Gli usi tornano con il riposo. Dettagli, meccaniche e benefici passivi nella guida [Scuole di magia](/sistemi/scuole/).

### Scrivere Pergamene (1°)
Al 1° livello il mago ottiene in automatico il talento Scrivere Pergamene.

### Talenti bonus (5°, 10°)
Ogni cinque livelli il mago riceve un talento bonus, da scegliere tra metamagia e padronanza degli incantesimi.

### Famiglio
Un famiglio è un animale domestico magico, legato magicamente al suo padrone: ne potenzia le abilità e i sensi e può aiutarlo nella magia. Il mago se lo lega con il rituale di `.sceglifamiglio`, che dura 8 ore di mondo, scegliendo tra coniglio, corvo, donnola, falco, gatto, gufo, lucertola, pipistrello, ragno, rospo, scimmia, scoiattolo, topo e serpente; legarne uno nuovo dopo il primo costa 200 monete d'oro per livello. Lo richiama poi al proprio fianco con `.evocafamiglio` (oppure `.compagni richiama famiglio`), restando fermi qualche secondo, e quando vuole metterlo al sicuro usa `.portafamiglio`, per recuperarlo con `.recuperafamiglio`. Per tutto il resto c'è il pannello `.compagni`. Il livello effettivo del famiglio è la somma dei livelli da Mago, Stregone e Warlock, fino a 12: è da questo livello che dipendono le sue capacità.

Se il famiglio muore, va rianimato con la magia oppure si attende il tempo previsto — 168 ore di mondo — prima di poterne legare uno nuovo.

Quando il famiglio è a portata di braccio, entro una casella, il padrone ne avverte ogni fruscio: chi non possiede già il talento Allerta riceve +2 a Percezione e Intuizione (+4 con 10 gradi). E finché resta nella stessa zona, ogni specie conferisce il suo bonus:

| Specie | Bonus |
|---|---|
| Gatto | +3 Furtività |
| Corvo | +3 Valutare |
| Pipistrello | +3 Volare |
| Lucertola, ragno | +3 Scalare |
| Scimmia | +3 Acrobazia |
| Scoiattolo | +3 Rapidità di Mano |
| Serpente | +3 Raggirare |
| Topo | +2 Tempra |
| Donnola | +2 Riflessi |
| Falco, gufo | +3 Percezione basata sulla vista (rispettivamente alla luce, in penombra e al buio) |

Dal 3° livello effettivo il famiglio può trasmettere incantesimi a contatto per il padrone: se i due sono vicini quando il mago lancia un incantesimo a contatto, egli può designare il famiglio come "colui che crea il contatto", e sarà il famiglio a recapitarlo proprio come avrebbe fatto il padrone. Con `.compagni tocca` si indica prima il destinatario, con `.compagni tocca un nemico` si colpisce direttamente il suo avversario. Vale solo per gli incantesimi adattati, con gestione delle cariche; e come di norma, se il padrone lancia un altro incantesimo prima che il contatto venga effettuato, la carica si dissolve.

A discrezione del padrone, il prossimo incantesimo con bersaglio "sé" può raggiungere il famiglio come un incantesimo a contatto: basta prepararlo con `.compagni condividi`, designando il compagno entro una casella. Con il talento Condividere incantesimi migliorato, `.compagni condividi migliorato` estende l'effetto a entrambi con durata dimezzata, finché il famiglio resta entro una casella (tredici effetti coperti per ora). `.compagni annulla magia` annulla carica e condivisioni in attesa.

Resta infine il legame: con `.compagni legame` il padrone percepisce solo emozioni generiche — tranquillità, allarme, dolore o fame. Dal 7° livello effettivo, `.compagni interroga` si spinge oltre: il famiglio gli riferisce lo stato di un animale dello stesso genere, entro due caselle.

## Competenze

**Armi:** balestra pesante e leggera, bastone ferrato, pugnale, pugnale da lancio, randello · **Armature:** mai.

## Incantesimi al giorno

Ogni giorno, dopo il riposo, il mago studia il grimorio: sceglie gli incantesimi con `.preparaspells`, che vengono memorizzati al termine del riposo. Gli slot base sono quelli in tabella, e lo specialista aggiunge uno slot vincolato per ogni cerchio, riservato alle magie della propria scuola. Un'Intelligenza alta concede slot bonus che crescono col punteggio: con 12 un 1° in più, con 14 anche un 2°, con 16 anche un 3°, con 18 anche un 4°, con 20 due di 1° e uno in più dal 2° al 5°.

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
| 1° | +0 | +0 / +0 / +2 | Scrivere Pergamene, specializzazione, libro, potere di scuola |
| 2° | +1 | +0 / +0 / +3 | — |
| 3° | +1 | +1 / +1 / +3 | — |
| 4° | +2 | +1 / +1 / +4 | — |
| 5° | +2 | +1 / +1 / +4 | Talento bonus |
| 6° | +3 | +2 / +2 / +5 | — |
| 7° | +3 | +2 / +2 / +5 | — |
| 8° | +4 | +2 / +2 / +6 | Potere di scuola di 8° |
| 9° | +4 | +3 / +3 / +6 | — |
| 10° | +5 | +3 / +3 / +7 | Talento bonus |
| 11° | +5 | +3 / +3 / +7 | — |
| 12° | +6/+1 | +4 / +4 / +8 | — |

## Comandi di classe

* **Libro e magia:** `.castamago` per lanciare (`.casta` generico), `.preparaspells` per scegliere (memorizza al riposo), `.memo` per gli slot residui, `.spells` per la lista, `.metamagia` per armare le metamagie possedute (anche `intensificati N`), `.controincantesimo`
* **Scuola:** `.poterescuola` con menu o nome del potere
* **Duelli e trucchi:** `.duellomagico` contro altri incantatori, `.ven`, `.visibile`, `.fermaritirata`
* **Famiglio:** `.sceglifamiglio`, `.evocafamiglio`, `.portafamiglio`, `.recuperafamiglio`, `.compagni` per gestirlo (condividi, tocca, legame, interroga, inventario)

## Vai oltre

[Creazione](/manuale/#creazione) · Nota: scuola e 3 + INT incantesimi gratuiti si scelgono al `.pgstart`. · [Magia](/sistemi/magia.html) · [Scuole di magia](/sistemi/scuole/)
