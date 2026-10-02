---
title: Scuole di magia
layout: sistemi
permalink: /sistemi/scuole/
order: 27
excerpt: Come si sceglie la scuola del mago e cosa fanno i poteri di ognuna delle otto scuole più l'universale
---

# Scuole di magia

Al 1° livello il mago sceglie se specializzarsi in una delle otto scuole o restare universalista. La scelta è permanente e decide poteri, slot e scuole proibite per tutto il personaggio. Questa guida spiega come si sceglie, come si attivano i poteri e cosa fa ognuna delle **otto scuole più l'universale**.

## Scegliere la scuola

La scelta avviene con `.poterescuola` e chiede prima la scuola e poi, per lo specialista, esattamente due scuole proibite. L'universale non si può né specializzare né proibire. Una volta confermata, la scelta non si cambia.

Le magie delle scuole proibite si possono comunque imparare e scrivere nel libro, ma prepararle costa due slot ordinari dello stesso cerchio. Lo specialista riceve in cambio uno slot vincolato per ogni cerchio che lancia, utilizzabile solo per una magia della propria scuola presente nel libro.

<div class="wotsc-esempio" markdown="1">

Evocatore con Necromanzia e Ammaliamento proibite: una Palla di Fuoco necromantica da preparare occupa due slot del suo cerchio, mentre lo slot vincolato di 3° accetta solo evocazioni scritte nel grimorio.

</div>

Senza scelta completata, il riposo non ricostruisce le preparazioni: il gioco lo segnala e invita a usare `.poterescuola`.

## Usarli in gioco

Tutti i poteri passano da un unico comando:

`.poterescuola [potere]`

Senza nome del potere si apre il **menu con i poteri disponibili al tuo livello** e gli usi rimasti sul totale; conoscendo il nome lo scrivi diretto, per esempio `.poterescuola dardo`. Con `.poterescuola stop` si interrompono i poteri mantenuti e con `.poterescuola riepilogo` si rilegge la propria scuola.

I poteri di attacco chiedono un **attacco di contatto** oppure un bersaglio entro 6 caselle; i poteri segnati [GDR] sono puramente ruolistici e si risolvono nel racconto col master. In combattimento serve quasi sempre l'**azione standard** (il Campo di Invisibilità quella veloce).

## Usi al giorno e riposo

I poteri di 1° livello si utilizzano un numero di volte al giorno pari a 3 + il proprio modificatore di Intelligenza; quelli di 8° per un numero di round al giorno pari al proprio livello da mago, non necessariamente consecutivi. Tutte le riserve tornano solo con il riposo. I poteri mantenuti consumano 1 uso per round finché restano attivi e se ne può tenere uno solo alla volta: per cambiarlo serve prima `stop`.

<div class="wotsc-esempio" markdown="1">

Mago di 8° con INT +3: il Dardo Acido sei volte al giorno, il Muro Elementale otto round totali da distribuire come vuoi, poi serve il riposo.

</div>

## Le scuole una per una

Sotto trovi le otto scuole più l'universale in ordine alfabetico. Ogni voce elenca il potere di 1° livello, quello di 8° e i benefici passivi della scuola.

### Abiurazione

È la scuola della difesa e del diniego: crea barriere fisiche e magiche, nega le facoltà altrui, punisce i trasgressori e bandisce le creature ad altri piani di esistenza. L'abiuratore volge la magia contro la magia stessa e padroneggia le arti della protezione come nessun altro: dove gli altri evocano e distruggono, lui resiste e nega.

- **1°**: Interdizione Protettiva: come azione standard si crea in un raggio di 2 caselle una barriera mantenuta che dura un numero di round pari al modificatore di INT; al riposo si sceglie una resistenza all'energia tra acido, elettricità, freddo, fuoco e sonoro (5, 10 dall'11°).
- **6°**: assorbimento automatico dei danni energetici fino a esaurire la riserva (3 per livello da mago).

### Ammaliamento

È la scuola che piega le menti altrui, influenzando e controllando il comportamento: gli charme mutano il modo in cui la vittima vede l'incantatore, fino a considerarlo un amico, mentre le compulsioni ne determinano le azioni o il modo stesso di ragionare. L'ammaliatore non ha bisogno di convincere né di minacciare: domina e manipola, e la volontà altrui diventa strumento nelle sue mani.

- **1°**: Tocco Frastornante: con un attacco di contatto in mischia si rende frastornata una creatura vivente per 1 round (non sui immuni mentali).
- **8°**: Aura di Disperazione: si emana un'aura mobile di 6 caselle che penalizza di 2 gli attacchi dei nemici, per un numero di round al giorno pari al livello da mago.
- **Passivo**: bonus pari a 2 + un quinto del livello a Diplomazia, Intimidire e Raggirare.

### Divinazione

È la scuola che squarcia il velo dell'ignoto: apprende segreti da tempo dimenticati, predice il futuro, ritrova oggetti nascosti e dissolve gli incantesimi illusori. I divinatori sono maestri dello scrutamento a distanza e delle profezie, ed esplorano il mondo con la magia prima ancora di percorrerlo: nulla di ciò che è nascosto resta tale al loro sguardo.

- **1°**: Fortuna del Divinatore: come azione standard si tocca una creatura per donarle un bonus di fortuna pari a metà livello (minimo +1) per 1 round.
- **8°**: Adepto Scrutatore [GDR], da concordare col master.
- **Passivo**: bonus all'iniziativa pari a metà livello da mago (minimo +1).

### Evocazione

È la scuola che chiama a sé ciò che è lontano: convoca creature al proprio fianco, crea oggetti dal nulla, richiama esseri da altri piani, guarisce e trasporta attraverso grandi distanze. L'evocatore piega la magia al suo volere e popola il campo con alleati che obbediscono ai suoi comandi, perché ogni distanza, per lui, è solo un'attesa.

- **1°**: Dardo Acido: come azione standard, con un attacco di contatto a distanza contro un bersaglio entro 6 caselle, infligge 1d6 danni da acido + 1 ogni due livelli da mago.
- **8°**: Passo Dimensionale [GDR], da concordare col master.
- **Passivo**: la durata delle magie di evocazione aumenta di un numero di round pari a metà livello (minimo 1).

### Illusione

È la scuola dell'inganno dei sensi e della mente: mostra ciò che non esiste, cela ciò che esiste, fa udire voci fantasma e ricordare fatti mai accaduti. Gli illusionisti tessono trame, finzioni e maschere per confondere e irritare i nemici, e la realtà stessa diventa la loro materia più duttile.

- **1°**: Raggio Accecante: come azione standard, con un attacco di contatto a distanza contro un nemico entro 6 caselle; le creature fino ai tuoi DV restano accecate per 1 round, le altre abbagliate per 1 round.
- **8°**: Campo di Invisibilità: come azione veloce, invisibilità superiore per un numero di round al giorno pari al livello da mago.
- **Passivo**: le illusioni a concentrazione durano un numero di round addizionali pari a metà livello dopo che se ne interrompe la concentrazione.

### Invocazione

È la scuola dell'energia pura, estratta da fonti invisibili per produrre l'effetto voluto: crea dal nulla, e molti dei suoi incantesimi sono spettacolari e devastanti. Gli invocatori si affidano alla potenza bruta della magia, per creare e distruggere con facilità scioccante, e il loro potere non conosce sottigliezze né compromessi.

- **1°**: Dardo di Forza: colpisce automaticamente un nemico entro 6 caselle e infligge 1d4 danni puri + metà livello (minimo +1).
- **8°**: Muro Elementale: muro lungo 4 caselle per livello, di acido, elettricità, freddo o fuoco a scelta, per un numero di round al giorno pari al livello.
- **Passivo**: le magie di invocazione che infliggono danni aggiungono gratis metà livello (minimo +1).

### Necromanzia

È la scuola che manipola il potere della morte, della non vita e della forza vitale, e gran parte di essa riguarda le creature non morte. Il temuto e macabro necromante domina i non morti e volge il potere ripugnante della non vita contro i suoi nemici, là dove la magia tocca il confine tra la vita e ciò che la segue.

- **1°**: Tocco della Tomba: con un attacco di contatto in mischia rende scossa la vittima per un numero di round pari a metà livello; se è già scossa e ha meno DV dei tuoi livelli, resta spaventata per 1 round. Potere sui Non Morti, scelta permanente una volta per sempre tra scacciare e comandare i non morti (usi pari a 3 + INT, più 2 con Incanalare Extra).
- **8°**: Visione della Vita, rivela presenze viventi e non morte intorno (2 caselle, 4 al 12°).
- **Passivo**: nessuno oltre i poteri.

### Trasmutazione

È la scuola che muta le proprietà di creature, cose e condizioni: trasforma i corpi nelle metamorfosi, altera la materia e riscrive ciò che è dato. I trasmutatori plasmano il mondo intorno a loro, e nulla resta uguale sotto le loro mani.

- **1°**: Pugno Telecinetico: con un attacco di contatto a distanza contro un bersaglio entro 6 caselle infligge 1d4 danni fisici + metà livello; al riposo si potenzia Forza, Destrezza o Costituzione (+1 più un quinto del livello).
- **8°**: Cambiare Forma: forma animale o elementale equivalente al 6° (8° al 12°) senza volo, per un numero di round pari al livello.

### Universale

Chi non si specializza appartiene alla scuola universale: nessuna proibizione e nessuno slot vincolato, in cambio della massima versatilità. I maghi generici sono i più versatili tra gli incantatori arcani, perché abbracciano le meraviglie illimitate di tutta la magia invece della profondità di una sola.

- **1°**: Mano dell'Apprendista: come azione standard scaglia da distante l'arma da mischia impugnata contro un bersaglio entro 6 caselle.
- **8°**: Padronanza Metamagica: applica una metamagia posseduta al prossimo lancio pagandone il costo in usi (usi pari a 1 più metà dei livelli oltre l'8°).
- **Passivo**: nessuno oltre i poteri, in cambio di nessuna scuola proibita.
