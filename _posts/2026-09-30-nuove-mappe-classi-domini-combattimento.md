---
layout: post
title: "Nuove mappe, classi, domini e combattimento"
date: 2026-09-30
excerpt: "Nuove località del Faerûn occidentale, manovre e combattimento, nuovo sistema comune per compagni e famigli, i 59 domini del Chierico, Druido, Ranger, Monaco e Mago, danni non letali e movimento."
categories: [patch, aggiornamenti, classi, mappe, combattimento]
---

Questa patch arricchisce la mappa con nuove località del Faerûn occidentale e introduce un'ampia revisione dei sistemi di progressione e combattimento, con interventi su manovre, compagni e famigli, Chierico e domini, diverse classi e nuove opzioni tattiche.

## Nuove mappe del Faerûn occidentale

La mappa di Whispers of the Sword Coast si arricchisce di nuove località del Faerûn occidentale, alcune delle quali affondano le proprie radici in una storia molto più antica di quanto il loro aspetto possa lasciar pensare.

### Il Nano Gemente

Nelle Montagne dei Troll si erge una delle opere più imponenti lasciate dai nani: un colossale volto di pietra alto circa 4.000 piedi, scolpito nel fianco del Monte Batyr.

Il vento che attraversa le enormi cavità degli occhi, delle orecchie e della bocca produce un lamento che ha dato origine al nome con cui il monumento è oggi conosciuto.

Ma il Nano Gemente è molto più di una semplice statua. Secondo la tradizione nanica, rappresenta Karlyn di Casa Kuldelver, il condottiero che guidò i nani di Shanatar alla vittoria contro i giganti durante le antiche Guerre dei Giganti. All'interno della montagna si trovava un'intera città nanica, la Fortezza Kuldelvon, abbandonata da millenni e ormai invasa da troll, mostri e altre creature.

La sua enorme facciata guarda verso est, in direzione del Passo di Breakback e delle Giant's Run Mountains.

<div class="wotsc-viewer">

    <button class="wotsc-viewer-prev" aria-label="Immagine precedente">&#10094;</button>

    <figure class="wotsc-viewer-item active">
        <img src="{{ '/assets/images/nanog1.webp' | relative_url }}" alt="Il sacrario tra le cascate">
        <figcaption><strong>Il sacrario tra le cascate</strong>Statue naniche di guardia nella gola.</figcaption>
    </figure>

    <figure class="wotsc-viewer-item">
        <img src="{{ '/assets/images/nanog2.webp' | relative_url }}" alt="Il pozzo nella foresta">
        <figcaption><strong>Il pozzo nella foresta</strong>Un drago bianco in una radura notturna.</figcaption>
    </figure>

    <figure class="wotsc-viewer-item">
        <img src="{{ '/assets/images/nanog3.webp' | relative_url }}" alt="La piattaforma musiva">
        <figcaption><strong>La piattaforma musiva</strong>Rovine colonnate nascoste nel bosco.</figcaption>
    </figure>

    <figure class="wotsc-viewer-item">
        <img src="{{ '/assets/images/nanog4.webp' | relative_url }}" alt="La statua del guerriero">
        <figcaption><strong>La statua del guerriero</strong>Un nano armato di ascia tra le rocce.</figcaption>
    </figure>

    <figure class="wotsc-viewer-item">
        <img src="{{ '/assets/images/nanog5.webp' | relative_url }}" alt="Rovine nella notte">
        <figcaption><strong>Rovine nella notte</strong>Resti di pietra tra i massi delle montagne.</figcaption>
    </figure>

    <button class="wotsc-viewer-next" aria-label="Immagine successiva">&#10095;</button>

    <div class="wotsc-viewer-count">1 / 5</div>

</div>

### La Piana dei Giganti

Una vasta pianura che porta ancora oggi il nome dei suoi antichi abitanti.

Molto tempo fa questo territorio era conosciuto come Karlyn's Vale, in onore del condottiero nanico Karlyn. Fu qui che, attorno al 5350 a.C., le forze di Shanatar affrontarono i giganti e ne massacrarono più di cinquemila, in una delle grandi vittorie naniche delle Guerre dei Giganti.

Con il passare dei secoli il vecchio nome venne dimenticato, ma la memoria di quella battaglia sopravvisse nelle montagne e nelle leggende dei nani.

La Piana non è però soltanto un luogo di antiche battaglie: è attraversata da grandi mandrie migratorie provenienti dalle Western Heartlands, tra cui rothé, cervi e cinghiali. Questi animali attirano a loro volta i draghi della Costa della Spada, che considerano la pianura un autentico terreno di caccia.

### Le Montagne della Corsa dei Giganti

A est della Piana dei Giganti si innalza una catena montuosa appartenente alla grande catena degli Iltkazar.

Anche queste montagne conservano il ricordo della guerra tra nani e giganti: secondo la tradizione nanica, il loro nome deriva proprio dalla caduta di Karlyn's Vale, dove oltre 5.000 giganti trovarono la morte per mano dei nani di Shanatar.

Le montagne sono tutt'altro che disabitate. Goblin e ogre ne percorrono i passi, mentre antiche miniere possono condurre direttamente nelle profondità dell'Underdark. Tra le loro località si trovano il Passo di Breakback e il tranquillo Lago delle Nevi.

E nelle profondità del Monte Dodild, sopra il lago, un tempo dimorava persino il drago verde smeraldo Behrshimmer.

---

## Manovre, lotta e carica

Introdotto **`.manovre`**, una finestra unica per consultare e utilizzare manovre, azioni speciali e opzioni di recupero.

Integrate **disarmare, sbilanciare, spingere, spezzare, oltrepassare, trascinare, riposizionare, rubare, fintare e Sporco Trucco**. Ampliata la **lotta**: presa, mantenimento, immobilizzazione, movimento, liberazione e rilascio. Tutte sono consultabili e utilizzabili dalla finestra **`.manovre`**; molte dispongono anche di comando testuale dedicato.

| Manovre | Comando | Azione |
|---|---|---|
| Disarmare | `.manovre` | Sostituisce un attacco |
| Sbilanciare | `.manovre` | Sostituisce un attacco |
| Botta Sbilanciante | `.bottasbilanciante` | Standard + veloce se il colpo riesce (richiede Attacco Poderoso) |
| Spingere | `.spinta` | Standard |
| Spezzare arma | `.spezzare` | Sostituisce un attacco |
| Spezzare oggetto indossato | `.spezzare oggetto` | Sostituisce un attacco |
| Oltrepassare | `.oltrepassare` | Standard + movimento |
| Trascinare | `.trascinare` | Standard + movimento |
| Riposizionare | `.riposizionare` | Standard |
| Rubare | `.rubare` | Standard |
| Fintare | `.fintare` | Standard (movimento con Fintare Migliorato) |
| Finta con due armi | `.fintare duearmi` | Sacrifica il primo attacco primario |
| Finta a distanza | `.fintare distanza` | Come Fintare; consuma un proiettile |
| Finta gemella | `.fintare gemella` | Come Fintare, su due bersagli vicini |
| Sporco trucco<br>(accecato, abbagliato, assordato,<br>intralciato, scosso, infermo) | `.sporcotrucco <effetto>` | Standard |
| Rimuovere un trucco | `.rimuovitrucco <effetto>` | Azione di movimento |
| Iniziare una presa | `.lotta` | Standard |
| Mantenere la presa | `.lotta mantieni` | Standard (movimento con Lottare Superiore) |
| Infliggere danni letali | `.lotta danno` | Come mantenimento |
| Infliggere danni non letali | `.lotta nonletale` | Come mantenimento |
| Immobilizzare | `.lotta immobilizza` | Come mantenimento |
| Muovere la presa | `.lotta muovi` | Come mantenimento |
| Liberarsi con BMC | `.lotta libera` | Standard |
| Artista della Fuga | `.lotta fuga` | Standard |
| Invertire la presa | `.lotta inverti` | Standard |
| Rilasciare | `.lotta rilascia` | Gratuita |
| Legare con corde | `.lotta lega` | Standard (richiede una corda) |
| Aiutare un alleato | `.lotta aiuta` | Standard |
| Sciogliere le corde | `.lotta sciogli` | Standard |
| Acrobazia | `.acrobazia` | Movimento |
| Acrobazia veloce | `.acrobazia veloce` | Movimento |
| Colpo Basso | `.colpobasso` | Completa |
| Giravolta Sbilanciante | `.giravoltasbilanciante` | Completa (bastone ferrato a due mani) |
| Attacco Rapido | `.attaccorapido` | Completa |
| Tiro in Movimento | `.tiroinmovimento` | Completa |
| Carica | `.caricare` | Vedi sotto |

Collegate le azioni speciali e i talenti posseduti alle relative opzioni del menu. Introdotta la gestione della **Carica** tramite **`.caricare`**, con corretto raccordo al movimento: inseguimento del bersaglio mobile, cambi di direzione e arresto davanti agli ostacoli, senza aumentare la distanza massima consentita. Migliorati i messaggi per bersagli troppo vicini o troppo lontani.

Sistemati messaggi ed emote dei tentativi e degli esiti delle manovre, evitando annunci prematuri o di falso successo. Aggiunti **`.alzati`** e la gestione del tentativo di rialzo automatico dalla posizione prona. Integrate diverse capacità fisiche delle creature con il sistema di combattimento e sistemati richiami di menu, attacchi di opportunità e azioni delle creature.

## Compagni, famigli e servitori

È stato introdotto un sistema comune per **compagni animali, famigli, ombre e servitori**, con gestione unificata di ordini, proprietà, progressione ed equipaggiamento.

Aggiunti i comandi **`.compagni`** e **`.ordina`**, insieme ai comandi dedicati alle diverse categorie di seguaci. Ampliate le funzioni di seguire, proteggere, trasportare e consegnare oggetti, con **accettazione del destinatario** nelle consegne previste dal sistema.

Migliorate gestione della **stalla**, ripristino dell'intelligenza artificiale, pascolo e dissoluzione delle creature evocate. Integrati attacchi fisici, capacità delle specie e condivisione degli incantesimi compatibili. Aggiornati richiamo e recupero dei famigli.

Corretto inoltre un vincolo residuo degli ordini di guardia o girovaga che poteva limitare il successivo inseguimento. Integrate le interazioni dei compagni con ragnatele e poteri di dominio. Sono stati infine integrati **Empatia Selvatica Superiore e Signore della Caccia** con il nuovo sistema di compagni.

## Chierico e domini

Revisionati i poteri dei **59 domini**, fino al 12° livello.

Aggiornato **`.poteredominio`**: selezione dei poteri disponibili e utilizzo diretto tramite nome. Uniformati utilizzi, recupero al riposo, durata degli effetti e gestione dei bonus sovrapposti. L'annullamento del bersaglio non consuma utilizzi.

Integrati i poteri di dominio con combattimento, incantesimi, condizioni e compagni. Aggiunti i comandi dedicati **`.armadanzante`**, **`.ragnatela`** e **`.unitafamiglia`**.

Aggiornate le associazioni dei domini per **17 culti esistenti**, senza introdurre nuove divinità né riassegnare automaticamente i domini dei personaggi.

## Scacciare e Incanalare

Assegnato gratuitamente **Scacciare Non Morti** ai Chierici, evitando duplicazioni. Rivista la gestione di Scacciare: energia positiva con fuga o distruzione, energia negativa con intimorimento o comando, secondo le regole dello shard. La competenza nell'**arma della divinità** è ora integrata.

Collegati gli scacciare speciali alla riserva di **Incanalare**. Corretti limiti e conteggi delle creature controllate, distinguendo categorie e provenienza del controllo. Aggiornate resistenze a Incanalare, interazioni con il **dominio del Sole**, polarità tra curare e infliggere e divieti legati alle scuole di magia contrarie alla fede.

Rimossa l'assegnazione automatica delle **armature pesanti** nei nuovi avanzamenti, senza sottrarla retroattivamente ai personaggi esistenti.

## Incantesimi di dominio

Configurate le liste cumulative dei domini per i circoli dal 1° al 6°, mantenendo un **solo slot di dominio per circolo**. Corretta la preparazione delle alternative e la gestione degli incantesimi duplicati.

Revisionati **Qualsiasi Incantesimo** e **Qualsiasi Incantesimo Superiore**, inclusi requisiti, preparazione e ripristino dopo il riposo.

Alcuni domini hanno ancora incantesimi mancanti e non ancora implementati.

## Druido

Rivista la **Forma Selvatica**, con nuovi profili e gestione delle capacità associate alle forme. Aggiornate durata, scadenza, sensi e interazioni con talenti e combattimento.

Integrata la gestione del **Compagno Animale** con il nuovo sistema comune e aggiornati i comandi di scelta, richiamo e recupero del compagno.

Aggiunto **`.linguaselvaggia`**: con il talento Lingua Selvaggia, sei livelli da druido e una Forma Selvatica attiva, è possibile comunicare con un animale dello stesso genere della forma assunta, per minuti al giorno pari al livello da druido. L'animale risponde comunicando il proprio stato — benessere, dolore, pericolo o fame — senza che la comunicazione ne cambi l'atteggiamento o gli imponga ordini. Con **`.linguaselvaggia stato`** si consultano i minuti residui. Corretti inoltre alcuni collegamenti delle capacità di classe.

## Ranger

Introdotta la scelta del Legame del Cacciatore tramite **`.sceglilegame`**, con la relativa capacità **`.legamecacciatore`**.

Aggiornati Compagno Animale e selettori dello stile di combattimento, con progressione e capacità del compagno integrate nel sistema condiviso.

## Monaco

Revisionati la **riserva di Ki** e i collegamenti dei poteri che la utilizzano. Aggiornati **Integrità del Corpo, Passo Abbondante, Pugno Stordente** e movimento del Monaco.

Sistemati i talenti bonus di classe e integrati **Pugni Potenti** e le azioni speciali del Monaco con combattimento e manovre.

## Mago e preparazione degli incantesimi

Implementato un primo aggiornamento dei **famigli ordinari**, con benefici, condizioni di applicazione e gestione distinta di **Allerta**. Ogni specie conferisce il proprio bonus quando il famiglio è vicino.

<div class="wotsc-esempio" markdown="1">

Il gatto concede +3 a Furtività, il corvo +3 a Valutare e il topo +2 ai tiri salvezza su Tempra.

</div>

Rivista la preparazione tramite **libri, Padronanza degli Incantesimi e Lettura del Magico**, con verifica dei requisiti dopo il riposo.

Introdotto il supporto alla trasmissione delle **magie a contatto** esplicitamente adattate, con gestione delle cariche. Corretto il salvataggio delle singole scelte di **`.spells`**, compresi annullamento, ripresa e limiti delle pagine.

## Danni non letali

Introdotta una gestione dedicata dei **danni non letali**, delle condizioni conseguenti e del recupero.

Aggiunti **`.colpononletale`** e **`.nonletali`**, con le relative informazioni integrate nell'interfaccia e nei controlli di combattimento.

## Movimento e andature

Introdotto un profilo di movimento condiviso per classi, forme, cavalcature, talenti, oggetti ed effetti.

Aggiunto **`.andatura`**, mantenendo **`.velocitamonaco`** come alias. Integrati **Agile, Correre e Piè Veloce**. Corretti il riconoscimento della cavalcatura effettivamente presente e i tempi inviati al client, compresa la gestione dei tempi fra camminata e corsa e delle richieste di movimento respinte.

Ripristinata la gestione nativa della stamina: **camminare non consuma stamina** e la corsa non la consuma fino al 150% della capacità nativa. Rimossi i rallentamenti automatici della velocità base dovuti ad armatura e carico; restano i requisiti per ottenere i bonus di classe e talento. Conservate le limitazioni dovute a magie, condizioni, immobilizzazione e collisioni. Allineate le soglie di carico alla scheda e integrati gli effetti dei domini sul movimento, evitando duplicazioni dei bonus.

## Compagni e guarigione

Per la **bendatura dei compagni**, distinta la semplice modalità combattimento lasciata dall'intelligenza artificiale da un combattimento effettivo. Aggiunti controlli prima del consumo della benda e corretti alcuni posizionamenti delle bende usate.

## Alchimia

Corretti identificativi duplicati e riferimenti errati in alcune **ricette**. Sistemata la creazione delle pozioni dissolventi e di **Destrezza maggiore**.

Migliorati controllo e prenotazione di reagenti e bottiglie, evitando consumi parziali o perdite dovute a errori di creazione. Distinti chiaramente i messaggi della prova di creazione da quelli della successiva prova per ottenere un indizio. Corretta la ripetizione dell'ultima formula e la selezione degli indizi.

## Talenti e recupero delle scelte

È stata corretta la gestione dei **talenti** ottenuti durante l'avanzamento, con controlli contro assegnazioni mancanti e duplicazioni.

È stato introdotto **`.recuperatalenti`** per recuperare le scelte spettanti e **`.completatalento`** per completare le scelte rimaste in sospeso. Sistemati inoltre i selettori dei talenti bonus di **Monaco e Ranger**.

Sono stati aggiornati **43 talenti** con bonus crescenti, compresa la scelta della Professione per Grande Esperienza, e migliorati testi, filtri e impaginazione delle finestre di selezione.

## Abilità e correzioni generali

Allineato **`.provatiro`** al sistema comune delle prove di abilità, comprese le interazioni con aiuti, ritentativi e Riesame.

Aggiornato il sistema alternativo delle **case**, con gestione di aree multiple, chiavi e pannello. Migliorata la disposizione dei pulsanti di **livello, razza e allineamento** nella scheda. Aggiornati i riferimenti alle icone di Ladro e Barbaro, con asset client distribuiti separatamente.
