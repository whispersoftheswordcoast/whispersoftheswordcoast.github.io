---
layout: post
title: "POL100 ufficiale e novità del client"
date: 2026-11-04
excerpt: "Il passaggio a POL100 è ufficialmente completato, con novità del client e il nuovo sistema case."
categories: [patch, aggiornamenti, server]
---

Il passaggio a POL100 (versione 100.3 *Never gonna give you up*) è ufficialmente completato. La fase di test ha aiutato a correggere quasi tutti i bug noti, e da oggi la nuova versione è quella ufficiale.

<img src="https://static2.klipy.com/ii/d7aec6f6f171607374b2065c836f92f4/52/a6/cskp9zTW.gif" alt="Never gonna give you up" style="display: block; margin: 0 auto;" />

Ci aspettiamo ancora altri piccoli bug o discrepanze dovute alle versioni, ma il sistema è decisamente giocabile ed è già un upgrade rispetto alla vecchia versione. Con POL100 abbiamo anche portato il client all'ultima versione di Ultima Online, Time of Legends, che arriva con oltre 30.000 posti in più per gli asset: nei prossimi mesi e anni potremo personalizzare il server ancora di più.

Se notate qualcosa che non torna, segnalatelo allo staff: ogni feedback aiuta a rifinire gli ultimi dettagli.

---

## Implementazioni client

### Animazioni sdoppiate in movimento

Correre e combattere allo stesso tempo ora si vede davvero: le gambe continuano la corsa mentre il torso attacca o lancia, come due animazioni indipendenti. Anche i vestiti seguono il movimento in modo intero, mantello compreso, invece di spezzarsi a metà. Il risultato è un personaggio sempre leggibile, anche in piena mischia con le gambe in movimento. Le animazioni sdoppiate sono attive da subito e si regolano in Opzioni, nella pagina delle animazioni, alla voce Animazioni in movimento.

<video autoplay muted loop playsinline
       style="display: block; margin: 20px auto; max-width: 100%; width: 480px;">
  <source src="{{ '/assets/images/movimentoanim.mp4' | relative_url }}" type="video/mp4">
</video>

### Anello di stato a terra

Una rinfrescata che porta il gioco al passo coi tempi: invece del modello interamente colorato di rosso, gli stati si leggono ora da un'ellisse colorata sotto i piedi, come nei videogiochi moderni. Veleno, paralisi, invulnerabilità, notorietà del nemico ingaggiato, selezione ed evidenziazione stanno tutte lì, mentre il modello resta normale e leggibile. Sulle creature grosse l'anello cresce un po', fino al doppio del diametro, senza tremolii. Si regola tutto in Opzioni → Video → Effetti di combattimento, con interruttore, spessore e dimensione.

Chi preferisce il vecchio stile può spegnere l'anello: sul nemico ingaggiato torna il colore pieno di notorietà come una volta. È possibile anche togliere entrambi, per chi desidera una visuale più immersiva.

Con l'anello attivo cambiano anche le aure sotto i piedi, quelle del party, del warmode e sempre attive, che diventano ellissi vuote invece del disco pieno. A interruttore spento, tutto come prima.

<img src="{{ '/assets/images/notoriety.webp' | relative_url }}" alt="Anelli di stato sotto i piedi" style="display: block; margin: 0 auto;" />

### Cadaveri della taglia giusta

Sistemata la dimensione dei mostri ridimensionati dopo la morte: il cadavere eredita la taglia di chi muore, niente più draghi grandi come topi. Per ora la soluzione tiene quando il mostro muore in schermata, ma le scale sono per ora sballate se il mostro muore prima che lo possiate vedere.

### Zoom più vicino

Aumentato lo zoom massimo, con due scatti extra di rotella verso il personaggio: per chi desidera vedere da vicino certi modelli, ha uno schermo 4k o vuole semplicemente provare una visuale più immersiva in determinati frangenti.

<div class="wotsc-attention" markdown="1">

Per essere sicuri di usare le DLL corrette, rinominate la cartella shaders nell'installazione per tenerne un backup, oppure cancellatela: senza farlo, le voci che funzionano a dovere sono Ambient, Basic e Advanced. Il consiglio è usare semplicemente il Default, allineato a tutte le novità, e tenere il Basic solo per macchine estremamente vetuste, dove resta un pelo più performante.

</div>

---

## Sistema case

Sistemato il sistema di housing automatico, per gestire stanze, case e negozi facilmente.

### Le basi

Per comprare basta cliccare sull'insegna, se presente, oppure scegliere "casa" dal menu contestuale che appare per le case e le stanze acquistabili. I limiti cambiano in base al valore e tipologia dell'immobile.

<img src="{{ '/assets/images/acquisto.webp' | relative_url }}" alt="Menu di acquisto della casa" style="display: block; margin: 0 auto;" />

### Comandi

Ogni casa può essere gestita tramite un semplice menu digitando `.immobili`, o nel menu contestuale su sé stessi, sotto la voce informazioni.

<img src="{{ '/assets/images/gestione-arredamento.webp' | relative_url }}" alt="Menu di gestione e arredamento" style="display: block; margin: 0 auto;" />

### Ruoli

Possibilità di settare ruoli con diversi privilegi, dall'ingresso alla gestione. Il proprietario è ovviamente il padrone, il comproprietario può gestire l'edificio come desidera, gli amici hanno ingresso libero. I bannati restano fuori da tutto.

### Porte e chiavi

Potete settare le porte di ingresso, decidere se sono pubbliche o private, creare automaticamente lucchetti e chiavi per bauli e porte interne, e potete anche ritirare dal menu una chiave che funziona da token per accedere ai vari menu di gestione interna.

### Personale e cassa

La casa può avere del personale: guardie, vendor e custodi, ognuno col suo stipendio giornaliero. Gli stipendi si pagano da soli, attingendo alla cassa della casa, che è separata dalla banca: finché ci sono fondi tutto funziona, quando finiscono il servizio si sospende. Le assunzioni passano dal menu Personale di `.immobili`, con postazione interna, tetto di 8 e limite per account. Esiste anche un magazzino che va da 50 a 150 spazi a seconda del valore della proprietà.

<img src="{{ '/assets/images/personale.webp' | relative_url }}" alt="Menu del personale della casa" style="display: block; margin: 0 auto;" />


### Sfratti

Con `.wthrecupera` gli oggetti arrivano in banca in sacche nominate per pratica, non più sparsi in giro; se la banca è piena la procedura si ferma e ve lo dice.

### Note finali

Lo staff ha una visuale completa di tutti gli edifici e si riserva la possibilità di rimettere sul mercato qualsiasi proprietà non usata da sei o più mesi, in caso di carenza o peso sul server. Inoltre ogni giocatore potrà avere una singola proprietà privata personale, senza limiti per le comproprietà. Per le proprietà definite "commerciali" se ne potrà avere una sola, che sia proprietà o comproprietà.

<div class="wotsc-esempio" markdown="1">

Herold ha una stanza di proprietà privata ed è comproprietario di un negozio. Può diventare comproprietario di una casa con qualcun altro, ma non comprare un negozio personalmente finché resta comproprietario di quello passato.

</div>

---

## Altri annunci

La banca privata è stata alzata da 300 a 600 spazi, a parità di peso. È stato inoltre aggiunto in gioco il Becco d'Ascia.

<img src="{{ '/assets/images/beccodascia.webp' | relative_url }}" alt="Becco d'Ascia" style="display: block; margin: 0 auto;" />


