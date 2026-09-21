---
title: Elenco dei comandi
layout: sistemi
order: 5
excerpt: Le parole di potere che aprono le porte alla fantasia
---
<img src="{{ '/assets/images/library.webp' | relative_url }}" alt="libreria fatata" style="display: block; margin: 0 auto;" />
<blockquote class="citazione">
  <p>"The words you speak can shape the world around you. Whether you wield magic through verbal incantations, rally your allies with inspiring speeches, or intimidate your foes with threats, language is a powerful tool in every adventurer’s arsenal."</p>
  <footer>— <cite>Player’s Handbook 5a</cite></footer>
</blockquote>

# Indice

I comandi si invocano con la sintassi .comando, e possono essere per facilitá sistemati con macro o pulsanti nella sezione "macro" delle opzioni del client con l'opzione "say" seguitra dal testo necessario.

- [Comandi Generici](#comandi-generici)
- [Comandi per Talenti](#comandi-per-talenti)
- [Comandi per Classe](#comandi-per-classe)
  - [Barbaro](#barbaro)
  - [Bardo](#bardo)
  - [Chierico](#chierico)
  - [Druido](#druido)
  - [Guerriero](#guerriero)
  - [Ladro](#ladro)
  - [Mago](#mago)
  - [Monaco](#monaco)
  - [Paladino](#paladino)
  - [Ranger](#ranger)
  - [Stregone](#stregone)
- [Note finali](#note-finali)

---

## Comandi Generici

- `.abilita [nomeabilita]`: Permette di utilizzare una determinata abilità (es. ".abilita ascoltare").
- `.aiuta <abilità> <CD>`: Dichiara aiuto a un altro personaggio nella prova indicata, con la CD finale (es. `.aiuta guarire 15`).
- `.assegnanome`: Permette di associare un nome a scelta ad un pg, per riconoscerlo poi col comando `.nomi`. Usando `.assegnanome cancella` si può pulire la lista dai nomi non più desiderati.
- `.azione [tipo]`: Permette di compiere azioni personali. Azioni possibili: attacco1, attacco2, attacco3, attacco4, attacco5, attacco6, attacco7, attacco8, cadiavanti, cadiindietro, castaarea, castadir, guardagiu, guardaintorno, inchinati, mangia, saluta.
- `.arrostire`: Cuoce i cibi senza usare il libro delle ricette.
- `.bestiario`: Apre il bestiario personale con le creature scoperte in gioco.
- `.borsaloot`: Definisce un contenitore in cui finiranno automaticamente tutti gli oggetti raccolti e creati.
- `.borsello`: Definisce un contenitore da usare come borsello per acquisti e vendite con i mercanti PNG.
- `.cambiapelle`: Permette customizzare colore di pelle e skin facciale del proprio personaggio.
- `.capacitarazziale <nome>`: Usa una capacità razziale (lucidanzanti, parlaconanimali, passosenzatracce; luce/lucediurna).
- `.lucerazziale [testo]`: Variante per la luce razziale.
- `.cercarisorse`: Permette di capire che tipo di risorsa (legno o metallo ) sia presente nelle immediate vicinanze. Consuma puntilavoro.
- `.cappuccio`: Alza/abbassa il cappuccio del mantello o della tunica indossati. Scrivendo il comando seguito da un qualsiasi carattere alfanumerico (es. `.cappuccio 5`) il cappuccio nasconderà l'identità del personaggio.
- `.cercare`: Il personaggio si mette a cercare trappole (é un loop, ripetendo il comando smette).
- `.char`: Visualizza la scheda del personaggio.
- `.citta`: Usa la Pietra Cittadina. `.citta insegne`: mostra o nasconde titolo di carica e sigla.
- `.cmdbar`: Apre una barra comandi personale.
- `.cogli`: Permette di cogliere frutti dagli alberi o cercare radici e bacche commestibili (tramite check di Conoscenza Terre Selvagge) nella zona circostante (utilizzabile solo fuori città).
- `.craftbook`: Apre il craftbook personale con ricette e progressi. `.elencomateriali`: elenca i materiali da lavoro nel contenitore indicato, con prelievo e deposito.
- `.cucina`: Cucina un piatto scegliendo strumenti e ingredienti. `.esamina`: esamina gli ingredienti (richiede Cuoco 5, mani libere).
- `.controllati`: Permette di rilasciare creature domate, soggiogate o controllate a distanza.
- `.controincantesimo`: Tenta di controbattere un incantesimo in corso di lancio.
- `.debugatk`: Restituisce i valori in attacco in tempo reale. Ripetere per disattivare.
- `.debugdef`: Restituisce i valori in difesa in tempo reale. Ripetere per disattivare.
- `.difesa`: Senza parametri attiva/disattiva il Combattimento difensivo. Con parametro "totale", attiva/disattiva la Difesa totale.
- `.disarma`: Prova a disarmare l'avversario al prossimo attacco in mischia.
- `.dove`: Fa una prova su geografia o sopravvivenza per comprendere l'area geografica dove ci si trova.
- `.elencospells [nomeclasse]`: Mostra l'elenco degli incantesimi, della propria classe o di quella indicata.
- `.elencopergamene`: Apre l'interfaccia con tutte le pergamene (arcane e divine) del contenitore indicato, divise per circolo e lanciabili da lì.
- `.emote [tipo]`: Permette di eseguire azioni sonore. Emote possibili: ah, ahha, applauso, bacio, fischio, gasp, grido, groan, hey, huh, no, oh, oooh, oops, peto, pianto, ringhio, risata, risatina, russa, rutto, sbadiglio, schiariscegola, shhht, sniff, soffianaso, sospiro, sputo, starnuto, tosse, tosse2, urlo, yahoo, yeah.
- `.firma`: Attiva/disattiva la propria firma sugli oggetti creati.
- `.fodero [cinta/schiena/secondario]`: Ripone l'arma impugnata nel fodero indicato.
- `.gettaarma`: Getta immediatamente a terra l'arma impugnata.
- `.gira`: Ruota l'oggetto di arredamento indicato.
- `.grab`: Raccoglie da terra gli oggetti a portata di mano, perquisendo anche eventuali cadaveri.
- `.guardacielo`: Guarda il cielo e stima condizioni metereologiche, momento della giornata e stagione in corso.
- `.guardie`: Chiama le guardie magiche della città (solo in città).
- `.grazia`: Attiva/disattiva la modalità di combattimento che non somma il modificatore di forza ai danni (utile per allenamenti o per non uccidere l’avversario).
- `.indica`: Indica un bersaglio (utile per mostrare dove sta una trappola, un oggetto o una persona).
- `.inginocchiati`: Il personaggio si inginocchia.
- `.insegne`: Attiva/disattiva la visualizzazione delle insegne e titoli di gilda.
- `.lingue`: Comando veloce per selezionare la lingua in cui parlare.
- `.mapticket`: Comando per segnalare bug di mappa, vi fará puntare la posizione e descrivere il problema, senza teletrasportarvi via (vedi SOS)
- `.memloc`: Permette di memorizzare una location su cui potersi teletrasportare in seguito tramite relativa spell.
- `.memloc cancella`: Permette di cancellare una location precedentemente memorizzata.
- `.metamagia [nome|tutto|reset|intensificati N]`: Arma le metamagie possedute (dai talenti) per i lanci successivi.
- `.motd`: Visualizza il "Message of the Day" attuale.
- `.msg`: Usa la messaggistica interna per comunicare in off con altri giocatori. Si può disattivare con `.msg off` e riattivare con `.msg on`.
- `.msgt`: Permette di inviare un messaggio privato a un personaggio in vista del proprio pg.
- `.osservacreatura`: Permette di osservare, se presente, il profilo o descrizione aggiuntiva del personaggio o creatura indicata, funziona anche sui cadaveri dei mob configurati.
- `.party`: Apre il gump di gestione del party.
- `.passalivello`: Una volta raggiunti i PX necessari, permette di passare al livello seguente.
- `.password`: Permette di cambiare la password del proprio account di gioco.
- `.pet [testo]`: Fa parlare una creatura controllata.
- `.pgstart`: Avvia la creazione del personaggio (nome, razza, classe, caratteristiche, talenti, abilità).
- `.pgreset`: Resetta il personaggio dopo gli aggiornamenti (con autorizzazione).
- `.posa*`: Pose del personaggio (posaferma, posainginocchiati, posaprega, posaprostrati, posasdraiati, posasvieni, posaguardaaterra/destra/giu/sinistra, posaallargalebraccia).
- `.poteremagico [indumento/oggetto]`: Attiva i poteri di un oggetto magico, bacchetta o pergamena già decifrata.
- `.preparaspells`: Prepara gli incantesimi memorizzati per il lancio.
- `.prostrati`: Il personaggio si prostra.
- `.provadestrezza`: Sfida un altro personaggio ad una prova di Destrezza.
- `.provaforza`: Sfida un altro personaggio ad una prova di Forza o permette di sfondare porte/contenitori tramite check di forza e costituzione.
- `.provaintelligenza`: Sfida un altro personaggio ad una prova di Intelligenza.
- `.provatiro [abilitá/ts/statistica]`: Lascia partire un tiro di dado che restituisce un risultato basato sulla statistica o abilitá scelta. Senza scrivere altro rende un menú
- `.puntilavoro`: Visualizza in percentuale quanti punti lavoro sono rimasti al pg.
- `.reply [testo]`: Risponde tramite messaggistica all’ultimo giocatore da cui si è ricevuto un messaggio.
- `.replyt [testo]`: Risponde all’ultimo giocatore da cui si è ricevuto un `.msgt`.
- `.riposa`: Permette un breve riposo che recupera punti ferita ma non permette di preparare nuovi incantesimi.
- `.roll [dadi]`: Tira i dadi e mostra il risultato sopra il personaggio (es. `.roll 2d8+12`).
- `.sbilanciare`: Permette di sbilanciare l'avversario a mani nude o con le armi adatte.
- `.scheda`: Visualizza la scheda del personaggio (alternativa a `.char`).
- `.sdraiati`: Il personaggio si sdraia.
- `.spaccarearma`:  Prova a spaccare l’arma dell’avversario al prossimo attacco in mischia.
- `.spinta`: Permette di spingere violentemente un’altra creatura (con adeguata prova di forza).
- `.sos`: Teletrasporta il pg al Gate e lascia la locazione del teletrasporto. Serve se siete bloccati, e segnala la locazione buggata a noi. Usato come teletrasporto libero viene punito.
- `.suicidio`: Permette di togliersi la vita con un’arma o lasciarsi morire al prossimo attacco che dovrebbe far svenire il pg.
- `.svuota`: Svuota un contenitore dentro un altro o a terra, oppure svuota a terra il contenuto di una pozione.
- `.talenti`: Restituisce la lista dei talenti completa, con le descrizioni per scegliere con calma.
- `.trascina`: Permette di trascinare corpi o oggetti molto pesanti (consuma molta stamina).
- `.townhouses`: Elenca le proprietà in vendita (registro, senza teletrasporto).
- `.visibile`: Interrompe eventuali incantesimi di Invisibilità su se stessi.

---

## Comandi per Talenti

- `.attaccopoderoso`: Scegli un valore tra 0 e il valore di Txc base; questo valore viene sottratto al tiro per colpire e aggiunto ai danni (richiede talento Attacco Poderoso).
- `.attaccoturbinante`: Esegue come azione di round completo un singolo attacco in mischia che colpisce tutti gli avversari attorno (richiede talento Attacco Turbinante).
- `.maestria`: Scegli un valore tra 0 e 5; questo valore viene sottratto al tiro per colpire e aggiunto alla classe armatura (richiede talento Maestria).
- `.calciorotante`: Come attacco turbinante, ma solo a mani nude (richiede talento Calcio Rotante).
- `.seguiretracce`: Cerca impronte di altre creature nelle vicinanze tramite check su Sopravvivenza (richiede talento Seguire Tracce).
- `.tirorapido`: Attiva/disattiva la modalità di combattimento che permette di lanciare una freccia aggiuntiva col bonus TxC massimo, ma ogni attacco ha -2 penalità al TxC.

---

## Comandi per Classe

### Barbaro

- `.irabarbarica`: Entra in ira (+4 FOR/COS, +2 Volontà, −2 CA; consuma la riserva round).
- `.velocitabarbaro`: Attiva/disattiva la corsa in ira.
- `.poteriira`: Sceglie i poteri d'ira (fuori ira, dal 2°). `.mieipoteriira`: li elenca.
- Poteri con comando: `.abbandonoavventato`, `.posizionedifensiva`, `.balzodifensivo`, `.accuratezzasorprendente`, `.attaccodevastante`, `.colpopossente`, `.ispirareferocia`, `.scagliaarma`, `.ostentareprovocazione`, `.sguardointimidatorio`, `.vieniaprendermi`, `.vigorerinnovato`, `.iraelementaleinferiore`.

### Bardo

- `.canzonebardo`: Esegue canzoni con effetti magici tramite strumento o voce.
- `.suona [nota]`: Suona una nota con uno strumento musicale scelto. Note valide: DO, DO#, RE, RE#, MI, FA, FA#, SOL, SOL#, LA, LA#, SI (o A, As, B, C, Cs, D, Ds, E, F, Fs, G, Gs).
- `.oratore`: Alterna la performance oratoria a quella musicale.
- `.casta [nome o numero]` e `.castabardo`: Lanciano incantesimi (numero tra parentesi, es. `.casta 8`). `.casta difensivo`: in modalità difensiva.
- `.spells` e `.spellsbardo`: Elenco incantesimi conosciuti, da lanciare.
- `.memo`: Visualizza le memorizzazioni disponibili. `.metamagia`: arma le metamagie possedute.

### Chierico

- `.castachierico` (o `.casta [nome o numero]`): Lancia un incantesimo. `.casta difensivo`: in modalità difensiva.
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute.
- `.scacciare`: Usa il simbolo sacro per scacciare/intimorire i non-morti in zona (3 + CAR usi al giorno, simbolo impugnato a mani libere).

  Uso: `.scacciare [rapido] [potenziato] [numero]`  
  - rapido: attiva Scacciare Rapido  
  - potenziato: attiva Scacciare Potenziato  
  - numero: indica i DV usati per Scacciare Intensificato

- `.converti`: Muta un incantesimo preparato in cura o ferita.
- `.poteredominio <dominio>` (es. `.poteredominio acqua`): Attiva i poteri di dominio.
- `.incanala`: Riversa energia divina sull'area (cura o ferisce secondo polarità).
- `.qualsiasiincantesimo [id]` comando per gestire Qualsiasi Incantesimo per il dominio incantesimi
- `.qualsiasiincantesimosuperiore [id]` comando per gestire Qualsiasi Incantesimo Superiore per il dominio incantesimi

### Druido

- `.castadruido` (o `.casta [nome o numero]`): Lancia incantesimi. `.casta difensivo`: in modalità difensiva.
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute.
- `.compagnoanimale` e `.compagnoanimaledruido`: Convincono un animale a diventare compagno. `.ricompagno`: lo richiama.
- `.formaselvaggia [animale]`: Cambia in forma animale. Può essere numero o nome animale. Senza parametro mostra il gump di scelta.
- `.formaselvaggia rimanenti`: Mostra cariche rimanenti di forma selvaggia.
- `.formaumana`: Torna alla forma umana, interrompendo metamorfosi.
- `.traslazione`: Se sotto effetto di Traslazione arborea, permette di entrare in un albero.

### Guerriero

- `.riaddestraguerriero`: Sostituisce un talento bonus da combattimento con un altro (mai i prerequisiti di altri).
- Manovre da mischia (dal talento corrispondente): `.attaccopoderoso`, `.incalzare`, `.disarma`, `.sbilanciare`, `.spaccarearma`.

### Ladro

- `.dotiladro`: Mostra le doti possedute. Le scelte arrivano da sole al `.passalivello` nei livelli pari.
- `.dotaladro dita` e `.dotaladro manovra`: Attivano Dita Rapide e Manovra Senza Pari (usi 1 + livello/5 al giorno).
- Dalle doti: `.subdolo`, `.settafurtivo`, `.alleatoinvolontario`, `.bersagliatorefurtivo`, `.maestrotravestimento`, `.ridirezionare`, `.riesame`, `.schivataestrema`, `.sorpresacacciatore`, `.disarma`, `.falsoamico`, `.rialzati`.

### Mago

- `.castamago` (o `.casta [nome o numero]`): Lancia incantesimi. `.casta difensivo`: in modalità difensiva.
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione dal Libro. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute. `.controincantesimo`: tenta di controbattere un lancio in corso.
- `.duellomagico [dimensione]`: Inizia un Duello Magico con altro incantatore arcano.
- `.ven [testo]`: Usa Ventriloquio per far apparire la voce come proveniente dal soggetto dell’incantesimo.
- `.visibile`: Toglie l'invisibilità a se stessi. `.fermaritirata`: blocca la Ritirata Rapida.
- Famiglio: `.famigliomago`, `.evocafamigliomago`, `.famigliomiglioratomago`, `.famigliononmortomago`.

### Monaco

- `.attaccostordente`: Arma il Pugno Stordente per il prossimo attacco senz'armi (1 al giorno per livello, CD 10 + metà livello + SAG).
- `.integrita`: Guarisce 2 × livello PF al giorno.
- `.raffica`: Attiva/disattiva la raffica di colpi. `.velocitamonaco`: Attiva/disattiva la camminata veloce.
- `.palmovibrante`: Carica il prossimo attacco per uccidere (15°, 1 a settimana). `.cancellapalmo`: cambia vittima designata.

### Paladino

- `.castapaladino` (o `.casta [nome o numero]`): Lancia incantesimi dal 4°. `.casta difensivo`: in modalità difensiva.
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute.
- `.distruggimale`: Concentra Punire il Male sul bersaglio (1 + (liv−1)/3 usi al giorno).
- `.imposizione [numero]`: Usa Imposizione delle Mani per guarire (livello/2 + CAR usi; `rimasti` per contarli).
- `.indivmale`: Individua il male attorno a sé (da riusare dopo il riposo).
- `.scacciare`: Usa simbolo sacro per scacciare non-morti (come chierico di 2 livelli sotto).
- `.incanala`: Riversa energia divina sull'area (costa 2 imposizioni).
- `.crociata`: Condivide il punire con gli alleati entro 3 m per 1 minuto (11°, costa 2 usi).
- `.indulgenze`: Sceglie e consulta le indulgenze (livello/3).
- `.rimuovimalattia`: Purga un malato (cariche settimanali; `rimasti` per contarle).
- Legame divino (5°, scelta esclusiva): `.cavalcatura` per chiamarla, `.cavalcaturaspeciale` per sceglierla, `.evocacavalcaturaspeciale` per evocarla, `.legamedivino` per gestirlo, `.legamearma` per potenziare l'arma.

### Ranger

- `.castaranger` (o `.casta [nome o numero]`): Lancia incantesimi dal 4°. `.casta difensivo`: in modalità difensiva.
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.compagnoanimaleranger`: Convinci un animale a diventare compagno (dal 4°). `.ricompagno`: lo richiama.
- `.preda`: Designa una preda viva a vista tra i Nemici Prescelti (11°). `.preda stato`: controlla quella attiva. `.preda abbandona`: rinuncia (24 ore di attesa).

### Stregone

- `.castastregone` (o `.casta [nome o numero]`): Lancia incantesimi spontanei. `.casta difensivo`: in modalità difensiva.
- `.spells`: Elenco incantesimi conosciuti, da lanciare.
- `.metamagia`: Arma le metamagie possedute.
- `.duellomagico [dimensione]`: Inizia Duello Magico con altro incantatore arcano.
- `.ven [testo]`: Ventriloquio.
- Famiglio: `.famigliostregone`, `.evocafamigliostregone`, `.famigliomiglioratostregone`, `.famigliononmortostregone`.