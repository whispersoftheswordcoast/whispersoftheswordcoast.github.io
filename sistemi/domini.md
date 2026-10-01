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

Molti poteri ostili chiedono un **attacco di contatto**, mentre altri aprono un cursore di bersaglio fino a 6 caselle. I poteri narrativi come parlare con gli animali, scrutare da lontano o saltare tra i piani si risolvono nel racconto col master.

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

## I domini uno per uno

Come nel manuale di Golarion, ogni voce indica i poteri concessi e a che livello si sbloccano. Gli incantesimi concessi sono nella sezione più sotto.

### Acqua
Scaccia e comanda gli elementali dell'acqua spendendo 1 uso di Incanalare e colpisce col dardo di freddo entro 6 caselle. Dal 6° resiste al freddo (10, poi 20 al 12°).

### Animale
Rende Natura una conoscenza di classe e fa parlare con gli animali nel racconto. Dal 4° affida un compagno animale con livello effettivo pari al tuo meno 3, condiviso col dominio dei Rettili.

### Aria
Scaccia e comanda gli elementali dell'aria spendendo 1 uso di Incanalare e colpisce col dardo elettrico entro 6 caselle. Dal 6° resiste all'elettricità (10, poi 20 al 12°).

### Artigianato
Aumenta di 1 il livello per creare oggetti e assegna Abilità Focalizzata in un Artigianato a scelta. Ripara 1d4 danni agli oggetti con un rituale di dieci minuti e tocca oggetti e costrutti. Dall'8° dona all'arma quattro round da danzante, poi va liberata e ripresa con le azioni apposite (`.armadanzante`).

### Bene
Aumenta di 1 il livello degli incantesimi del bene e tocca gli alleati col tocco del bene. Dall'8° rende sacra l'arma impugnata.

### Caos
Aumenta di 1 il livello degli incantesimi del caos. Dall'8° rende anarchica l'arma impugnata. Non ha altri poteri da attivare prima dell'8°.

### Castigo
Dopo una ferita, una volta al giorno arma la vendetta: il prossimo attacco contro chi ti ha colpito, se va a segno, è massimizzato. Qualsiasi altra azione prima dell'attacco la spezza. Dall'8° puoi armare anche la risposta immediata.

### Caverne
Rende esperto minatore e lancia un dardo acido. Dall'8°, nelle zone sotterranee, concede scurovisione e bonus a Furtività e iniziativa. L'arrampicata resta narrativa.

### Charme
Una volta al giorno alza il Carisma di 4 per un minuto e frastorna col tocco. Dall'8° il charme rapido convince un PNG a non aggredirti (sui PG resta racconto).

### Commercio
Aumenta la velocità di 3 metri e addolcisce con la lingua d'argento la prossima prova sociale. Lettura dei pensieri e balzo dimensionale dall'8° sono solo narrativi.

### Conoscenza
Rende le Conoscenze abilità di classe, aumenta di 1 il livello delle divinazioni e consulta il bestiario col tocco. Dal 6° la visione remota è solo narrativa.

### Distruzione
Punisce in due modi: in breve ai danni fisici e in forte alla fede una volta al giorno. Dall'8° apre un'aura che fa male a tutti intorno, amici compresi.

### Drow
Assegna gratis Riflessi Fulminei. Non ha poteri da attivare.

### Elfi
Assegna gratis Tiro Ravvicinato. Non ha poteri da attivare.

### Equilibrio
Una volta al giorno aggiunge Saggezza alla CA per un numero di round pari al livello. Assegna Riflessi Fulminei e dall'8° anche Saldo e agile.

### Famiglia
Protegge con +2 schivare e trasferisce a tocco una condizione da un alleato a te, conservandone la scadenza, per un totale di 3 più Saggezza round al giorno. Dall'8° arma l'Unità con `.unitafamiglia`: il gruppo condivide un effetto se tutti acconsentono, un uso per effetto e due dal 12°.

### Fanghiglie
Comanda le melme spendendo 1 uso di Incanalare, entro un limite di DV separato. Dardo acido e resistenza all'acido come Terra.

### Fato
Assegna gratis Fortuna degli Eroi. Non ha poteri da attivare.

### Fortuna
Assegna gratis Fortuna degli Eroi. Non ha poteri da attivare.

### Forza
Una volta al giorno l'Impresa aggiunge tutto il livello alla Forza per un round; il tocco dà un impulso breve. Dall'8° la Forza degli Dei aiuta prove e abilità, non attacchi e danni. Riserve condivise con gli Orchi.

### Freddo
Scaccia il fuoco e comanda il freddo spendendo 1 uso di Incanalare, con dardo di freddo come Acqua. Dall'8° la forma glaciale rende immune al freddo e dà RD 5 per un numero di round pari al livello, ma raddoppia il fuoco subito.

### Fuoco
Scaccia e comanda gli elementali del fuoco spendendo 1 uso di Incanalare e colpisce col dardo di fuoco entro 6 caselle. Dal 6° resiste al fuoco (10, poi 20 al 12°).

### Gnomi
Aumenta di 1 il livello delle illusioni senza cumularlo con Illusioni. Condivide un solo doppio e il velo con Inganno e Illusioni: il velo cambia corpo, colore e nome, non gli abiti.

### Guarigione
Aumenta di 1 il livello delle cure e tocca i viventi svenuti sotto zero per rialzarli. Dal 6° le cure sono potenziate del 50%.

### Guerra
Assegna competenza e Arma Focalizzata nell'arma del culto, tocca di furia ai danni e dall'8° concede un talento di combattimento temporaneo scelto dal menu, per una riserva di round e con i prerequisiti rispettati.

### Halfling
Assegna Fortuna degli Eroi e una volta al giorno aggiunge Carisma a Scalare, Furtività e salti per dieci minuti.

### Illusioni
Aumenta di 1 il livello delle illusioni e alza un solo doppio illusorio. Dall'8° stende il velo sul gruppo. Doppio e riserve sono condivisi con Inganno e Gnomi.

### Incantesimi
Apre liste cumulative con Qualsiasi Incantesimo preparato tramite rituale. Dall'8° condivide il tocco dissolutore con Magia.

### Inganno
Rende le abilità del dominio abilità di classe e alza un solo doppio illusorio. Dall'8° stende il velo sul gruppo, condiviso con Illusioni e Gnomi.

### Legge
Aumenta di 1 il livello degli incantesimi della legge. Dall'8° rende assiomatica l'arma impugnata. Non ha altri poteri da attivare prima dell'8°.

### Luna
Assegna Combattere alla cieca, scaccia i licantropi spendendo 1 uso di Incanalare e tocca di oscurità come Oscurità. Dall'8° colpisce col fuoco lunare, che può abbagliare.

### Magia
Usa gli oggetti magici come un mago di livello dimezzato e colpisce a distanza con la mano dell'accolito, tirando con Saggezza. Dall'8° condivide il tocco dissolutore con Incantesimi.

### Male
Aumenta di 1 il livello degli incantesimi del male. Il tocco rende infermo e tratta il bersaglio come buono per gli effetti malvagi, senza cambiarne l'allineamento. Dall'8° rende sacrilega l'arma.

### Mentalismo
Rende le Conoscenze abilità di classe e consulta il bestiario col tocco. Una volta al giorno l'interdizione dà resistenza pari a livello più 2 al prossimo Volontà entro un'ora. Dal 6° la visione remota è solo narrativa.

### Metalli
Assegna competenza e Focalizzata in un martello a scelta e resiste all'acido. I pugni metallici partono con l'azione veloce e durano un round, con danno migliore, letali e capaci di ignorare durezza fino a 10.

### Morte
Tocca di morte come Riposo e sanguina col tocco sanguinante. Dall'8° trae cura dall'energia negativa.

### Nani
Assegna Tempra Possente e dall'8° la tenacia della pietra dà RD 3 per un round (5 al 12°).

### Nobiltà
Ispira il gruppo e risolleva il singolo con la parola, con solo il miglior bonus morale. Dall'8° l'autorità sui seguaci è narrativa.

### Non-Morte
Aggiunge quattro usi alla riserva di Incanalare e tocca per reagire alle energie come un non morto, senza cambiare tipo. Dall'8° l'energia negativa cura.

### Oceano
Resiste al freddo, respira sott'acqua nel racconto e spinge o trascina con l'ondata, tirando livello più Saggezza contro la difesa di manovra.

### Odio
Marchia un nemico per un minuto e dall'8° scatena contro di lui l'ostilità implacabile per un round.

### Orchi
Punisce con danni pari al livello e aggiunge 4 al tiro contro elfi e nani. Condivide tocco e Forza degli Dei con Forza.

### Oscurità
Assegna Combattere alla cieca e tocca di oscurità come Luna. Dall'8° gli occhi dell'oscurità vedono nelle tenebre per metà livello in round al giorno.

### Pianificazione
Applica gratis gli incantesimi prolungati e dall'8° assegna Allerta. Non ha altri poteri da attivare.

### Portali
Cerca i portali con CD 20. Il balzo dimensionale dall'8° è solo narrativo.

### Protezione
Resiste ai tiri salvezza, trasferisce la resistenza col tocco e interdice il prossimo TS. Dall'8° l'aura protettiva devia i colpi e ripara dagli elementi senza cumulare bonus omonimi.

### Ragni
Intimorisce e comanda spendendo 1 uso di Incanalare; i movimenti del ragno sono narrativi. Dall'8° stende la ragnatela con ancoraggi, TS Riflessi, fuga, terreno difficile, copertura e combustione, una volta al giorno e due dal 12°, gestita con `.ragnatela`.

### Rettili
Comanda i rettili spendendo 1 uso di Incanalare entro un limite di DV separato e avvelena con lo sguardo, tra resistenza agli incantesimi e Volontà. Dal 4° affida un serpente con livello effettivo pari al tuo meno 3, unico compagno condiviso con Animale.

### Rinnovamento
Recupera da solo una volta dal colpo mortale e tocca per rimuovere le condizioni previste. Dal 6° le cure sono potenziate del 50%.

### Riposo
Tocca di morte come Morte e addolcisce col tocco gentile. Dall'8° la barriera sospende morte, risucchio e penalità dei livelli negativi senza cancellarli.

### Rune
Assegna gratis Scrivere Pergamene. La runa-trappola è solo narrativa.

### Sofferenza
Tocca con dolore breve o da un minuto sulla riserva comune. Dall'8° tormenta rendendo infermo. Le penalità omonime non si duplicano.

### Sole
Una volta al giorno, con 1 uso di Incanalare, cura i viventi, ferisce i non morti e li scaccia con un TS separato, ignorando le loro resistenze. Dall'8° accende il nimbo di luce.

### Tempeste
Resiste all'elettricità (5) e colpisce con la raffica. Dal 6° l'aura di bufera ostacola avvicinamento e cariche dei nemici.

### Terra
Scaccia e comanda gli elementali della terra spendendo 1 uso di Incanalare e colpisce col dardo acido entro 6 caselle. Dal 6° resiste all'acido (10, poi 20 al 12°).

### Tempo
Assegna gratis Iniziativa Migliorata e Allerta. Non ha poteri da attivare.

### Tirannia
Alza di 2 la CD delle compulsioni e comanda ai PNG di fermarsi, avvicinarsi, fuggire, posare o cadere (sui PG resta racconto). Dall'8° la presenza opprime chi resiste a paura e compulsioni.

### Vegetale
Rende Natura una conoscenza di classe, intimorisce e comanda i vegetali spendendo 1 uso di Incanalare, indurisce i pugni di legno e dal 6° veste di spine per una riserva di round.

### Viaggio
Rende Terre Selvagge una conoscenza di classe e aumenta la velocità di 3 metri. Libera da solo dagli impedimenti magici per un numero di round pari al livello al giorno e coi piedi agili ignora il terreno difficile per un round. Il balzo dall'8° è solo narrativo.

## Gli incantesimi dei domini

Ogni livello di incantesimo dal 1° al 6° ti dà **un solo slot di dominio**. Dentro ci metti solo gli incantesimi concessi dai tuoi due domini, presi da **liste cumulative**: se i due domini offrono lo stesso incantesimo, non lo prepari due volte.

Li prepari con `.preparaspells` come gli altri e li controlli con `.memo`. I domini Incantesimi e Magia hanno in più il *Qualsiasi Incantesimo*, che si prepara con un piccolo rituale e si gestisce con `.qualsiasiincantesimo`. Gli incantesimi mai implementati restano segnati e non partono.

## I culti

Non ci sono dèi nuovi: ogni dio concede domini fissi. Il **Caos** compare in undici culti: Corellon, Cyric, Lolth, Malar, Selune, Shaundakul, Sune, Talos, Tempus, Tymora e Umberlee. Oghma e Waukeen accolgono l'**Equilibrio**, Kelemvor lascia la Morte per il **Riposo**, Torm perde l'Animale e resta su Bene, Forza, Guarigione, Legge e Protezione, Bahamut corregge il nome in **Tempeste** e Beshaba perde la Distruzione.

Se il tuo personaggio aveva un dominio cambiato, resta come prima finché lo staff non lo aggiorna con te.

## Errori tipici

- Cercare il terzo dominio: sono sempre due, non si sbloccano altri salendo.
- Pensare che il velo cambi i vestiti: cambia corpo e nome, gli abiti restano i tuoi.
- Sommare due bonus morali: vale solo il migliore, l'altro è sprecato.
- Chiedere al potere narrativo di fare danni: dialogo, visioni e balzi raccontano, non tirano dadi.
- Dimenticare il riposo: senza letto e senza nemici intorno, le riserve non tornano.

## Vedi anche

- [Chierico](/classi/chierico/): Scacciare, Incanalare, polarità e scuole vietate
- [Magia](/sistemi/magia/): preparazione, slot bonus e metamagie
- [Elenco dei comandi](/sistemi/elencocomandi/): sintassi di `.poteredominio`, `.incanala`, `.scacciare`
