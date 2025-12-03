---
title: Primi Passi
layout: sistemi
order: 3
excerpt: Tutto il necessario per mettere piede lungo la Costa della Spada in sicurezza
---

# Primi Passi

<img src="{{ '/assets/images/rookie.webp' | relative_url }}" alt="a rookie warrior" style="display: block; margin: 0 auto;" />

<blockquote class="citazione">
  <p>“The game begins with a single step into the unknown.
The adventurer leaves behind a world of comfort and certainty, stepping into the vastness of a realm filled with wonders and perils.
Every decision carves the path forward, shaping not just the fate of the character, but the fate of the world itself.
Here, in these early moments, legends are born.”</p>
  <footer>— <cite>Dungeon Master’s Guide, Chapter 1: A World of Your Own Making</cite></footer>
</blockquote>

Questa sezione é una sorta di corso accelerato per i primissimi momenti di gioco. Altri articoli potrebbero trattare piú a fondo gli argomenti qui descritti

## Indice
- [Riposare](#riposare)
- [Curare](#curare)
- [Riconoscere i PG con il comando .assegnanome](#riconoscere-i-pg-con-il-comando-assegnanome)
- [Come salire di livello](#come-salire-di-livello)
- [Macro per gli incantesimi](#macro-per-gli-incantesimi)
- [Morte](#morte)
- [Messaggistica Interna](#messaggistica-interna)
- [Page](#page)

---

## Riposare
<img src="{{ '/assets/images/riposo.webp' | relative_url }}" alt="riposo" style="display: block; margin: 0 auto;" />

È possibile riposare nelle Locande negli appositi letti o anche all'aperto.  
Nel secondo caso occorre avere nel proprio equipaggiamento alcuni oggetti:

- un sacco a pelo  
- delle pietre focaie  
- un coltellino (un coltellino semplice, non quello intagliatore)

Bisogna usare il coltellino su un albero (non alberi che si trovano nelle città) in modo tale da ricavare dei legnetti che devono essere messi a terra.

Usate poi le pietre focaie sui legnetti in modo tale da accendere un fuoco (non sempre il fuoco si accende subito se non avete un buon grado in Conoscenza Terre Selvagge, quindi riprovate fin quando non si accende).

Una volta acceso il fuoco bisogna:

1. doppio cliccare sul sacco a pelo in prossimità del fuoco, per “preparare il campo”
2. cliccare sul sacco a pelo per iniziare a riposare (o abbandonare il gioco per un corretto log out)

**È severamente vietato** accendere un fuoco e riposare in prossimità delle città o delle strade.

---

## Curare
<img src="{{ '/assets/images/bende.webp' | relative_url }}" alt="medicarsi" style="display: block; margin: 0 auto;" />

Per quanto riguarda le cure si utilizzano delle **bende**.

Potete comprarle dagli appositi NPC o anche da mercanti PG.  
Per sapere dove trovarle potete chiedere in game.

Le bende vanno cliccate e poi si seleziona la tag del PG da curare.

Maggiore è il grado in **Guarire**, più velocemente riuscirete a curare:

- cura più rapida  
- più PF recuperati  
- minori possibilità di fallimento (“Non sei riuscito a curare le ferite”)

---

## Riconoscere i PG con il comando `.assegnanome`
<img src="{{ '/assets/images/assegnanome.webp' | relative_url }}" alt="assegnare nome" style="display: block; margin: 0 auto;" />

Quando incontrate un PG, per riconoscerlo la volta successiva, potete utilizzare il comando:

.assegnanome


Questo associa un nome a quel PG.

Gli NPC hanno nomi che possono essere rivelati solo in quest o tramite intervento GM.

L'intelligenza del personaggio determina quanti nomi è possibile memorizzare.

Se appare il messaggio che non potete ricordare altre persone, potete liberare spazio con:

.assegnanome cancella

---

## Come salire di livello

Si possono accumulare PX:

- andando a mostri  
- ruolando  
- facendo quest

Il Faerûn ha zone adatte anche ai PG di primo livello.

**È sempre consigliato andare a caccia in gruppo**, per sicurezza e per unire exp e role.

Una volta raggiunti i PX richiesti basta eseguire:

.passalivello


### Blocco per voto ruolo

As un certo punto poi potrebbe apparire:

> "La tua media role non è sufficiente a passare di livello."

Questo avviene se non si è raggiunta una buon voto ruolo.

Non esistono scorciatoie: occorre ruolare di più.

---

## Macro per gli incantesimi
<img src="{{ '/assets/images/macro.webp' | relative_url }}" alt="le macro" style="display: block; margin: 0 auto;" />

Andate nel **Pannello Macro**. Per farlo basta schiacciare la freccia in alto a sinistra nello schermo, andare su character, ed infine, nel paperdoll che si aprirá, su opzioni
<img src="{{ '/assets/images/opzioni.webp' | relative_url }}" alt="le opzioni" style="display: block; margin: 0 auto;" />

Per creare macro di incantesimi usate:

- Actions: **say**
- Testo:
 .casta X


Dove **X** è un numero.

Per trovare quel numero:

1. cliccate sul simbolo sacro  
 **oppure**  
 scrivete:

 .spells o .elencospells

<img src="{{ '/assets/images/elencospells.webp' | relative_url }}" alt="gli incantesimi" style="display: block; margin: 0 auto;" />

2. accanto all’incantesimo vedrete qualcosa come:

`Scudo della fede [154]`

Il numero tra parentesi quadre è il valore da usare come X.
In alternativa potete usare anche il nome dell'incantesimo per intero ( esempio, .casta ragnatela)
---

## Morte

Quando si muore si perde un tot di PX.  
Parte può essere recuperata al tempio della propria divinità, cliccando sulla *pietra del perdono*.

Il PG inizierà a pregare, e al termine apparirà:

> "Gli Dei ti hanno graziato"

così recupererete parte dei PX perduti.

Se non pregate:

- potreste ritrovarvi con un livello inferiore in scheda  
- es: livello 6 → morte ×2 → livello 4

Non è un bug: basta pregare.

Esistono anche pietre del perdono sparse nel Faerûn, utilizzabili da PG di qualunque religione.

---

## Messaggistica interna

Potete comunicare in ogni momento con i personaggi online attraverso la messaggistica interna, scrivendo i seguenti comandi
**.msg:**

Utilizza il sistema di messaggistica interna per comunicare con gli altri giocatori in off. Si può disattivare la ricezione dei messaggi con ".msg off" e riattivarla con ".msg on". scrivendolo vi apparirá una lista dei personaggi, e potrete selezionarne uno per poi scrivere un messaggio. Se vi rispondessero o voleste rispondere, potrete farlo anche usando la forma .reply -messaggio-

**.msgt:**
 Permette di inviare un messaggio privato ad un personaggio (sconosciuto) in vista del proprio pg. É simile a .msg ma questa volta vi lascerá selezionare un personaggio visibile a coi mandare direttamente il messaggio.
 potete rispondere a questi messaggi anche con la forma .replyt -messaggio-

---

## Page

Fare un *page* significa mandare un messaggio allo staff.

Si fa tramite il bottone **Aiuto** vicino al paperdoll del PG, selezionando:

> “Voglio fare un page ad un GM”

Il messaggio sarà messo in coda e un membro dello staff risponderà appena possibile.

Le risposte:

- arrivano immediatamente se siete online  
- oppure vengono salvate come messaggio offline per la prossima connessione

**Importante:**  
È concesso **un solo page per personaggio**.  
Se ne inviate un altro, il precedente viene sovrascritto.






