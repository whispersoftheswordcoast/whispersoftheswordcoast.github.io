---
title: Elenco dei comandi
layout: sistemi
order: 5
---
<img src="{{ '/assets/images/library.png' | relative_url }}" alt="riposo" style="display: block; margin: 0 auto;" />
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
- `.assegnanome`: Permette di associare un nome a scelta ad un pg, per riconoscerlo poi col comando `.nomi`. Usando `.assegnanome cancella` si può pulire la lista dai nomi non più desiderati.
- `.azione [tipo]`: Permette di compiere azioni personali. Azioni possibili: attacco1, attacco2, attacco3, attacco4, attacco5, attacco6, attacco7, attacco8, cadiavanti, cadiindietro, castaarea, castadir, guardagiu, guardaintorno, inchinati, mangia, saluta.
- `.borsaloot`: Definisce un contenitore in cui finiranno automaticamente tutti gli oggetti raccolti e creati.
- `.borsello`: Definisce un contenitore da usare come borsello per acquisti e vendite con i mercanti PNG.
- `.cappuccio`: Alza/abbassa il cappuccio del mantello o della tunica indossati. Scrivendo il comando seguito da un qualsiasi carattere alfanumerico (es. `.cappuccio 5`) il cappuccio nasconderà l'identità del personaggio.
- `.char`: Visualizza la scheda del personaggio.
- `.cogli`: Permette di cogliere frutti dagli alberi o cercare radici e bacche commestibili (tramite check di Conoscenza Terre Selvagge) nella zona circostante (utilizzabile solo fuori città).
- `.controllati`: Permette di rilasciare creature domate, soggiogate o controllate a distanza.
- `.difesa`: Senza parametri attiva/disattiva il Combattimento difensivo. Con parametro "totale", attiva/disattiva la Difesa totale.
- `.disarma`: Prova a disarmare l'avversario al prossimo attacco in mischia.
- `.lencospells [nomeclasse]`: Permette di avere una lista delle quest consultabili. Senza mettere un nome classe rende le spells della propria classe, altrimenti quelle della classe indicata.
- `.emote [tipo]`: Permette di eseguire azioni sonore. Emote possibili: ah, ahha, applauso, bacio, fischio, gasp, grido, groan, hey, huh, no, oh, oooh, oops, peto, pianto, ringhio, risata, risatina, russa, rutto, sbadiglio, schiariscegola, shhht, sniff, soffianaso, sospiro, sputo, starnuto, tosse, tosse2, urlo, yahoo, yeah.
- `.firma`: Attiva/disattiva la propria firma sugli oggetti creati.
- `.gettaarma`: Getta immediatamente a terra l'arma impugnata.
- `.grab`: Raccoglie da terra gli oggetti a portata di mano, perquisendo anche eventuali cadaveri.
- `.guardacielo`: Guarda il cielo e stima condizioni metereologiche, momento della giornata e stagione in corso.
- `.grazia`: Attiva/disattiva la modalità di combattimento che non somma il modificatore di forza ai danni (utile per allenamenti o per non uccidere l’avversario).
- `.indica`: Indica un bersaglio (utile per mostrare dove sta una trappola, un oggetto o una persona).
- `.insegne`: Attiva/disattiva la visualizzazione delle insegne e titoli di gilda.
- `.lingue`: Comando veloce per selezionare la lingua in cui parlare.
- `.memloc`: Permette di memorizzare una location su cui potersi teletrasportare in seguito tramite relativa spell.
- `.memloc cancella`: Permette di cancellare una location precedentemente memorizzata.
- `.motd`: Visualizza il "Message of the Day" attuale.
- `.msg`: Usa la messaggistica interna per comunicare in off con altri giocatori. Si può disattivare con `.msg off` e riattivare con `.msg on`.
- `.msgt`: Permette di inviare un messaggio privato a un personaggio in vista del proprio pg.
- `.party`: Apre il gump di gestione del party.
- `.passalivello`: Una volta raggiunti i PX necessari, permette di passare al livello seguente.
- `.password`: Permette di cambiare la password del proprio account di gioco.
- `.poteremagico [indumento/oggetto]`: Attiva i poteri di un oggetto magico, bacchetta o pergamena già decifrata.
- `.provadestrezza`: Sfida un altro personaggio ad una prova di Destrezza.
- `.provaforza`: Sfida un altro personaggio ad una prova di Forza o permette di sfondare porte/contenitori tramite check di forza e costituzione.
- `.provaintelligenza`: Sfida un altro personaggio ad una prova di Intelligenza.
- `.puntilavoro`: Visualizza in percentuale quanti punti lavoro sono rimasti al pg.
- `.reply [testo]`: Risponde tramite messaggistica all’ultimo giocatore da cui si è ricevuto un messaggio.
- `.replyt [testo]`: Risponde all’ultimo giocatore da cui si è ricevuto un `.msgt`.
- `.riposa`: Permette un breve riposo che recupera punti ferita ma non permette di preparare nuovi incantesimi.
- `.scheda`: Visualizza la scheda del personaggio (alternativa a `.char`).
- `.spaccarearma`: Prova a spaccare l’arma dell’avversario al prossimo attacco in mischia.
- `.spinta`: Permette di spingere violentemente un’altra creatura (con adeguata prova di forza).
- `.suicidio`: Permette di togliersi la vita con un’arma o lasciarsi morire al prossimo attacco che dovrebbe far svenire il pg.
- `.svuota`: Svuota un contenitore dentro un altro o a terra, oppure svuota a terra il contenuto di una pozione.
- `.talenti`: Restituisce la lista dei talenti completa, con le descrizioni per scegliere con calma.
- `.trascina`: Permette di trascinare corpi o oggetti molto pesanti (consuma molta stamina).
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

- `.irabarbarica`: Entra in ira barbarica.
- `.velocitabarbaro 1`: Aumenta la velocità a piedi in ira.

### Bardo

- `.canzonebardo`: Usa uno strumento musicale o la voce per eseguire canzoni con effetti magici. Permette di scegliere nuovi incantesimi arcani da imparare.
- `.casta [nome o numero]`: Lancia un incantesimo (numero indicato nella descrizione tra parentesi tonde, es. `.casta armatura magica` o `.casta 8`).
- `.casta difensivo`: Lancia incantesimi in modalità difensiva.
- `.memo`: Visualizza numero di memorizzazioni di incantesimi disponibili.
- `.spells`: Visualizza elenco incantesimi conosciuti e permette di lanciarli.  
- `.suona [nota]`: Suona una nota con uno strumento musicale scelto. Note valide: DO, DO#, RE, RE#, MI, FA, FA#, SOL, SOL#, LA, LA#, SI (o A, As, B, C, Cs, D, Ds, E, F, Fs, G, Gs).

### Chierico

- `.casta [nome o numero]`: Lancia un incantesimo (vedi sopra).
- `.casta difensivo`: Incantesimi in modalità difensiva.
- `.scacciare`: Usa simbolo sacro per scacciare/intimorire non-morti in zona.

  Uso: `.scacciare [rapido] [potenziato] [numero]`  
  - rapido: attiva Scacciare Rapido  
  - potenziato: attiva Scacciare Potenziato  
  - numero: indica i DV usati per Scacciare Intensificato

- `.spells`: Visualizza e lancia incantesimi memorizzati.
- `.poteredominio <dominio>` (es. `.poteredominio acqua`): Attiva i poteri di dominio.

### Druido

- `.casta [nome o numero]`: Lancia incantesimi.
- `.casta difensivo`: Incantesimi difensivi.
- `.formaselvaggia [animale]`: Cambia in forma animale. Può essere numero o nome animale. Senza parametro mostra il gump di scelta.
- `.formaselvaggia rimanenti`: Mostra cariche rimanenti di forma selvaggia.
- `.formaumana`: Torna alla forma umana, interrompendo metamorfosi.
- `.spells`: Elenco incantesimi memorizzati.
- `.traslazione`: Se sotto effetto di Traslazione arborea, permette di entrare in un albero.

### Guerriero

- Nessun comando specifico.

### Ladro

- Nessun comando specifico.

### Mago

- `.casta [nome o numero]`: Lancia incantesimi.
- `.casta difensivo`: Incantesimi difensivi.
- `.duellomagico [dimensione]`: Inizia un Duello Magico con altro incantatore arcano.
- `.spells`: Elenco incantesimi memorizzati.
- `.ven [testo]`: Usa Ventriloquio per far apparire la voce come proveniente dal soggetto dell’incantesimo.

### Monaco

- `.attaccostordente`: Attiva Attacco Stordente per il prossimo attacco in mischia.
- `.cancellapalmo`: Grazia la vittima designata da Palmo Vibrante.
- `.intregrità [numero]`: Usa Integrità del Corpo per guarire ferite.
- `.velocitamonaco 1/0`: Attiva/Disattiva camminata veloce.
- `.muoripalmo`: Tenta di uccidere la vittima designata da Palmo Vibrante.
- `.palmovibrante`: Attiva Palmo Vibrante per il prossimo attacco in mischia.

### Paladino

- `.casta [nome o numero]`: Lancia incantesimi.
- `.casta difensivo`: Incantesimi difensivi.
- `.cavalcaturaspeciale` e `.evocacavalcaturaspeciale`: Evoca la propria cavalcatura speciale.
- `.distruggimale`: Attiva Distruggere il Male per il prossimo attacco in mischia.
- `.imposizione [numero]`: Usa Imposizione delle Mani per guarire.
- `.indivmale`: Individua il male attorno a sé (solo su mostri).
- `.scacciare`: Usa simbolo sacro per scacciare non-morti (come per chierico).

### Ranger

- `.casta [nome o numero]`: Lancia incantesimi.
- `.casta difensivo`: Incantesimi difensivi.
- `.spells`: Elenco incantesimi.
- `.traslazione`: Permette di entrare in un albero sotto effetto Traslazione arborea.

### Stregone

- `.casta [nome o numero]`: Lancia incantesimi.
- `.casta difensivo`: Incantesimi difensivi.
- `.duellomagico [dimensione]`: Inizia Duello Magico con altro incantatore arcano.
- `.memo`: Visualizza memorizzazioni incantesimi disponibili.
- `.spells`: Elenco incantesimi conosciuti e possibilità di lanciarli.
- `.ven [testo]`: Ventriloquio.