---
title: Lavorative
layout: sistemi
order: 6
excerpt: Tutto quel che c'é da sapere sul sistema di crafting
---
<img src="{{ '/assets/images/lavorative.png' | relative_url }}" alt="lavorative" style="display: block; margin: 0 auto;" />

- [Lavorative](#lavorative)
  - [Caratteristiche generali](#caratteristiche-generali)

- [Professioni](#professioni)
  - [Agricoltore](#agricoltore)
  - [Cuoco](#cuoco)
  - [Erborista](#erborista)
  - [Metallurgia](#metallurgia)
  - [Taglialegna](#taglialegna)
  - [Pescatore](#pescatore)

- [Artigianato](#artigianato)
  - [Alchimia](#alchimia)
  - [Fabbricare armi e armature](#fabbricare-armi-e-armature)
  - [Falegname](#falegname)
  - [Intagliare pietre / Ferramenta](#ferramenta-e-intagliare-gemme)
  - [Tessitura / Lavorare pellami](#tessitura-e-lavorare-pellami)

# Lavorative

## Caratteristiche generali
L'implementazione delle lavorative é in genere basata su tiri nelle varie skill delle categorie di artigianato e professione, piú gli eventuali bonus di caratteristia o dovute agli oggetti.
Si usa quasi sempre uno strumento, a volte si clicca anche il materiale necessario e dopo un certo tempo, si arriva al momento del tiro che determinerá se la creazione o la raccolta ha successo.
Le lavorative sono divise nel seguente modo

| Tipo di abilità | Nome                                   | Caratteristica               |
|-----------------|----------------------------------------|------------------------------|
| Artigianato     | Artigianato (alchimia)                 | Intelligenza, Destrezza      |
| Artigianato     | Artigianato (fabbricare armi ed armature) | Intelligenza, Forza       |
| Artigianato     | Artigianato (falegnameria)             | Intelligenza, Forza          |
| Artigianato     | Artigianato (ferramenta)               | Intelligenza, Destrezza      |
| Artigianato     | Artigianato (intagliare pietre)        | Intelligenza, Destrezza      |
| Artigianato     | Artigianato (lavorare pellami)         | Intelligenza, Destrezza      |
| Artigianato     | Artigianato (tessitura)                | Intelligenza, Destrezza      |
| Professione     | Professione (metallurgia)              | Saggezza, Forza              |
| Professione     | Professione (agricoltore)              | Saggezza, Forza              |
| Professione     | Professione (cuoco)                    | Saggezza, Destrezza          |
| Professione     | Professione (erborista)                | Saggezza, Destrezza          |
| Professione     | Professione (pescatore)                | Saggezza, Forza              |
| Professione     | Professione (taglialegna)              | Saggezza, Forza              |


---

# Professioni

---

## Agricoltore
<img src="{{ '/assets/images/agricoltura.jpg' | relative_url }}" alt="agricoltura" style="display: block; margin: 0 auto;" />

**Descrizione**  
L’agricoltore é una figura fondamentale per la produzione di piante, frutti e semi necessari a molti altri mestieri come alchimisti, cuochi e sarti.

**Meccaniche**
- Arare: doppio click sull’aratro → click sul terreno.  
- Seminare: doppio click sul seme → click sul terreno arato.  
- Annaffiare/Concimare: doppio click sul secchio/attrezzo → click sul terreno seminato.  
- Cura piante: usare le varie pozioni di cura tramite il pannello fertilizzazione/concimazione.  
- Camminare sul terreno arato o su piantine può danneggiarle o ucciderle.  

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Aratro | Arare il terreno. |
| Secchio | Annaffiare, riempire d’acqua, fertilizzare. |
| Pozione Rinvigorente Vegetale | Ripristina la salute della pianta. |
| Pozione Cura Malattie | Cura malattie delle piante. |
| Pozione di Veleno | Elimina parassiti (come bruchi). |
| Pozione Cura Veleno | Cura funghi/veleni presenti sulla pianta. |
| Tino | Usato per pigiatura e fermentazione (es. uva). |
| Boccette Vuote | Contenitori per imbottigliare prodotti come il vino. |

---
## Cuoco
<img src="{{ '/assets/images/cuoco.jpg' | relative_url }}" alt="cuoco" style="display: block; margin: 0 auto;" />

**Descrizione**
Il cuoco trasforma ingredienti e materie prime in cibo pronto da consumare. Serve a garantire pasti, viveri e preparazioni alimentari utili per la sopravvivenza quotidiana, viaggi, avventure o commercio.

**Meccaniche / Procedura**

**Libro delle ricette** :Viene utilizzato per salvare le varie ricette. Il numero di ricette scrivibili in un libro è limitato (max 20). È possibile copiare una ricetta da un libro ad un altro libro o ad una pergamena vuota cliccando sull’apposito pulsante. Se invece si clicca sul pulsante “prepara”, viene chiesto di selezionare gli ingredienti e gli strumenti necessari alla preparazione. Gli ingredienti vengono selezionati nella giusta quantita’ (anche se lo stack contiene un amount maggiore). Se un ingrediente fa parte di un gruppo (per esempio “aromi”, di cui fanno parte aglio e cipolla), si possono selezionare diversi item che si trovano nel gruppo.
**Ricetta**:Consiste in una pergamena in cui è memorizzata una ricetta (come per il libro delle ricette).

**Comandi**

**.cucina**
Il comando permette di preparare un cibo senza avere a disposizione la ricetta che si intende preparare. Quando si digita il comando .cucina, compare il seguente gump che permette di selezionare gli ingredienti, gli strumenti e il fuoco da utilizzare per cuocere il cibo (nel caso in cui sia necessario).

Nota: gli ingredienti devono essere selezionati nella giusta quantità, quindi, per esempio, se nello zaino si hanno 20 uova e per la ricetta ne servono solo 2, allora bisogna separare prima le due uova dal mucchio e poi selezionarle. Questa è la principale differenza tra l’utilizzo del comando .cucina e l’utilizzo del pulsante “prepara” che si trova nelle ricette o nel libro delle ricette. Nel caso in cui si voglia deselezionare qualcosa, è possibile utilizzare il pulsante X vicino all’Item selezionato. Quando si è sicuri degli elementi selezionati, si può provare a cucinare il cibo premendo sul pulsante OK.
Se la preparazione è andata a buon fine, si può decidere di trascrivere la ricetta su una pergamena o sul libro delle ricette.

**.esamina**
La qualità del cibo creato dipende dalla qualità di tutti gli ingredienti utilizzati nella ricetta. Nel caso in cui degli ingredienti non abbiano una qualità settata, essa viene stabilita in modo “random”. Per ovviare al problema di non sapere la qualità degli ingredienti utilizzati è possibile utilizzare il comando esamina che assegna una qualità random agli item selezionati (applicabile solo sugli item contenuti nel file ingredienti.cfg).
Quando viene selezionato uno stack di ingredienti, essi vengono separati e raggruppati per qualità (come mostrato in figura).

**.arrostire** 
Permette di arrostire alla bell'e meglio costolette di carne o tranci di pesce su un fuoco preparato. Comando utilizzabile senza cd. 



---

## Erborista
<img src="{{ '/assets/images/erborista.jpg' | relative_url }}" alt="erborista" style="display: block; margin: 0 auto;" />

**Descrizione**
Gli alchimisti hanno sempre bisogno di reagenti per le proprie pozioni, e la maggior parte di questi si possono trovare tra le erbe dei verdi prati di Faerûn: solo un attento erborista sarà in grado di riconoscerli e raccoglierli senza danneggiarli, e solo con lo strumento giusto. Grazie all’apposito sradicatore, l’esperto raccoglitore di erbe può selezionare i reagenti migliori e raccoglierli per uso futuro. Anche se il lavoro è lento e ripetitivo, il rendimento è assicurato.

**Meccaniche / Procedura**  
- Equipaggia lo **sradicatore** → due click sullo sradicatore → un click sul terreno verdeggiante.  
- Finché il personaggio resta fermo, continua a cercare fino all’esaurimento della zona. I reagenti raccolti finiscono nello zaino o nella borsa selezionata.  

**Attrezzi necessari** 

| Attrezzo    | Funzione / Utilizzo |
|-------------|----------------------|
| Sradicatore | Usato per cercare e raccogliere erbe/reagenti sul terreno. |

**Materie prime / Reagenti & Risultati possibili** 

| Categoria / Nome | Note / Descrizione |
|------------------|--------------------|
| Fango            | É ovuunque! |
| Letame           | Praticamente oro per gli agricoltori. |
| Vermi            | Creature che si trovano scavando il terreno — usati anche come esche dai pescatori. |
| Reagenti Comuni  | Erbe e reagenti facilmente reperibili: ad esempio Aglio, Bacche, Bozzoli, Cenere Sulfurea, Cenere Vulcanica, Foglie di Vischio, Funghi Bianchi, Funghi Rossi, Funghi Viola, Ginseng, Gusci d'Uova, Muschio Sanguigno, Scarafaggi, Terreni Fertili. |
| Reagenti Rari    | Erbe e ingredienti rari e ricercati: tra questi si trovano Belladonna, Radice di Mandragola, Perla Nera (o altri reagenti speciali) — raccolti solo dagli erboristi più esperti. |

**Note**
- La raccolta può dare risultati variabili: da semplici reagenti comuni a materiali rari.  
- L’uso dello sradicatore è necessario: senza di esso non si può raccogliere in modo efficace.  
- I materiali raccolti da un erborista sono fondamentali per alchimisti, studiosi e altri mestieri che richiedono reagenti.  

---

## Metallurgia
<img src="{{ '/assets/images/metallurgia.jpg' | relative_url }}" alt="metallurgia" style="display: block; margin: 0 auto;" />

**Descrizione**  
Il minatore estrae minerali, metalli e pietre da cave e montagne. Le risorse ottenute alimentano il lavoro di fabbri, inventori e altri artigiani.

**Meccaniche**
- Estrarre: impugnare la piccozza → doppio click → click su terreno roccioso.  
- Continuando a restare fermi si mina fino all’esaurimento.  
- Fusioni e leghe avvengono in forgia usando le pinze da fusione. Basta un doppio click sul lingotto vicino ad una forgia, ma la pinza migliora le possibilitá

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Pala | Scavare terreni sabbiosi o paludosi. (Utile per alcune risorse come la sabbia o l'argilla) |
| Piccozza | Estrazione da terreno roccioso, cave. Utile per metalli e altro |
| Pinze da Fusione | Fondono metalli in forgia e creano leghe. |
| Forgia | Per fondere minerali grezzi in lingotti. |

---

## Taglialegna
<img src="{{ '/assets/images/boscaiolo.jpg' | relative_url }}" alt="boscaiolo" style="display: block; margin: 0 auto;" />

**Descrizione**  
Abbattendo gli alberi, il boscaiolo ricava tronchi e legno utile a molti altri mestieri. Esistono varie tipologie di legno, ognuna con proprietà specifiche.

**Meccaniche**
- Abbattimento: impugnare l’accetta → doppio click → click sull’albero.  
- Se si resta fermi si continua fino all’esaurimento della risorsa.

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Accetta | Abbattere gli alberi e ricavare tronchi. |

---

## Pescatore
<img src="{{ '/assets/images/pescare.jpg' | relative_url }}" alt="Sartoria" style="display: block; margin: 0 auto;" />

**Descrizione**  
Con canna ed esche pesca pesci e a volte oggetti rari o utili come reagenti.

**Meccaniche**
- Selezionare l’esca → usare la canna → click sull’acqua. L'esca non é necessaria ma migliora le possibilitá
- Si consiglia di non lanciare troppo lontano per aumentare la riuscita.

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Canna da Pesca | Strumento principale per pescare. |

---

# Artigianato

---


## Alchimia
<img src="{{ '/assets/images/alchimia.jpg' | relative_url }}" alt="Alchimia" style="display: block; margin: 0 auto;" />

**Descrizione**  
L’alchimista combina reagenti per creare pozioni con vari effetti. Servono solo un mortaio (con pestello) e un’ampolla per contenere il risultato. Generalmente bastano due reagenti, tranne che per i coloranti per cuoio.
Indizi su come combinarli sono nella descrizione in gioco di alcuni reagenti.

**Meccaniche**
- Creare pozione: doppio click sul mortaio → click sul primo reagente → click sul secondo → premere “Esc” per ottenere la pozione.  
- Ricreare una pozione già fatta: doppio click sul mortaio → selezionare il mortaio come target.

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Mortaio | Strumento base per combinare i reagenti. |
| Bottiglie Vuote | Contenitori per le pozioni create. |

---

# Fabbricare armi e armature
<img src="{{ '/assets/images/armi.jpg' | relative_url }}" alt="armi" style="display: block; margin: 0 auto;" />

**Descrizione**
Il fabbro è l’artigiano che, una volta che i metalli sono stati estratti e fusi in lingotti, li lavora per creare armi, armature, utensili e altri oggetti metallici necessari.  
Con incudine, martello da fabbro e lingotti, il fabbro plasma metalli secondo le proprie esigenze, dando vita a spade, corazze, e molto altro.

**Meccaniche / Procedura**  
- Equipaggiare il martello da fabbro → due click sul martello → click su un’incudine vicina → click sui lingotti da usare → nel menu scegliere il tipo di oggetto (es. “Armi” → “Spade” → “Spada lunga”) → dopo il tempo necessario l’oggetto viene creato e finisce nello zaino o nella borsa.  
- Se si vuole, con le pinze per fusione e una forgia è possibile fondere o rifondere oggetti metallici: usare pinze → click sulla forgia → click su un oggetto metallico → si ottengono parte dei lingotti impiegati.

**Attrezzi necessari**  

| Attrezzo / Oggetto        | Funzione / Utilizzo |
|---------------------------|----------------------|
| Incudine                  | Supporto per battere e modellare metalli con martello. |
| Martello da Fabbro        | Strumento principale per forgiare armi/oggetti partendo da lingotti. |
| Forgia                    | Necessaria per fondere metalli o rifondere oggetti. |
| Pinze per Fusione         | Usate insieme alla forgia per fondere o smantellare oggetti in metallo. |
| Incisore                  | Permette di incidere decorazioni o testi su oggetti metallici già creati. |

**Materie prime / Materiali lavorabili** 

I metalli e materiali che un fabbro può utilizzare sono numerosi, da quelli comuni a quelli molto rari. Ecco alcuni esempi tipici:

- Ferro — metallo base, ampiamente usato per armi, utensili e armature.  
- Rame, Bronzo, Ottone, Electrum — metalli e leghe più leggeri o semplici, usati per oggetti meno “bellici” o decorativi.  
- Acciaio — lega resistente per armi e armature robuste.  
- Metalli pregiati o speciali come Argento, Oro, Platino — utilizzati per monili, decorazioni o armi/armature da cerimonia o magiche.  
- Metalli rari o esotici (ad es. Dlarun, Ferro Febbrile, Metallo Vivente, leghe leggendarie come Arandur, Mithral, Adamantio/Adamantite) — materiali rari e difficili da reperire, usati per manufatti di alto livello, con proprietà particolari.  

**Prodotti tipici** 

Un fabbro qualificato può produrre:

- Armi: spade, pugnali, lance, mazze, asce, ecc.  
- Armature e protezioni: corazze, elmi, scudi, gambali, corazze leggere o pesanti a seconda del metallo.  
- Oggetti personalizzati o decorati, grazie all’incisore — ad esempio con incisioni, fregi, decorazioni su armi e armature
**Note**

- La qualità del metallo usato influisce molto su resistenza, durata ed efficacia dell’oggetto finale.  
- La lavorazione richiede attenzione: una forgia, materiali adeguati e strumenti specifici.  
- Un fabbro può anche smantellare o rifondere oggetti, recuperando parte del materiale di base se usa pinze e forgia.  

---

## Falegname
<img src="{{ '/assets/images/falegname.jpg' | relative_url }}" alt="armi" style="display: block; margin: 0 auto;" />

**Descrizione**  
Lavora il legno per creare mobili, contenitori, armi (archi, balestre, bastoni), strumenti e molti altri oggetti. Legni rari permettono creazioni più pregiate.

**Meccaniche**
- Con il coltello intagliatore: doppio click → click sul tronco → scegliere oggetto.  
- Oggetti complessi richiedono sega, martello, pialla, scalpelli e altri strumenti. Possono essere sostituiti con una semplice borsa da falegname

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Coltello Intagliatore | Crea oggetti base partendo dai tronchi. |
| Sega | Trasforma tronchi in assi. |
| Martello | Assemblaggio e creazione di oggetti. |
| Pialla (grande/piccola) | Rifinitura e fabbricazione su assi. |
| Scavatore / Scalpello / Squadra / Coltello Appianatore / Chiodi / Sega a Coda di Rondine | Strumenti vari per mobili e oggetti complessi. |
| Incisore | Per incidere oggetti in legno con testo o decorazioni. |

---

## Ferramenta e Intagliare gemme

**Descrizione**  
L’inventore è un artigiano versatile che unisce materiali diversi (metalli, legni, gemme, argilla, ossa, vetro, scaglie) per creare oggetti complessi, strumenti, monili e armature particolari.
Generalmente parlando intagliare gemme e ferramenta utilizzano lo stesso oggetto, il kit da inventore, ma per scopi diversi. Con ferramenta si fanno utensili da lavoro, e utensili perfetti rendono piú semplice lavorare (-2 sulla cd), mentre con intagliare gemme si possono creare gioielli.
Con intagliare gemme si puó anche usare l'incisore per perfezionare gemme, per esempio creando una gemma perfetta da una grezza, o per romperle e ricavarne frammenti o polveri.

**Meccaniche**
- Usa vari strumenti per tagliare, fondere, assemblare o modellare materiali differenti.  
- Molte operazioni si avviano con doppio click sull’attrezzo → click sul materiale.

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Kit da Inventore | Set base per creazioni e lavorazioni multiple. |
| Punteruolo | Taglio e lavorazione di gemme. |
| Stampo per Chiavi | Copia di chiavi esistenti. (richiede un minimo di ferramenta) |
| Forgia | Ammorbidire e lavorare metalli. |
| Forno | Cuocere argilla per ceramiche e vasellame. |

---

## Tessitura e Lavorare pellami
<img src="{{ '/assets/images/sartoria.jpg' | relative_url }}" alt="Sartoria" style="display: block; margin: 0 auto;" />

**Descrizione**  
Crea vestiti, bende, armature leggere e abiti decorati usando stoffe, pelli o cuoio. Può tingere, incidere o ricamare i capi.

**Meccaniche**
- Doppio click su ago e filo → click su stoffa/pelle → selezionare l’oggetto.  
- Per lavori avanzati: usare forbici, arcolaio, filatoio, kit ricamo, colori, tinozza, incisore per cuoio.
- Per creare rotoli di stoffa in genere serve creare del filo con l'arcolaio (da lana, cotone o seta), e poi tesserlo con il filatoio ( per ottenere i rotoli). I rotoli vanno poi tagliati per ottenere stoffe.
- Per sgrezzare le pelli grezze e poterle lavorare invece dovrete avvicinarvi alla stenditore che trovate in genere nei negozi, usare la forbice sulla pelle che volete stendere, ed aspettare sia pronta.
- Per ottenere pelli il modo piú semplice é scuoiare gli animali con un coltellino.

**Attrezzi**

| Attrezzo | Funzione |
|----------|----------|
| Ago e Filo | Creazione di indumenti e armature leggere. |
| Ferri da Lavoro | Lavorazione gomitoli di lana. |
| Forbici | Tagliare stoffe, pelli, bende. |
| Arcolaio | Trasformare lana/bozzoli in gomitoli. |
| Filatoio | Filare gomitoli per ottenere stoffe. |
| Pelle Stesa | Base di lavorazione per pelli/cuoio. |
| Incisore per Cuoio | Decorazioni e incisioni su pelle. |
| Kit Ricamo | Applicare ricami e decorazioni. |
| Colori + Tinozza | Tingere vestiti e stoffe. |
