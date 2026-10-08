---
title: Elenco dei comandi
layout: sistemi
order: 3
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
- [Manovre](#manovre)
- [Compagni e seguaci](#compagni-e-seguaci)
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
- `.andatura`: Cambia andatura di movimento (camminata/corsa); `.velocitamonaco` resta come alias.
- `.arrostire`: Cuoce i cibi senza usare il libro delle ricette.
- `.assegnanome`: Permette di associare un nome a scelta ad un pg, per riconoscerlo poi col comando `.nomi`. Usando `.assegnanome cancella` si può pulire la lista dai nomi non più desiderati.
- `.azione [tipo]`: Permette di compiere azioni personali. Azioni possibili: attacco1, attacco2, attacco3, attacco4, attacco5, attacco6, attacco7, attacco8, cadiavanti, cadiindietro, castaarea, castadir, guardagiu, guardaintorno, inchinati, mangia, saluta.
- `.bestiario`: Apre il bestiario personale con le creature scoperte in gioco.
- `.borsaloot`: Definisce un contenitore in cui finiranno automaticamente tutti gli oggetti raccolti e creati.
- `.borsello`: Definisce un contenitore da usare come borsello per acquisti e vendite con i mercanti PNG.
- `.cambiapelle`: Permette customizzare colore di pelle e skin facciale del proprio personaggio.
- `.capacitarazziale <nome>`: Usa una capacità razziale (lucidanzanti, parlaconanimali, passosenzatracce; luce/lucediurna).
- `.cappuccio`: Alza/abbassa il cappuccio del mantello o della tunica indossati. Scrivendo il comando seguito da un qualsiasi carattere alfanumerico (es. `.cappuccio 5`) il cappuccio nasconderà l'identità del personaggio.
- `.cercare`: Il personaggio si mette a cercare trappole (é un loop, ripetendo il comando smette).
- `.cercarisorse`: Permette di capire che tipo di risorsa (legno o metallo ) sia presente nelle immediate vicinanze. Consuma puntilavoro.
- `.char`: Visualizza la scheda del personaggio.
- `.citta`: Usa la Pietra Cittadina. `.citta insegne`: mostra o nasconde titolo di carica e sigla.
- `.cmdbar`: Apre una barra comandi personale.
- `.cogli`: Permette di cogliere frutti dagli alberi o cercare radici e bacche commestibili (tramite check di Conoscenza Terre Selvagge) nella zona circostante (utilizzabile solo fuori città).
- `.colpononletale [on|off|auto]`: Converte la mischia in non letale, forza letali o segue l'arma.
- `.controincantesimo`: Tenta di controbattere un incantesimo in corso di lancio.
- `.controllati`: Permette di rilasciare creature domate, soggiogate o controllate a distanza.
- `.craftbook`: Apre il craftbook personale con ricette e progressi. `.elencomateriali`: elenca i materiali da lavoro nel contenitore indicato, con prelievo e deposito.
- `.cucina`: Cucina un piatto scegliendo strumenti e ingredienti. `.esamina`: esamina gli ingredienti (richiede Cuoco 5, mani libere).
- `.debugatk`: Restituisce i valori in attacco in tempo reale. Ripetere per disattivare.
- `.debugdef`: Restituisce i valori in difesa in tempo reale. Ripetere per disattivare.
- `.difesa`: Senza parametri attiva/disattiva il Combattimento difensivo. Con parametro "totale", attiva/disattiva la Difesa totale.
- `.disarma`: Prova a disarmare l'avversario al prossimo attacco in mischia.
- `.dove`: Fa una prova su geografia o sopravvivenza per comprendere l'area geografica dove ci si trova.
- `.elencopergamene`: Apre l'interfaccia con tutte le pergamene (arcane e divine) del contenitore indicato, divise per circolo e lanciabili da lì.
- `.elencospells [nomeclasse]`: Mostra l'elenco degli incantesimi, della propria classe o di quella indicata.
- `.emote [tipo]`: Permette di eseguire azioni sonore. Emote possibili: ah, ahha, applauso, bacio, fischio, gasp, grido, groan, hey, huh, no, oh, oooh, oops, peto, pianto, ringhio, risata, risatina, russa, rutto, sbadiglio, schiariscegola, shhht, sniff, soffianaso, sospiro, sputo, starnuto, tosse, tosse2, urlo, yahoo, yeah.
- `.firma`: Attiva/disattiva la propria firma sugli oggetti creati.
- `.fodero [cinta/schiena/secondario]`: Ripone l'arma impugnata nel fodero indicato.
- `.gettaarma`: Getta immediatamente a terra l'arma impugnata.
- `.gira`: Ruota l'oggetto di arredamento indicato.
- `.grab`: Raccoglie da terra gli oggetti a portata di mano, perquisendo anche eventuali cadaveri.
- `.grazia`: Attiva/disattiva la modalità di combattimento che non somma il modificatore di forza ai danni (utile per allenamenti o per non uccidere l’avversario).
- `.guardacielo`: Guarda il cielo e stima condizioni metereologiche, momento della giornata e stagione in corso.
- `.guardie`: Chiama le guardie magiche della città (solo in città).
- `.indica`: Indica un bersaglio (utile per mostrare dove sta una trappola, un oggetto o una persona).
- `.inginocchiati`: Il personaggio si inginocchia.
- `.insegne`: Attiva/disattiva la visualizzazione delle insegne e titoli di gilda.
- `.lingue`: Comando veloce per selezionare la lingua in cui parlare.
- `.lucerazziale [testo]`: Variante per la luce razziale.
- `.mapticket`: Comando per segnalare bug di mappa, vi fará puntare la posizione e descrivere il problema, senza teletrasportarvi via (vedi SOS)
- `.memloc`: Permette di memorizzare una location su cui potersi teletrasportare in seguito tramite relativa spell.
- `.memloc cancella`: Permette di cancellare una location precedentemente memorizzata.
- `.metamagia [nome|tutto|reset|intensificati N]`: Arma le metamagie possedute (dai talenti) per i lanci successivi.
- `.motd`: Visualizza il "Message of the Day" attuale.
- `.msg`: Usa la messaggistica interna per comunicare in off con altri giocatori. Si può disattivare con `.msg off` e riattivare con `.msg on`.
- `.msgt`: Permette di inviare un messaggio privato a un personaggio in vista del proprio pg.
- `.nonletali [mostra|nascondi]`: Mostra o nasconde i danni non letali.
- `.osservacreatura`: Permette di osservare, se presente, il profilo o descrizione aggiuntiva del personaggio o creatura indicata, funziona anche sui cadaveri dei mob configurati.
- `.party`: Apre il gump di gestione del party.
- `.passalivello`: Una volta raggiunti i PX necessari, permette di passare al livello seguente.
- `.password`: Permette di cambiare la password del proprio account di gioco.
- `.pet [testo]`: Fa parlare una creatura controllata.
- `.pgreset`: Resetta il personaggio dopo gli aggiornamenti (con autorizzazione).
- `.pgstart`: Avvia la creazione del personaggio (nome, razza, classe, caratteristiche, talenti, abilità).
- `.posa*`: Pose del personaggio (posaferma, posainginocchiati, posaprega, posaprostrati, posasdraiati, posasvieni, posaguardaaterra/destra/giu/sinistra, posaallargalebraccia).
- `.poteremagico [indumento/oggetto]`: Attiva i poteri di un oggetto magico, bacchetta o pergamena già decifrata.
- `.preparaspells`: Prepara gli incantesimi memorizzati per il lancio.
- `.prostrati`: Il personaggio si prostra.
- `.provadestrezza`: Sfida un altro personaggio ad una prova di Destrezza.
- `.provaforza`: Sfida un altro personaggio ad una prova di Forza o permette di sfondare porte/contenitori tramite check di forza e costituzione.
- `.provaintelligenza`: Sfida un altro personaggio ad una prova di Intelligenza.
- `.provatiro [abilita/ts/statistica]`: Prova generica col sistema comune (aiuti, ritentativi e Riesame allineati).
- `.provatiro [abilitá/ts/statistica]`: Lascia partire un tiro di dado che restituisce un risultato basato sulla statistica o abilitá scelta. Senza scrivere altro rende un menú
- `.puntilavoro`: Visualizza in percentuale quanti punti lavoro sono rimasti al pg.
- `.reply [testo]`: Risponde tramite messaggistica all’ultimo giocatore da cui si è ricevuto un messaggio.
- `.replyt [testo]`: Risponde all’ultimo giocatore da cui si è ricevuto un `.msgt`.
- `.riposa`: Permette un breve riposo che recupera punti ferita ma non permette di preparare nuovi incantesimi.
- `.roll [dadi]`: Tira i dadi e mostra il risultato sopra il personaggio (es. `.roll 2d8+12`).
- `.salta`: Salto atletico.
- `.saltodombra`: Salto d'ombra.
- `.sbilanciare`: Permette di sbilanciare l'avversario a mani nude o con le armi adatte.
- `.scheda`: Visualizza la scheda del personaggio (alternativa a `.char`).
- `.schedaabilita`: Mostra la scheda delle abilità con ritratto, consapevole di classi e domini.
- `.scorpione` e `.gorgone`: Stili di manovra dello scorpione e della gorgone.
- `.sdraiati`: Il personaggio si sdraia.
- `.sos`: Teletrasporta il pg al Gate e lascia la locazione del teletrasporto. Serve se siete bloccati, e segnala la locazione buggata a noi. Usato come teletrasporto libero viene punito.
- `.spaccarearma`:  Prova a spaccare l’arma dell’avversario al prossimo attacco in mischia.
- `.spinta`: Permette di spingere violentemente un’altra creatura (con adeguata prova di forza).
- `.suicidio`: Permette di togliersi la vita con un’arma o lasciarsi morire al prossimo attacco che dovrebbe far svenire il pg.
- `.svuota`: Svuota un contenitore dentro un altro o a terra, oppure svuota a terra il contenuto di una pozione.
- `.talenti`: Restituisce la lista dei talenti completa, con le descrizioni per scegliere con calma.
- `.townhouses`: Elenca le proprietà in vendita (registro, senza teletrasporto).
- `.trascina`: Permette di trascinare corpi o oggetti molto pesanti (consuma molta stamina).
- `.versatile`: Gestisce l'impugnatura a 1 o 2 mani delle armi che lo supportano.
- `.visibile`: Interrompe eventuali incantesimi di Invisibilità su se stessi.

---

## Comandi per Talenti

- `.afferrarefrecce [impugna|conserva|rilancia]`: Gestisce frecce afferrate al volo.
- `.aggiornatalenti`: Completa scelte di talenti lasciate a metà.
- `.attaccopoderoso`: Scegli un valore tra 0 e il valore di Txc base; questo valore viene sottratto al tiro per colpire e aggiunto ai danni (richiede talento Attacco Poderoso).
- `.attaccoturbinante`: Esegue come azione di round completo un singolo attacco in mischia che colpisce tutti gli avversari attorno (richiede talento Attacco Turbinante).
- `.calciorotante`: Come attacco turbinante, ma solo a mani nude (richiede talento Calcio Rotante).
- `.colpotremendo`: Colpo tremendo.
- `.completatalento [id]`: Completa scelte di talenti rimaste in sospeso (es. 37 Cosmopolita, 246 Grande esperienza), senza consumare nuovi talenti.
- `.cosmopolita`: Talento Cosmopolita (usa `.completatalento 37`).
- `.esplosionearcana [nome|livello]`: Sacrifica un incantesimo per un'esplosione (arcano 10).
- `.furtivoattento`: Passo furtivo lento da nascosto (non correre).
- `.incalzare [attiva|disattiva]`: Catena di mischia sui nemici adiacenti (-2 CA).
- `.maestria`: Scegli un valore tra 0 e 5; questo valore viene sottratto al tiro per colpire e aggiunto alla classe armatura (richiede talento Maestria).
- `.maestriaintimorente`: Gestione di Maestria Intimorente.
- `.scagliaarma`: Scaglia l'arma impugnata.
- `.seguiretracce`: Cerca impronte di altre creature nelle vicinanze tramite check su Sopravvivenza (richiede talento Seguire Tracce).
- `.tirorapido`: Attiva/disattiva la modalità di combattimento che permette di lanciare una freccia aggiuntiva col bonus TxC massimo, ma ogni attacco ha -2 penalità al TxC.

---

## Comandi per Classe

### Barbaro

- `.irabarbarica`: Entra in ira (+4 FOR/COS, +2 Volontà, −2 CA; consuma la riserva round).
- Poteri con comando: `.abbandonoavventato`, `.posizionedifensiva`, `.balzodifensivo`, `.accuratezzasorprendente`, `.attaccodevastante`, `.colpopossente`, `.ispirareferocia`, `.scagliaarma`, `.ostentareprovocazione`, `.sguardointimidatorio`, `.vieniaprendermi`, `.vigorerinnovato`, `.iraelementaleinferiore`.
- `.poteriira`: Sceglie i poteri d'ira (fuori ira, dal 2°). `.mieipoteriira`: li elenca.
- `.velocitabarbaro`: Attiva/disattiva la corsa in ira.

### Bardo

- `.canzonebardo`: Esegue canzoni con effetti magici tramite strumento o voce.
- `.casta [nome o numero]` e `.castabardo`: Lanciano incantesimi (numero tra parentesi, es. `.casta 8`). `.casta difensivo`: in modalità difensiva.
- `.memo`: Visualizza le memorizzazioni disponibili. `.metamagia`: arma le metamagie possedute.
- `.oratore`: Alterna la performance oratoria a quella musicale.
- `.spells` e `.spellsbardo`: Elenco incantesimi conosciuti, da lanciare.
- `.suona [nota]`: Suona una nota con uno strumento musicale scelto. Note valide: DO, DO#, RE, RE#, MI, FA, FA#, SOL, SOL#, LA, LA#, SI (o A, As, B, C, Cs, D, Ds, E, F, Fs, G, Gs).

### Chierico

- `.armadanzante`, `.ragnatela`, `.unitafamiglia`: Comandi dedicati ai domini Artigianato, Ragni e Famiglia.
- `.castachierico` (o `.casta [nome o numero]`): Lancia un incantesimo. `.casta difensivo`: in modalità difensiva.
- `.converti`: Muta un incantesimo preparato in cura o ferita (stessa polarità permanente di `.incanala`).
- `.incanala cura/danneggia [rapido]` · `.incanala punizione` · `.incanala rimanenti`: Riversa energia divina sull'area (danni/cure (livello+1)/2 d6, raggio 6 caselle).
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute.
- `.poteredominio <dominio> [potere]` (es. `.poteredominio acqua`): Attiva i poteri di dominio (menu se ometti il potere). Dettagli nella [guida](/sistemi/domini/).
- `.qualsiasiincantesimo [id]` comando per gestire Qualsiasi Incantesimo per il dominio incantesimi
- `.qualsiasiincantesimosuperiore [id]` comando per gestire Qualsiasi Incantesimo Superiore per il dominio incantesimi
- `.scacciare` e `.scacciare rimanenti`: Usa il simbolo sacro impugnato contro i non-morti (TS Volontà, raggio 6 caselle; 1 uso di Incanalare). I vecchi `rapido / potenziato / numero` non si applicano più.

### Druido

- `.castadruido` (o `.casta [nome o numero]`): Lancia incantesimi. `.casta difensivo`: in modalità difensiva.
- `.compagnoanimale` e `.compagnoanimaledruido`: Aprono il menu unificato di scelta del compagno. `.compagni`: lo richiama e apre il pannello. Dettagli nella [guida](/sistemi/compagni/).
- `.formaselvaggia [animale]`: Cambia in forma animale. Può essere numero o nome animale. Senza parametro mostra il gump di scelta.
- `.formaselvaggia rimanenti`: Mostra cariche rimanenti di forma selvaggia.
- `.formaumana`: Torna alla forma umana, interrompendo metamorfosi.
- `.linguaselvaggia [stato]`: Parla con gli animali della propria forma (druido 6, forma selvatica).
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute.
- `.traslazione`: Se sotto effetto di Traslazione arborea, permette di entrare in un albero.

### Guerriero

- Manovre da mischia (dal talento corrispondente): `.attaccopoderoso`, `.incalzare`, `.disarma`, `.sbilanciare`, `.spaccarearma`.
- `.riaddestraguerriero`: Sostituisce un talento bonus da combattimento con un altro (mai i prerequisiti di altri).

### Ladro

- Dalle doti: `.subdolo`, `.settafurtivo`, `.alleatoinvolontario`, `.bersagliatorefurtivo`, `.maestrotravestimento`, `.ridirezionare`, `.riesame`, `.schivataestrema`, `.sorpresacacciatore`, `.disarma`, `.falsoamico`, `.rialzati`.
- `.dotaladro dita` e `.dotaladro manovra`: Attivano Dita Rapide e Manovra Senza Pari (usi 1 + livello/5 al giorno).
- `.dotiladro`: Mostra le doti possedute. Le scelte arrivano da sole al `.passalivello` nei livelli pari.

### Mago

- `.castamago` (o `.casta [nome o numero]`): Lancia incantesimi. `.casta difensivo`: in modalità difensiva.
- `.compagni`: gestisce il famiglio (condividi, tocca, legame, interroga).
- `.duellomagico [dimensione]`: Inizia Duello Magico con altro incantatore arcano.
- `.evocafamiglio`: richiama il famiglio al proprio fianco.
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione dal Libro. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute. `.controincantesimo`: tenta di controbattere un lancio in corso.
- `.portafamiglio`: mette al sicuro il famiglio.
- `.poterescuola` e `.poterescuola [potere]`: Scelta della scuola e poteri (menu con utilizzi). Dettagli nella [guida](/sistemi/scuole/).
- `.recuperafamiglio`: recupera il famiglio al sicuro.
- `.sceglifamiglio`: sceglie il famiglio tra le specie con rituale di 8 ore.
- `.ven [testo]`: Usa Ventriloquio per far apparire la voce come proveniente dal soggetto dell’incantesimo.
- `.visibile`: Toglie l'invisibilità a se stessi. `.fermaritirata`: blocca la Ritirata Rapida.

### Monaco

- `.attaccostordente`: Arma il Pugno Stordente per il prossimo attacco senz'armi (1 al giorno per livello, CD 10 + metà livello + SAG).
- `.integrita`: Guarisce 2 × livello PF al giorno.
- `.ki [potere]`: Poteri del Ki del monaco.
- `.lancioki`: Sbilanciare col Ki.
- `.palmovibrante`: Carica il prossimo attacco per uccidere (15°, 1 a settimana). `.cancellapalmo`: cambia vittima designata.
- `.passoabbondante`: Passo Abbondante del monaco.
- `.raffica`: Attiva/disattiva la raffica di colpi. `.velocitamonaco`: Attiva/disattiva la camminata veloce.

### Paladino

- `.castapaladino` (o `.casta [nome o numero]`): Lancia incantesimi dal 4°. `.casta difensivo`: in modalità difensiva.
- `.crociata`: Condivide il punire con gli alleati entro 3 m per 1 minuto (11°, costa 2 usi).
- `.distruggimale`: Concentra Punire il Male sul bersaglio (1 + (liv−1)/3 usi al giorno).
- `.imposizione [numero]`: Usa Imposizione delle Mani per guarire (livello/2 + CAR usi; `rimasti` per contarli).
- `.incanala`: Riversa energia divina sull'area (costa 2 imposizioni).
- `.indivmale`: Individua il male attorno a sé (da riusare dopo il riposo).
- `.indulgenze`: Sceglie e consulta le indulgenze (livello/3).
- Legame divino (5°, scelta esclusiva): `.cavalcatura` per chiamarla, `.cavalcaturaspeciale` per sceglierla, `.evocacavalcaturaspeciale` per evocarla, `.legamedivino` per gestirlo, `.legamearma` per potenziare l'arma.
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.metamagia`: Arma le metamagie possedute.
- `.rimuovimalattia`: Purga un malato (cariche settimanali; `rimasti` per contarle).
- `.scacciare`: Usa simbolo sacro per scacciare non-morti (come chierico di 2 livelli sotto).

### Ranger

- `.castaranger` (o `.casta [nome o numero]`): Lancia incantesimi dal 4°. `.casta difensivo`: in modalità difensiva.
- `.compagni`: apre il menu unificato di scelta e il pannello del compagno (dal 4°, con Legame del Cacciatore). Dettagli nella [guida](/sistemi/compagni/).
- `.memo` e `.preparaspells`: Gestiscono memorizzazione e preparazione. `.spells`: elenco incantesimi.
- `.preda`: Designa una preda viva a vista tra i Nemici Prescelti (11°). `.preda stato`: controlla quella attiva. `.preda abbandona`: rinuncia (24 ore di attesa).

### Stregone

- `.castastregone` (o `.casta [nome o numero]`): Lancia incantesimi spontanei. `.casta difensivo`: in modalità difensiva.
- `.duellomagico [dimensione]`: Inizia Duello Magico con altro incantatore arcano.
- Famiglio: `.poterestirpe famiglio` per gestirlo, `.compagni` per richiamarlo.
- `.metamagia`: Arma le metamagie possedute.
- `.poterestirpe` e `.poterestirpe [potere]`: Scelta iniziale della stirpe e poteri (menu con cariche). Dettagli nella [guida](/sistemi/stirpi/).
- `.spells`: Elenco incantesimi conosciuti, da lanciare.
- `.ven [testo]`: Ventriloquio.

## Manovre

Le manovre si usano dalla finestra `.manovre` o col comando dedicato; molte sostituiscono un attacco.

- `.acrobazia [veloce]`: acrobazia in movimento.
- `.alzati`: rialzarsi da prono, con tentativo di rialzo automatico.
- `.attaccorapido`: attacco rapido (completa).
- `.bottasbilanciante`: botta sbilanciante (richiede Attacco Poderoso).
- `.caricare [opzioni]`: carica con raccordo al movimento (prossimo, annulla, impetuosa, radiosa, passaggio, sbilanciare, disarmare, spezzare, spingere, oltrepassare).
- `.colpobasso`: colpo basso (completa).
- `.fintare [duearmi|distanza|gemella]`: fintare (Standard; movimento con Fintare Migliorato).
- `.giravoltasbilanciante`: giravolta sbilanciante (completa, bastone ferrato a due mani).
- `.lotta [azione]`: presa e gestione della lotta (mantieni, danno, nonletale, immobilizza, muovi, libera, fuga, inverti, rilascia, lega, aiuta, sciogli).
- `.oltrepassare`: oltrepassare un avversario (Standard + movimento).
- `.rimuovitrucco <effetto>`: rimuove un trucco tra accecato, abbagliato, assordato, intralciato, scosso e infermo (movimento).
- `.riposizionare`: riposizionare un avversario (Standard).
- `.rubare`: rubare un oggetto (Standard).
- `.spezzare [oggetto]`: spezzare arma o oggetto indossato (sostituisce un attacco).
- `.spinta`: spingere un avversario (Standard).
- `.sporcotrucco <effetto>`: sporco trucco tra accecato, abbagliato, assordato, intralciato, scosso e infermo (Standard).
- `.talentomanovra`: talento di manovra.
- `.tiroinmovimento`: tiro in movimento (completa).
- `.trascinare`: trascinare un avversario (Standard + movimento).

## Compagni e seguaci

- `.compagnoombra`: gestione del compagno ombra.
- `.designaanimale`: designare un animale.
- `.evocafamiglio`: richiama il famiglio al proprio fianco.
- `.gesto`: far compiere gesti alle creature.
- `.legamecacciatore`: condividere il Nemico Prescelto col gruppo.
- `.ordina`: impartire ordini ai seguaci.
- `.portafamiglio`: mette al sicuro il famiglio.
- `.recuperafamiglio`: recupera il famiglio al sicuro.
- `.sceglifamiglio`: sceglie il famiglio tra le specie.
- `.sceglilegame`: scelta permanente compagno contro bonus di gruppo (ranger 4+).
- `.servitoreimmondo`: gestione del servitore immondo.

