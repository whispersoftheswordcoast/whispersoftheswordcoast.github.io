---
title: Domini del chierico
layout: sistemi
order: 25
excerpt: Cosa sono i domini, come si scelgono e come si usano i 59 domini fino al 12° livello
---

# Domini del chierico

In base al dio servito, i chierici hanno a disposizione domini diversi: ogni dio concede i suoi e il chierico ne sceglie 2. Questa guida spiega come si scelgono, come si attivano e cosa fa ognuno dei **59 domini fino al 12° livello**.

## Scegliere i domini

Al `.pgstart`, dopo aver scelto la divinità, il gioco ti chiede di sceglierne **2 domini tra quelli del dio**. Non puoi pescare da altre liste: se il tuo dio non ha il Fuoco, non avrai mai il Fuoco.

La scelta passa anche per l'allineamento. I domini di **Bene e Male** guardano la seconda lettera del tuo allineamento (B, N, M), quelli di **Legge e Caos** la prima (L, N, C). In pratica, un chierico buono non vedrà mai il dominio del Male in lista, e un chierico legale non vedrà mai il Caos.

<div class="wotsc-esempio" markdown="1">
Servi Tymora da Caotico Buono? Potrai prendere Fortuna e Caos, ma non Legge né Male: il gump ti mostra solo ciò che la tua fede e il tuo allineamento permettono. Una volta confermati, i due domini restano tuoi.
</div>

Se cambi dio o domini, serve l'intervento dello staff con `.sceglidomini` o `.assegnadomini`.

## Usarli in gioco

Tutti i poteri passano da un unico comando:

`.poteredominio nome [potere]`

Se scrivi solo il nome del dominio, per esempio `.poteredominio acqua`, si apre il **menu con i poteri disponibili al tuo livello**. Se conosci già il potere, lo scrivi diretto, per esempio `.poteredominio acqua dardo`.

Tre poteri hanno anche una scorciatoia propria che consuma la stessa riserva del dominio: `.armadanzante` per l'arma danzante di Artigianato, `.ragnatela` per le ragnatele dei Ragni e `.unitafamiglia` per l'unità di Famiglia.

### Come si attivano

Molti poteri ostili chiedono un **attacco di contatto**, mentre altri aprono un cursore di bersaglio fino a 6 caselle. I poteri segnati [GDR] sono puramente ruolistici, come parlare con gli animali, scrutare da lontano o saltare tra i piani, e si risolvono nel racconto col master.

In combattimento serve sempre un'**azione**: quasi tutto chiede l'azione standard, pochi poteri quella veloce.

## Usi al giorno e riposo

Ogni potere si può usare un certo numero di volte al giorno e tutte le riserve tornano solo con il riposo. Le indicazioni in gioco si leggono così:

- **Una volta al giorno**: un solo uso, poi serve il riposo.
- **3 + Saggezza al giorno**: parti da 3 usi e aggiungi il modificatore di Saggezza. Con Saggezza +2 sono 5 usi, con +3 sono 6.
- **Pari al livello**: usi o round pari al livello da chierico. Al 5° livello sono 5, al 10° sono 10.
- **Metà livello**: la metà del livello da chierico, arrotondata per difetto. Al 5° livello sono 2, al 10° sono 5.
- **Dall'8° (due dal 12°)**: il potere si sblocca all'8° livello con un uso e dal 12° si usa due volte.

La durata è scritta potere per potere (round, minuti, ore) e parte quando lo attivi. I bonus dello stesso tipo non si sommano mai: se due effetti danno lo stesso tipo di bonus, resta valido solo il più alto.

<div class="wotsc-esempio" markdown="1">
Hai Saggezza +2 e il dardo di fuoco? Lo lanci cinque volte al giorno. Hai l'aura protettiva dall'8°? La accendi una volta al giorno e resta per tutto lo scontro, poi dormi per riaverla.
</div>

## Talenti automatici

Alcuni domini non si attivano: assegnano talenti al momento della scelta.

Luna e Oscurità assegnano **Combattere alla cieca**, Drow ed Equilibrio **Riflessi Fulminei**, Elfi **Tiro Ravvicinato**, Nani **Tempra Possente**, Tempo **Iniziativa Migliorata** e **Allerta**, Fato, Fortuna e Halfling **Fortuna degli Eroi**, Pianificazione **Incantesimo Esteso** dall'8°, Rune **Scrivere Pergamene**, Non-Morte usi di Incanalare aggiuntivi. Guerra e Metalli assegnano competenza e Arma Focalizzata nell'**arma del culto** o in un martello a scelta.

Per questo i domini **Fato, Fortuna, Drow, Elfi, Pianificazione e Tempo** non hanno voci da attivare con `.poteredominio`.

## Gli incantesimi dei domini

Oltre ai poteri, ogni dominio concede i suoi incantesimi: per ogni livello dal 1° al 6° hai un solo slot di dominio, da riempire con gli incantesimi dei tuoi due domini presi dalle liste cumulative. Se entrambi offrono lo stesso incantesimo, lo prepari una volta sola. Li prepari e controlli come gli altri, con `.preparaspells` e `.memo`. I domini Incantesimi e Magia aggiungono il *Qualsiasi Incantesimo*, che si prepara con un piccolo rituale e si gestisce con `.qualsiasiincantesimo`.

## I domini uno per uno

Sotto trovi tutti i 59 domini in ordine alfabetico. Ogni voce elenca i poteri concessi con il livello di sblocco e poi riporta in tabella gli incantesimi concessi dal 1° al 6° circolo. La scritta (non attivo) indica gli incantesimi non ancora implementati nel server: restano in lista ma non partono.

### Acqua

*Poteri concessi: le acque obbediscono alla tua preghiera.*

- **1°**: Scaccia o comanda gli elementali dell'acqua intorno a te (costa 1 uso di Incanalare); lancia un dardo di freddo a un bersaglio entro 6 caselle, che infligge 1d6 più metà livello danni.
- **6°**: Resistenza al freddo 10, sempre attiva.
- **12°**: Resistenza al freddo 20.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Foschia occultante (non attivo) |
| 2 | Nube di nebbia (non attivo) |
| 3 | Respirare sott'acqua |
| 4 | Controllare acqua (non attivo) |
| 5 | Tempesta di ghiaccio |
| 6 | Cono di freddo |

### Animale

*Poteri concessi: le bestie ti riconoscono come uno di loro.*

- **1°**: Natura diventa conoscenza di classe; puoi parlare con gli animali [GDR].
- **4°**: Ricevi un compagno animale con livello pari al tuo meno 3, condiviso con Rettili.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Calmare animali (non attivo) |
| 2 | Blocca animali |
| 3 | Dominare animali |
| 4 | Evoca alleato naturale IV (solo animali) (non attivo) |
| 5 | Comunione con la natura (non attivo), Forma Ferina III (solo animali) (non attivo) |
| 6 | Guscio anti-vita (non attivo) |

### Aria

*Poteri concessi: i venti portano lontano la tua voce.*

- **1°**: Scaccia o comanda gli elementali dell'aria intorno a te (costa 1 uso di Incanalare); lancia un dardo elettrico a un bersaglio entro 6 caselle, che infligge 1d6 più metà livello danni.
- **6°**: Resistenza all'elettricità 10, sempre attiva.
- **12°**: Resistenza all'elettricità 20.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Foschia occultante (non attivo) |
| 2 | Muro di vento (non attivo) |
| 3 | Forma gassosa (non attivo) |
| 4 | Camminare nell'aria (non attivo) |
| 5 | Controllare venti (non attivo) |
| 6 | Catena di fulmini |

### Artigianato

*Poteri concessi: le tue mani danno forma e vita alla materia.*

- **1°**: Prendi +1 livello quando crei oggetti e Abilità Focalizzata in un Artigianato a scelta; ripari 1d4 danni agli oggetti con un rituale di dieci minuti; con il tocco danneggi oggetti e costrutti.
- **8°**: Doni all'arma quattro round da danzante, così combatte da sola, poi la liberi e la riprendi con le azioni apposite.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Animare corde (non attivo) |
| 2 | Scolpire legno (non attivo) |
| 3 | Scolpire pietra (non attivo) |
| 4 | Creazione minore (non attivo) |
| 5 | Muro di pietra, Fabbricare (non attivo) |
| 6 | Macchina fantastica (non attivo), Creazione maggiore (non attivo) |

### Bene

*Poteri concessi: la luce del bene arde in te più forte che negli altri.*

- **1°**: Prendi +1 livello agli incantesimi del bene; con il tocco dai a un alleato un bonus per colpire pari a metà livello (minimo 1) per un round.
- **8°**: Rendi sacra l'arma impugnata per metà livello in round.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Protezione dal male |
| 2 | Aiuto, Allineare arma (bene) (non attivo) |
| 3 | Cerchio magico contro il male |
| 4 | Punizione sacra (non attivo) |
| 5 | Dissolvi il male (non attivo) |
| 6 | Barriera di lame (non attivo) |

### Caos

*Poteri concessi: il caos danza al ritmo del tuo cuore.*

- **1°**: Prendi +1 livello agli incantesimi del caos.
- **8°**: Rendi anarchica l'arma impugnata.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Protezione dalla legge (non attivo) |
| 2 | Frantumare (non attivo), Allineare arma (caos) (non attivo) |
| 3 | Cerchio magico contro la legge |
| 4 | Martello del caos (non attivo) |
| 5 | Dissolvi la legge (non attivo) |
| 6 | Animare oggetti (non attivo) |

### Castigo

*Poteri concessi: nessun torto subito resta senza risposta.*

- **1°**: Dopo una ferita, una volta al giorno dichiari vendetta: il prossimo attacco contro chi ti ha colpito, se va a segno, infligge danni massimi. Qualsiasi altra azione prima dell'attacco la spezza.
- **8°**: Puoi armare anche la risposta immediata, che parte da sola quando ti colpiscono.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Scudo della fede |
| 2 | Vigore |
| 3 | Parlare con i morti (non attivo) |
| 4 | Scudo di fuoco (non attivo) |
| 5 | Sigillo di giustizia (non attivo) |
| 6 | Esilio |

### Caverne

*Poteri concessi: la pietra ti conosce per nome.*

- **1°**: Diventi esperto minatore e lanci un dardo acido entro 6 caselle (1d6 più metà livello danni).
- **8°**: Nelle zone sotterranee vedi al buio e hai bonus a Furtività e iniziativa; arrampicata [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Individuazione delle porte segrete (non attivo), Pietra magica (non attivo) |
| 2 | oscurità (non attivo), Creare fossa (non attivo) |
| 3 | Fondersi nella pietra (non attivo), Fossa con spuntoni (non attivo) |
| 4 | Riparo sicuro di Leomund (non attivo), Rocce aguzze (non attivo) |
| 5 | Passapareti (non attivo), Muro di pietra |
| 6 | Scopri il percorso (non attivo), Fossa affamata (non attivo) |

### Charme

*Poteri concessi: il tuo sorriso disarma prima della spada.*

- **1°**: Una volta al giorno alzi il Carisma di 4 per un minuto; con il tocco frastorni un nemico per un round.
- **8°**: Il charme rapido convince un PNG a non aggredirti (sui PG [GDR]).

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Charme |
| 2 | Calmare emozioni (non attivo) |
| 3 | Suggestione (non attivo) |
| 4 | Buone speranze (non attivo), Eroismo (non attivo) |
| 5 | Charme sui mostri |
| 6 | Costrizione/Cerca (non attivo) |

### Commercio

*Poteri concessi: ogni strada è mercato e ogni parola è moneta.*

- **1°**: Cammini 3 metri più veloce e la lingua d'argento dà un bonus pari a metà livello (minimo 1) alla prossima prova sociale.
- **8°**: Lettura dei pensieri e balzo dimensionale [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Messaggio (non attivo), Disco fluttuante (non attivo) |
| 2 | Gemma esplosiva (non attivo), Localizza oggetto (non attivo) |
| 3 | Splendore dell'Aquila, Volare (non attivo) |
| 4 | Inviare (non attivo), Porta dimensionale |
| 5 | Fabbricare (non attivo), Volo giornaliero (non attivo) |
| 6 | Visione del vero, Scopri il percorso (non attivo) |

### Conoscenza

*Poteri concessi: nessun segreto resiste al tuo sguardo.*

- **1°**: Le Conoscenze diventano abilità di classe; prendi +1 livello alle divinazioni; con il tocco consulti il bestiario sulle creature.
- **6°**: Visione remota [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Individuazione delle porte segrete (non attivo), Comprensione dei linguaggi |
| 2 | Individuazione dei pensieri (non attivo) |
| 3 | Chiaroudienza/Chiaroveggenza (non attivo), Parlare con i morti (non attivo) |
| 4 | Divinazione (non attivo) |
| 5 | Visione del vero |
| 6 | Scopri il percorso (non attivo) |

### Distruzione

*Poteri concessi: dove passi, il mondo si ricorda di poter crollare.*

- **1°**: Armi la punizione per il prossimo tentativo in mischia (uso speso anche se manchi): la breve aggiunge metà livello ai danni (minimo 1), la forte una volta al giorno aggiunge tutto il livello.
- **8°**: Apri un'aura che dura un round per uso: i critici contro i nemici vicini si confermano da soli e i danni morali crescono di metà livello.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Infliggi ferite leggere, Colpo accurato (non attivo) |
| 2 | Frantumare (non attivo) |
| 3 | Contagio (non attivo), Ira (non attivo) |
| 4 | Infliggi ferite critiche |
| 5 | Infliggi ferite leggere di massa (non attivo), Grido (non attivo) |
| 6 | Ferire |

### Drow

*Poteri concessi: i riflessi degli elfi oscuri scorrono nel tuo sangue.*

- Solo talento automatico: Riflessi Fulminei. Nessun potere da attivare.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Mantello di potere oscuro (non attivo) |
| 2 | Chiaroudienza/Chiaroveggenza (non attivo) |
| 3 | Suggestione (non attivo) |
| 4 | Rivela bugie (non attivo) |
| 5 | Forma di ragno (non attivo) |
| 6 | Dissolvere superiore |

### Elfi

*Poteri concessi: l'occhio elfico non sbaglia mai la mira.*

- Solo talento automatico: Tiro Ravvicinato. Nessun potere da attivare.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Colpo accurato (non attivo) |
| 2 | Grazia felina |
| 3 | Calappio |
| 4 | Traslazione arborea |
| 5 | Comunione con la natura (non attivo) |
| 6 | Scopri il percorso (non attivo) |

### Equilibrio

*Poteri concessi: la bilancia del mondo pende dalla tua quiete.*

- **1°**: Una volta al giorno aggiungi Saggezza alla CA per un numero di round pari al livello; hai Riflessi Fulminei gratis.
- **8°**: Ottieni anche Saldo e agile.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Riparare superiore (non attivo) |
| 2 | Calmare emozioni (non attivo) |
| 3 | Chiarezza mentale (non attivo) |
| 4 | Congedo |
| 5 | Santuario di massa (non attivo) |
| 6 | Esilio |

### Famiglia

*Poteri concessi: il sangue chiama sangue, e tu rispondi.*

- **1°**: Difendi con +2 schivare e con i legami prendi su di te una condizione di un alleato toccandolo, per 3 più Saggezza round al giorno.
- **8°**: Armi l'Unità con consenso del gruppo: gli effetti si condividono.
- **12°**: Due usi per effetto condiviso.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Benedizione |
| 2 | Scudo su altri, Calmare emozioni (non attivo) |
| 3 | Mano soccorrevole (non attivo), Creare cibo ed acqua (non attivo) |
| 4 | Infondere capacita magiche (non attivo) |
| 5 | Legame telepatico di Rary (non attivo) |
| 6 | Banchetto degli eroi (non attivo) |

### Fanghiglie

*Poteri concessi: anche il fango riconosce il suo padrone.*

- **1°**: Comandi le melme con 1 uso di Incanalare (limite di DV separato); dardo acido entro 6 caselle.
- **6°**: Resistenza all'acido 10.
- **12°**: Resistenza all'acido 20.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Unto (non attivo), Pietra magica (non attivo) |
| 2 | Freccia acida di Melf, Ammorbidire terra e pietra (non attivo) |
| 3 | Veleno, Scolpire pietra (non attivo) |
| 4 | Stretta corrosiva (non attivo), Rocce aguzze (non attivo) |
| 5 | Tentacoli neri di Evard (non attivo), Muro di pietra |
| 6 | Trasmutare roccia in fango (non attivo), Pelle di pietra |

### Fato

*Poteri concessi: il destino ti ha già scelto, e ti protegge.*

- Solo talento automatico: Fortuna degli Eroi. Nessun potere da attivare.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Colpo accurato (non attivo) |
| 2 | Presagio (non attivo) |
| 3 | Scagliare maledizione (non attivo), Fortuna in prestito (non attivo) |
| 4 | Divinazione (non attivo), Libertà di movimento |
| 5 | Sigillo di giustizia (non attivo), Spezzare incantesimo |
| 6 | Costrizione/Cerca (non attivo), Fuorviare |

### Fortuna

*Poteri concessi: la sorte siede alla tua tavola.*

- Solo talento automatico: Fortuna degli Eroi. Nessun potere da attivare.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Scudo entropico (non attivo), Colpo accurato (non attivo) |
| 2 | Aiuto |
| 3 | Protezione dagli elementi |
| 4 | Libertà di movimento |
| 5 | Spezzare incantesimo |
| 6 | Fuorviare |

### Forza

*Poteri concessi: i giganti ti guardano con rispetto.*

- **1°**: Una volta al giorno l'Impresa aggiunge tutto il tuo livello alla Forza per un round; il tocco dà un bonus pari a metà livello (minimo 1) per un round.
- **8°**: La Forza degli Dei dà un bonus pari al livello a prove e abilità (non attacchi e danni), un uso per round. Riserve condivise con Orchi.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Ingrandire Persone |
| 2 | Forza straordinaria |
| 3 | Veste magica |
| 4 | immunità agli incantesimi (non attivo) |
| 5 | Giusto potere |
| 6 | Pelle di pietra |

### Freddo

*Poteri concessi: l'inverno abita nel tuo respiro.*

- **1°**: Scacci il fuoco e comandi il freddo con 1 uso di Incanalare; dardo di freddo entro 6 caselle.
- **8°**: La forma glaciale ti rende immune al freddo e ti dà RD 5 per un numero di round pari al livello, ma il fuoco ti ferisce doppio.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Tocco Gelido (non attivo), Foschia occultante (non attivo) |
| 2 | Gelare il metallo (non attivo), Nube di nebbia (non attivo) |
| 3 | Tempesta di nevischio (non attivo), Respirare sott'acqua |
| 4 | Tempesta di ghiaccio, Controllare acqua (non attivo) |
| 5 | Muro di ghiaccio |
| 6 | Cono di freddo |

### Fuoco

*Poteri concessi: le fiamme ti salutano come un fratello.*

- **1°**: Scaccia o comanda gli elementali del fuoco intorno a te (costa 1 uso di Incanalare); lancia un dardo di fuoco a un bersaglio entro 6 caselle, che infligge 1d6 più metà livello danni.
- **6°**: Resistenza al fuoco 10, sempre attiva.
- **12°**: Resistenza al fuoco 20.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Mani brucianti |
| 2 | Produrre fiamma (non attivo) |
| 3 | Resistere agli elementi, Palla di fuoco |
| 4 | Muro di fuoco |
| 5 | Scudo di fuoco (non attivo) |
| 6 | Semi di fuoco (non attivo) |

### Gnomi

*Poteri concessi: la realtà è solo un suggerimento.*

- **1°**: Prendi +1 livello alle illusioni (non si cumula con Illusioni); condividi un solo doppio e il velo con Inganno e Illusioni.
- **8°**: Stendi il velo sul gruppo: cambia corpo, colore e nome, non gli abiti.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Immagine silenziosa (non attivo), Cambiare sembianze (non attivo) |
| 2 | Gemma esplosiva (non attivo), Invisibilità |
| 3 | Immagine minore (non attivo), Anti-individuazione |
| 4 | Creazione minore (non attivo), Confusione |
| 5 | Terreno illusorio (non attivo), Visione falsa (non attivo) |
| 6 | Macchina fantastica (non attivo), Fuorviare |

### Guarigione

*Poteri concessi: le tue mani ricordano al corpo come stare bene.*

- **1°**: Prendi +1 livello alle cure; tocchi un vivente svenuto sotto zero e lo curi di 1d4 più metà livello per rialzarlo.
- **6°**: Le tue cure sono potenziate del 50%.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Cura ferite leggere |
| 2 | Cura ferite moderate |
| 3 | Cura ferite gravi |
| 4 | Cura ferite critiche |
| 5 | Cura ferite leggere di massa (non attivo), Respiro di Vita (non attivo) |
| 6 | Guarigione |

### Guerra

*Poteri concessi: la battaglia ti riconosce come suo figlio.*

- **1°**: Competenza e Arma Focalizzata nell'arma del culto; con il tocco dai a un alleato un bonus morale ai danni pari a metà livello (minimo 1) per un round.
- **8°**: Scegli dal menu un talento di combattimento temporaneo, che resta attivo fino a un numero di round pari al tuo livello (un uso per round).

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Arma magica |
| 2 | Arma Spirituale |
| 3 | Veste magica |
| 4 | Potere divino |
| 5 | Colpo infuocato |
| 6 | Barriera di lame (non attivo) |

### Halfling

*Poteri concessi: piccolo di statura, grande di fortuna.*

- **1°**: Hai Fortuna degli Eroi; una volta al giorno aggiungi Carisma a Scalare, Furtività e salti per dieci minuti.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Pietra magica (non attivo), Colpo accurato (non attivo) |
| 2 | Grazia felina, Aiuto |
| 3 | Veste magica, Protezione dagli elementi |
| 4 | Libertà di movimento |
| 5 | Segugio fedele di Mordenkainen (non attivo), Spezzare incantesimo |
| 6 | Muovere il terreno (non attivo), Fuorviare |

### Illusioni

*Poteri concessi: il vero e il falso si confondono al tuo passaggio.*

- **1°**: Prendi +1 livello alle illusioni; alzi un solo doppio illusorio, condiviso con Inganno e Gnomi.
- **8°**: Stendi il velo sul gruppo.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Immagine silenziosa (non attivo), Cambiare sembianze (non attivo) |
| 2 | Immagine minore (non attivo), Invisibilità |
| 3 | Distorsione, Anti-individuazione |
| 4 | Allucinazione mortale, Confusione |
| 5 | Immagine persistente (non attivo), Visione falsa (non attivo) |
| 6 | Fuorviare |

### Incantesimi

*Poteri concessi: ogni magia è una porta che sai aprire.*

- **1°**: Liste cumulative con Qualsiasi Incantesimo, da preparare con un rituale.
- **8°**: Tocco dissolutore che spegne le magie attive (condiviso con Magia).

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Armatura magica, Aura magica (non attivo) |
| 2 | Silenzio, Bocca magica |
| 3 | Qualsiasi incantesimo, Dissolvi magie |
| 4 | Potenziatore mnemonico di Rary (non attivo), Occhio Arcano (non attivo) |
| 5 | Spezzare incantesimo, Resistenza agli incantesimi |
| 6 | Qualsiasi incantesimo superiore, Analizzare dweomer |

### Inganno

*Poteri concessi: la verità ti invidia.*

- **1°**: Le abilità del dominio diventano di classe; alzi un solo doppio, condiviso con Illusioni e Gnomi.
- **8°**: Stendi il velo sul gruppo.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Cambiare sembianze (non attivo) |
| 2 | Invisibilità |
| 3 | Anti-individuazione |
| 4 | Confusione |
| 5 | Visione falsa (non attivo) |
| 6 | Fuorviare |

### Legge

*Poteri concessi: l'ordine del cosmo parla con la tua voce.*

- **1°**: Prendi +1 livello agli incantesimi della legge.
- **8°**: Rendi assiomatica l'arma impugnata.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Protezione dal caos (non attivo) |
| 2 | Calmare emozioni (non attivo), Allineare arma (legge) (non attivo) |
| 3 | Cerchio magico contro il caos |
| 4 | Ira dell'ordine (non attivo) |
| 5 | Dissolvi il caos (non attivo) |
| 6 | Blocca mostri |

### Luna

*Poteri concessi: la luna ti conta tra i suoi figli.*

- **1°**: Hai Combattere alla cieca; scacci i licantropi con 1 uso di Incanalare; il tocco avvolge d'ombra per metà livello in round (minimo 1).
- **8°**: Colpisci col fuoco lunare: tanti d8 quanta è metà livello, TS Riflessi dimezza e chi fallisce resta abbagliato.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Luminescenza (non attivo) |
| 2 | Bagliore lunare (non attivo), Cecità/Sordità |
| 3 | Lama lunare (non attivo), oscurità profonda (non attivo) |
| 4 | Buone speranze (non attivo), Lunaticismo (non attivo) |
| 5 | Sentiero lunare (non attivo), Evoca Mostri V (evoca 1d3 Ombre) (non attivo) |
| 6 | Immagine permanente (non attivo), Sogno (non attivo) |

### Magia

*Poteri concessi: la Trama ti accarezza quando la sfiori.*

- **1°**: Usi gli oggetti magici come un mago di metà livello; la mano dell'accolito colpisce a distanza tirando con Saggezza e poi torna.
- **8°**: Tocco dissolutore (condiviso con Incantesimi).

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Aura magica (non attivo), Identificare |
| 2 | Bocca magica |
| 3 | Dissolvi magie |
| 4 | Infondere capacita magiche (non attivo) |
| 5 | Resistenza agli incantesimi |
| 6 | Campo anti-magia (non attivo) |

### Male

*Poteri concessi: l'oscurità ti ha scelto come voce.*

- **1°**: Prendi +1 livello agli incantesimi del male; il tocco rende infermo e tratta il bersaglio come buono per gli effetti malvagi, senza cambiarne l'allineamento.
- **8°**: Rendi sacrilega l'arma impugnata.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Protezione dal bene |
| 2 | Dissacrare (non attivo), Allineare arma (male) (non attivo) |
| 3 | Cerchio magico contro il bene |
| 4 | Influenza sacrilega (non attivo) |
| 5 | Dissolvi il bene (non attivo) |
| 6 | Creare non morti |

### Mentalismo

*Poteri concessi: i pensieri altrui sono libri aperti.*

- **1°**: Le Conoscenze diventano di classe; con il tocco consulti il bestiario; una volta al giorno l'interdizione dà resistenza pari a livello più 2 al prossimo Volontà entro un'ora.
- **6°**: Visione remota [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Confusione inferiore (non attivo), Comprensione dei linguaggi |
| 2 | Individuazione dei pensieri (non attivo) |
| 3 | Chiaroudienza/Chiaroveggenza (non attivo), Parlare con i morti (non attivo) |
| 4 | Modificare memoria (non attivo), Divinazione (non attivo) |
| 5 | Nebbia mentale, Visione del vero |
| 6 | Legame telepatico di Rary (non attivo), Scopri il percorso (non attivo) |

### Metalli

*Poteri concessi: il ferro canta sotto le tue mani.*

- **1°**: Competenza e Focalizzata in un martello a scelta; resistenza all'acido; i pugni metallici partono con l'azione veloce e durano un round, con danno migliore e capaci di ignorare durezza fino a 10.
- **6°**: Resistenza all'acido 10.
- **12°**: Resistenza all'acido 20.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Arma magica, Pietra magica (non attivo) |
| 2 | Riscaldare il metallo (non attivo) |
| 3 | Estremità affilata (non attivo), Scolpire pietra (non attivo) |
| 4 | Stretta corrosiva (non attivo), Rocce aguzze (non attivo) |
| 5 | Muro di ferro, Muro di pietra |
| 6 | Barriera di lame (non attivo) |

### Morte

*Poteri concessi: la morte ti ascolta prima di colpire.*

- **1°**: Il tocco mortale può uccidere chi è quasi morto; il tocco sanguinante fa perdere 1d6 per round finché dura (metà livello in round, minimo 1).
- **8°**: L'energia negativa ti cura invece di ferirti.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Incuti paura |
| 2 | Rintocco di morte (non attivo) |
| 3 | Animare morti |
| 4 | Interdizione alla morte |
| 5 | Distruggere viventi |
| 6 | Creare non morti |

### Nani

*Poteri concessi: la montagna ti ha fatto le ossa.*

- **1°**: Hai Tempra Possente gratis.
- **8°**: La tenacia della pietra dà RD 3 per un round.
- **12°**: RD 5.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Arma magica |
| 2 | Vigore |
| 3 | Glifo di interdizione (non attivo) |
| 4 | Arma magica superiore |
| 5 | Fabbricare (non attivo) |
| 6 | Pietre parlanti (non attivo) |

### Nobiltà

*Poteri concessi: i potenti ti ascoltano, i deboli ti seguono.*

- **1°**: Ispiri gli alleati vicini per un numero di round pari al Carisma (minimo 1) e risollevi il singolo con la parola (+2 morale per metà livello in round, minimo 1, senza cumuli).
- **8°**: Autorità sui seguaci [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Favore divino |
| 2 | Estasiare (non attivo) |
| 3 | Veste magica |
| 4 | Rivela bugie (non attivo) |
| 5 | Comando superiore |
| 6 | Costrizione/Cerca (non attivo) |

### Non-Morte

*Poteri concessi: cammini sul confine tra due mondi.*

- **1°**: Quattro usi di Incanalare in più; il tocco ti fa reagire alle energie come un non morto, senza cambiare tipo: la positiva ti ferisce e la negativa ti cura per metà livello in round (minimo 1).
- **8°**: L'energia negativa ti cura.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Individuazione dei non morti (non attivo), Incuti paura |
| 2 | Dissacrare (non attivo), Tocco del ghoul |
| 3 | Animare morti |
| 4 | Interdizione alla morte, Debilitazione |
| 5 | Infliggi ferite leggere di massa (non attivo), Distruggere viventi |
| 6 | Creare non morti |

### Oceano

*Poteri concessi: il mare ti porta rispetto.*

- **1°**: Resisti al freddo; respiri sott'acqua [GDR]; con l'ondata spingi o trascini, tirando livello più Saggezza contro la difesa di manovra.
- **6°**: Resistenza al freddo 10.
- **12°**: Resistenza al freddo 20.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Contrastare elementi, Foschia occultante (non attivo) |
| 2 | Suono dirompente (non attivo), Risucchio (non attivo) |
| 3 | Respirare sott'acqua, Camminare sull'acqua (non attivo) |
| 4 | Libertà di movimento, Controllare acqua (non attivo) |
| 5 | Muro di ghiaccio, Tempesta di ghiaccio |
| 6 | Sfera congelante di Otiluke (non attivo), Cono di freddo |

### Odio

*Poteri concessi: il tuo rancore ha un nome e un volto.*

- **1°**: Marchi un nemico per un minuto.
- **8°**: Scateni contro il marchiato l'ostilità implacabile per un round.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Devastazione |
| 2 | Spaventare |
| 3 | Scagliare maledizione (non attivo) |
| 4 | Canto di discordia (non attivo) |
| 5 | Giusto potere |
| 6 | Proibizione (non attivo) |

### Orchi

*Poteri concessi: la furia della tribù brucia in te.*

- **1°**: Punisci una volta al giorno con danni pari al livello (+4 al tiro contro elfi e nani, uso speso anche se manchi); tocco e Forza condivisi con Forza.
- **8°**: Forza degli Dei.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Incuti paura, Ingrandire Persone |
| 2 | Produrre fiamma (non attivo), Forza straordinaria |
| 3 | Preghiera, Veste magica |
| 4 | Potere divino, immunità agli incantesimi (non attivo) |
| 5 | Occhi indagatori (non attivo), Giusto potere |
| 6 | Sguardo penetrante (non attivo), Pelle di pietra |

### Oscurità

*Poteri concessi: il buio ti copre come un mantello.*

- **1°**: Hai Combattere alla cieca; il tocco avvolge d'ombra per metà livello in round (minimo 1).
- **8°**: Gli occhi dell'oscurità vedono nelle tenebre per metà livello in round al giorno.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Foschia occultante (non attivo) |
| 2 | Cecità/Sordità |
| 3 | Luce nera (non attivo), oscurità profonda (non attivo) |
| 4 | Armatura di oscurità (non attivo), Ombra di una evocazione (non attivo) |
| 5 | Fulmine oscuro (non attivo), Evoca Mostri V (evoca 1d3 Ombre) (non attivo) |
| 6 | Occhi indagatori (non attivo), Camminare nelle Ombre (non attivo) |

### Pianificazione

*Poteri concessi: niente accade per caso, se lo hai previsto tu.*

- **1°**: Applichi gratis gli incantesimi prolungati.
- **8°**: Ottieni Allerta.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Visione della morte (non attivo) |
| 2 | Presagio (non attivo) |
| 3 | Chiaroudienza/Chiaroveggenza (non attivo) |
| 4 | Infondere capacita magiche (non attivo) |
| 5 | Individuazione dello scrutamento (non attivo) |
| 6 | Banchetto degli eroi (non attivo) |

### Portali

*Poteri concessi: ogni soglia nasconde una strada che conosci.*

- **1°**: Cerchi i portali con CD 20.
- **8°**: Balzo dimensionale [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Evoca mostri I |
| 2 | Analizzare portale (non attivo) |
| 3 | Ancora dimensionale (non attivo) |
| 4 | Porta dimensionale |
| 5 | Teletrasporto (non attivo) |
| 6 | Esilio |

### Protezione

*Poteri concessi: sei lo scudo dietro cui gli altri respirano.*

- **1°**: Aggiungi 1 più un quinto del livello ai tiri salvezza e puoi prestare la resistenza a un alleato col tocco per un minuto o marchiarlo per dargli un bonus pari al livello al prossimo tiro entro un'ora.
- **8°**: L'aura protettiva dura un round per uso e dà +10 deviazione alla CA (+20 al 12°) più resistenze elementali 5.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Santuario (non attivo) |
| 2 | Scudo su altri |
| 3 | Protezione dagli elementi |
| 4 | immunità agli incantesimi (non attivo) |
| 5 | Resistenza agli incantesimi |
| 6 | Campo anti-magia (non attivo) |

### Ragni

*Poteri concessi: la tela aspetta solo il tuo comando.*

- **1°**: Intimorisci e comandi con 1 uso di Incanalare; movimenti [GDR].
- **8°**: Stendi la ragnatela: ancoraggi, TS Riflessi, fuga, terreno difficile, copertura e fuoco che la brucia.
- **12°**: Due ragnatele al giorno.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Movimenti del ragno (non attivo) |
| 2 | Evoca sciame (ragni) (non attivo) |
| 3 | Destriero fantomatico (cavalcatura ragno) (non attivo) |
| 4 | Parassiti giganti (non attivo) |
| 5 | Piaga degli insetti (sciami di ragni) (non attivo) |
| 6 | Maledizione del ragno (non attivo) |

### Rettili

*Poteri concessi: i rettili sentono in te un antico padrone.*

- **1°**: Comandi i rettili con 1 uso di Incanalare (limite DV separato); lo sguardo affascina fino al tuo prossimo turno (1d6 più metà livello danni puri; TS Volontà CD 10 + metà livello + Sag nega; una minaccia lo interrompe).
- **4°**: Ricevi un serpente con livello pari al tuo meno 3.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Zanna magica |
| 2 | Trance animale (non attivo) |
| 3 | Zanna magica superiore |
| 4 | Veleno |
| 5 | Crescita animale (rettili/serpenti) (non attivo) |
| 6 | Sguardo penetrante (non attivo) |

### Rinnovamento

*Poteri concessi: la vita ricomincia da te, ogni volta.*

- **1°**: Una volta il recupero automatico ti salva dal colpo mortale; il tocco rimuove fatica, barcollamento, frastorno, infermità e scosse.
- **6°**: Le tue cure sono potenziate del 50%.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Charme, Cura ferite leggere |
| 2 | Ristorare inferiore, Rimuovi malattia (non attivo) |
| 3 | Cura ferite gravi |
| 4 | Reincarnazione (non attivo), Neutralizza veleno |
| 5 | Espiazione (non attivo), Spezzare incantesimo |
| 6 | Banchetto degli eroi (non attivo), Guarigione |

### Riposo

*Poteri concessi: il sonno e la morte ti obbediscono entrambi.*

- **1°**: Il tocco mortale può uccidere chi è quasi morto; il tocco gentile barcolla i vivi e può addormentarli.
- **8°**: La barriera sospende morte, risucchio e penalità dei livelli negativi senza cancellarli.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Nascondersi ai non morti (non attivo), Visione della morte (non attivo) |
| 2 | Riposo inviolato (non attivo) |
| 3 | Parlare con i morti (non attivo) |
| 4 | Interdizione alla morte |
| 5 | Distruggere viventi |
| 6 | Non morto a morto (non attivo) |

### Rune

*Poteri concessi: i segni antichi rispondono alla tua mano.*

- **1°**: Scrivi pergamene gratis; la runa-trappola [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Cancellare (non attivo) |
| 2 | Pagina segreta (non attivo) |
| 3 | Glifo di interdizione (non attivo) |
| 4 | Rune esplosive |
| 5 | Legame planare inferiore (non attivo) |
| 6 | Glifo di interdizione superiore (non attivo) |

### Sofferenza

*Poteri concessi: conosci il dolore e sai donarlo.*

- **1°**: Il tocco doloroso toglie 2 a Forza e Destrezza per metà livello in round (minimo 1) o per un minuto.
- **8°**: Il tormento rende infermo (TS Volontà nega).

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Anatema |
| 2 | Vigore |
| 3 | Scagliare maledizione (non attivo) |
| 4 | Debilitazione |
| 5 | Simbolo di dolore (non attivo) |
| 6 | Ferire |

### Sole

*Poteri concessi: l'alba sorge dove decidi tu.*

- **1°**: Una volta al giorno, con 1 uso di Incanalare, curi i vivi, ferisci i non morti con danni aumentati del tuo livello e li scacci con un TS separato, ignorando le loro resistenze.
- **8°**: Accendi il nimbo: ogni round ferisce i non morti vicini per danni pari al tuo livello.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Contrastare elementi |
| 2 | Riscaldare il metallo (non attivo) |
| 3 | Luce incandescente |
| 4 | Scudo di fuoco (non attivo) |
| 5 | Colpo infuocato |
| 6 | Semi di fuoco (non attivo) |

### Tempeste

*Poteri concessi: la tempesta ti segue come un vessillo.*

- **1°**: Resisti all'elettricità (5); la raffica infligge 1d6 più metà livello danni entro 6 caselle e toglie 2 a colpire e alle magie per un round.
- **6°**: L'aura di bufera ostacola avvicinamento e cariche dei nemici.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Scudo entropico (non attivo), Foschia occultante (non attivo) |
| 2 | Folata di vento, Nube di nebbia (non attivo) |
| 3 | Invocare il fulmine |
| 4 | Tempesta di nevischio (non attivo) |
| 5 | Tempesta di ghiaccio, Invocare Tempesta di Fulmini (non attivo) |
| 6 | Scirocco (non attivo) |

### Terra

*Poteri concessi: la pietra marcia al tuo fianco.*

- **1°**: Scaccia o comanda gli elementali della terra intorno a te (costa 1 uso di Incanalare); lancia un dardo acido a un bersaglio entro 6 caselle, che infligge 1d6 più metà livello danni.
- **6°**: Resistenza all'acido 10, sempre attiva.
- **12°**: Resistenza all'acido 20.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Pietra magica (non attivo) |
| 2 | Ammorbidire terra e pietra (non attivo) |
| 3 | Scolpire pietra (non attivo) |
| 4 | Rocce aguzze (non attivo) |
| 5 | Muro di pietra |
| 6 | Pelle di pietra |

### Tempo

*Poteri concessi: l'attimo giusto non ti sfugge mai.*

- Solo talenti automatici: Iniziativa Migliorata e Allerta. Nessun potere da attivare.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Colpo accurato (non attivo) |
| 2 | Riposo inviolato (non attivo), Aiuto |
| 3 | Velocità, Protezione dagli elementi |
| 4 | Libertà di movimento |
| 5 | Permanenza (non attivo), Spezzare incantesimo |
| 6 | Contingenza (non attivo), Fuorviare |

### Tirannia

*Poteri concessi: la tua parola è catena.*

- **1°**: Alzi di 2 la CD delle compulsioni; ordini ai PNG di fermarsi, avvicinarsi, fuggire, posare o cadere (sui PG [GDR]).
- **8°**: La presenza dà -2 ai nemici vicini nei TS contro paura e compulsioni.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Comando |
| 2 | Estasiare (non attivo) |
| 3 | Rivela bugie (non attivo) |
| 4 | Paura |
| 5 | Comando superiore |
| 6 | Costrizione/Cerca (non attivo) |

### Vegetale

*Poteri concessi: la foresta ti considera dei suoi.*

- **1°**: Natura di classe; intimorisci e comandi i vegetali con 1 uso di Incanalare; pugni di legno.
- **6°**: L'armatura di spine dura un round per uso, fino a livello usi al giorno.

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Intralciare |
| 2 | Pelle coriacea |
| 3 | Crescita vegetale (non attivo) |
| 4 | Comandare vegetali |
| 5 | Muro di spine |
| 6 | Respingere legno (non attivo) |

### Viaggio

*Poteri concessi: la strada si accorcia sotto i tuoi passi.*

- **1°**: Terre Selvagge di classe; cammini 3 metri più veloce; ti liberi da solo dagli impedimenti magici per un numero di round pari al livello al giorno; i piedi agili ignorano il terreno difficile per un round.
- **8°**: Balzo dimensionale [GDR].

| Circolo | Incantesimi concessi |
|---|---|
| 1 | Passo veloce (non attivo) |
| 2 | Localizza oggetto (non attivo) |
| 3 | Volare (non attivo) |
| 4 | Porta dimensionale |
| 5 | Teletrasporto (non attivo) |
| 6 | Scopri il percorso (non attivo) |

## Vedi anche

- [Chierico](/classi/chierico/): Scacciare, Incanalare, polarità e scuole vietate
- [Magia](/sistemi/magia/): preparazione, slot bonus e metamagie
- [Elenco dei comandi](/sistemi/elencocomandi/): sintassi di .poteredominio, .incanala, .scacciare
- [Domini su Golarion](https://golarion.altervista.org/wiki/Domini): i domini nel manuale Pathfinder di riferimento

