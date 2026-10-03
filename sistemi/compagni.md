---
title: Compagno animale
layout: sistemi
order: 24
excerpt: Come ottenere, far crescere e gestire il compagno animale di druidi e ranger
---

# Compagno animale

<img src="{{ '/assets/images/compagni0002.webp' | relative_url }}" alt="compagno animale" style="display: block; margin: 0 auto; max-width: 100%;" />

Un compagno animale non è solo un animale addomesticato: è un compagno di vita. Combatte al tuo fianco, cresce con te e condivide parte del tuo potere. Lo ottengono il **druido dal 1° livello** e il **ranger dal 4°**. Questa pagina ti accompagna in ogni fase: chi può averlo, come si sceglie e si richiama, come gli si danno ordini e come diventa più forte.

## Chi lo ottiene

- **Druido:** dal 1° livello, senza condizioni.
- **Ranger:** dal 4° livello, dopo aver scelto il Legame del Cacciatore (sotto).

## La scelta del ranger: Legame del Cacciatore

Al 4° livello da ranger si apre una scelta **permanente ed esclusiva**, da fare con `.sceglilegame` e confermare: non si potrà più cambiare. Le due strade sono:

- **Compagno animale:** una bestia scelta dal catalogo combatte al tuo fianco, sale di livello con te e condivide i tuoi Nemici Prescelti. Usa `.compagnoanimaleranger` per gestirlo.
- **Bonus condiviso:** nessun animale, ma il tuo bonus contro il Nemico Prescelto si estende al gruppo tramite `.legamecacciatore` contro un bersaglio, utile se giochi in squadra e non vuoi gestire una seconda creatura.

Chi aveva già un compagno prima di questa scelta viene migrato automaticamente sulla prima strada. Se hai scelto il bonus condiviso (e non sei druido), i comandi del compagno ti risponderanno che hai fatto l'altra scelta.

## Scegliere il compagno

Con `.compagni scegli animale` si apre il menu con **tutte le specie disponibili**: non esistono fasce di livello da sbloccare, e la potenza dipenderà solo dal livello effettivo (sotto). Scelta la specie, parte un **rituale di 24 ore del mondo**, al termine del quale si completa con `.compagni richiama animale`. Se provi prima, il gioco ti dice quante ore mancano.

I vecchi comandi specifici (`.compagnoanimale`, `.compagnoanimaledruido`, `.compagnoanimaleranger`) aprono lo stesso menu unificato.

### Le specie

Tra parentesi la crescita (il livello effettivo a cui la specie fiorisce), i dadi di danno e il movimento speciale, in piedi:

| Specie | Crescita | Danni | Movimento |
|---|---|---|---|
| Aquila | 4 | 1d4 1d4 1d4 | volo 80 |
| Falco | 4 | 1d4 1d4 1d4 | volo 80 |
| Gufo | 4 | 1d4 1d4 1d4 | volo 80 |
| Pipistrello crudele | 7 | 1d6 | volo 40 |
| Pteranodonte | 7 | 1d8 | volo 50 |
| Quetzalcoatlus | 9 | 1d8 | volo 50 |
| Roc | 7 | 1d4 1d4 1d6 | volo 80 |
| Coccodrillo | 4 | 1d6 | nuoto 30 |
| Delfino | 4 | 1d4 | nuoto 80 |
| Elasmosauro | 4 | 1d8 | nuoto 50 |
| Piovra (compagno) | 4 | 1d3 | nuoto 30 |
| Calamaro (compagno) | 4 | 1d4 1d3 | nuoto 60 |
| Squalo | 4 | 1d4 | nuoto 60 |
| Serpente Costrittore | 4 | 1d3 | nuoto 20, scalare 20 |
| Vipera piccola | 4 | 1d3 | nuoto 20, scalare 20 |
| Spinosauro | 7 | 1d6 1d4 1d4 | nuoto 20 |
| Tartaruga azzannatrice crudele | 7 | 1d6 | nuoto 20 |
| Tricheco | 7 | 1d6 | nuoto 40 |
| Varano | 7 | 1d6 | nuoto 30 |
| Topo crudele | 4 | 1d4 | nuoto 20, scalare 20 |
| Donnola Crudele | 4 | 1d4 | scalare 10 |
| Gorilla | 4 | 1d4 1d4 1d4 | scalare 30 |
| Megaterio | 7 | 1d4 1d4 | scalare 10 |
| Tasso | 4 | 1d4 1d3 1d3 | scalare 10, scavare 10 |
| Ghiottone | 4 | 1d4 1d3 1d3 | scalare 10, scavare 10 |
| Cane | 4 | 1d4 |  |
| Cane da galoppo | 4 | 1d4 |  |
| Cavallo | 4 | 1d4 1d6 1d6 |  |
| Pony | 4 | 1d3 1d3 |  |
| Cammello | 4 | 1d4 |  |
| Lama | 4 | 1d4 |  |
| Cervo | 4 | 1d4 |  |
| Iena | 4 | 1d4 |  |
| Lupo | 7 | 1d6 |  |
| Cinghiale | 4 | 1d6 |  |
| Bisonte | 7 | 1d6 |  |
| Rinoceronte | 7 | 1d8 |  |
| Elefante | 7 | 1d8 1d6 |  |
| Orso nero | 4 | 1d4 1d3 1d3 |  |
| Orso polare | 7 | 1d4 1d3 1d3 |  |
| Leone | 7 | 1d6 1d4 1d4 |  |
| Tigre | 7 | 1d6 1d4 1d4 |  |
| Pantera | 4 | 1d4 1d2 1d2 |  |
| Deinonico | 7 | 1d6 1d6 1d4 |  |
| Allosauro | 7 | 1d6 1d4 1d4 |  |
| Ceratosauro | 7 | 1d8 |  |
| Anchilosauro | 7 | 1d6 |  |
| Stegosauro | 7 | 2d6 |  |
| Tirannosauro | 7 | 1d8 |  |
| Triceratopo | 7 | 1d8 |  |

L'elenco nel menu di gioco fa fede: se una specie non compare, non è al momento disponibile.

<div class="wotsc-esempio" markdown="1">
Vuoi un lupo crudele? Lo scegli dal menu al primo livello utile: sarà il tuo livello effettivo a stabilirne la potenza, non la specie in sé. Pazienta le 24 ore del rituale e richiamalo.
</div>

Se cambi idea, con `sostituisci` rilasci quello vivo (recupera prima tutti i suoi oggetti) e ne parte uno nuovo, sempre col rituale di 24 ore.

## Richiamarlo al tuo fianco

Scelto il compagno, lo si richiama a sé con `.compagni` (vale anche `.ricompagno` come alias): raggiunge la tua posizione in circa un minuto, e l'eventuale compagno precedente viene distrutto. Tra una chiamata e l'altra passano **24 ore di cooldown**, sempre, anche se il compagno è morto nel frattempo. Se il comando avverte di un'attesa residua, mostra quante ore del mondo mancano.

<div class="wotsc-esempio" markdown="1">
Hai scelto il lupo ma è rimasto nella foresta? `.compagni`, aspetti un minuto ed eccolo al tuo fianco. Se cade in combattimento, potrai richiamarne uno nuovo solo dopo 24 ore (oppure rianimarlo, vedi sotto).
</div>

## Compagno designato

Oltre al compagno di classe esiste il compagno designato. Con 10 gradi veri in Addestrare Animali, `.designaanimale` promuove un animale ordinario a compagno designato: da quel momento è gestibile come se fosse parte del sistema compagni, con ordini, congedo e richiamo. `congedati` lo manda nel box e `.compagni richiama addestrato` lo richiama; con `.designaanimale revoca` la designazione si toglie. Il designato non riceve livelli né bonus da compagno: resta quello che è, custodito. Se ne può designare uno solo alla volta.

## Il pannello: tutto da un posto

`.compagni` apre il **pannello** del compagno: in alto ritratto, stato, PF, livello effettivo, caratteristiche, CA e talenti assegnati; sotto i pulsanti con cui si fa tutto:

| Pulsante | Cosa fa |
|---|---|
| Richiama | Lo richiama al tuo fianco |
| Attacca, Ritirati, Scappa, Annulla | Ordini rapidi di combattimento e movimento |
| Congedati | Lo congeda (solo in condizioni tranquille) |
| Nasconditi | Si nasconde |
| Inventario | Il suo zaino |
| Osserva la zona | Perlustra e ti riferisce quante presenze ci sono |
| Capacità | I poteri della sua specie |
| Condividi | Condivide il prossimo incantesimo con lui (migliorato: effetto su entrambi, durata dimezzata) |
| Tocca | Il famiglio recapita incantesimi a contatto (da livello effettivo 3) |
| Nome, Descrizione, Emote, Parla | Personalità: come si chiama, com'è fatto, gesti e parole |
| Caratteristiche, Abilità, Talenti, Crescita | Scheda e avanzamento |
| Equipaggia | Armatura e bardatura |

## Dare ordini

Gli ordini si danno dal pannello, **a voce** (parlando normalmente) o a tutti insieme col prefisso **tutti**, oppure a uno solo chiamandolo per **nome**. Il vocabolario capisce le varianti: attacca, attaccate e uccidi sono lo stesso ordine, come seguimi, seguitemi e vieni. Se sbagli parola, te lo dice lui: ordine non riconosciuto, apri il pannello per la guida.

Non tutti gli ordini sono uguali: i semplici riescono sempre, gli altri richiedono una prova di **Addestrare Animali**, e il gioco mostra pubblicamente tiro, risultato ed esito, con l'animale che si rifiuta in caso di fallimento:

| Riescono sempre | CD 10 | CD 15 | CD 17 |
|---|---|---|---|
| vai, attacca, segui, resta, congeda, scappa, annulla, ritirati | carica, proteggi, difendi, raccogli, caccia, siediti | manovre (sbilancia, disarma, afferra, fiancheggia), nascondi, osserva, apri, insegui, deposita | consegna, usa (lanciare un incantesimo tramite lui) |

Se la creatura è ferita, la CD sale di +2. Con `usa nome-incantesimo` gli fai lanciare un incantesimo; con `osserva la zona` ti riferisce quante presenze ci sono intorno; congedarlo si può solo in condizioni tranquille.

<div class="wotsc-esempio" markdown="1">
Il lupo è lontano e vuoi che torni? `tutti resta` e poi `tutti segui`. Vuoi che attacchi quel bandito? `Lupo attacca` (se si chiama Lupo). Vuoi che gli porti via la spada? `Lupo disarma`: qui serve la prova di Addestrare Animali.
</div>

Limiti: il compagno obbedisce entro **18 caselle** e nello stesso reame, solo se attivo. Con silenzio o sordità di mezzo servono i gesti a vista. Da gestione passano amico/alleato, trasferimenti, obbedienza e congedo, mentre dissolvi vale solo per gli evocati.

## Quanto è forte: il livello effettivo

È il numero su cui si calcola tutto ciò che segue:

- **Druido:** pari al livello da druido, pieno anche in multiclasse, più eventuali livelli da domini.
- **Ranger:** pari al livello da ranger **−3**, solo col Legame del Cacciatore sul compagno, con corretta interazione con eventuali livelli da druido (le due progressioni si combinano, non si sommano due volte).
- **Talento Ottimo compagno:** +4 al livello effettivo, fino al massimo del livello totale del personaggio.
- **Caccia del druido:** +1 (fino a 13) sulle prede designate.
- **Tetto:** comunque mai oltre il 12.

Al crescere del livello effettivo il compagno ottiene scatti di potenza, comandi bonus e aumenti di caratteristica:

| Livello effettivo | DV | Scatti | Comandi bonus | Aumenti caratteristica | Talenti | Gradi abilità |
|---|---|---|---|---|---|---|
| 1 | 2 | 0 | 1 | 0 | 1 | 2 |
| 2 | 3 | 0 | 1 | 0 | 2 | 3 |
| 3 | 3 | 1 | 2 | 0 | 2 | 3 |
| 4 | 4 | 1 | 2 | 1 | 2 | 4 |
| 5 | 5 | 1 | 2 | 1 | 3 | 5 |
| 6 | 6 | 2 | 3 | 1 | 3 | 6 |
| 7 | 6 | 2 | 3 | 1 | 3 | 6 |
| 8 | 7 | 2 | 3 | 1 | 4 | 7 |
| 9 | 8 | 3 | 4 | 2 | 4 | 8 |
| 10 | 9 | 3 | 4 | 2 | 5 | 9 |
| 11 | 9 | 3 | 4 | 2 | 5 | 9 |
| 12 | 10 | 4 | 5 | 2 | 5 | 10 |

I **gradi di abilità** in tabella valgono a Intelligenza invariata; la formula è DV moltiplicati per (1 + modificatore di Intelligenza), minimo i DV — alzando Int con gli aumenti si ottengono più gradi. Si distribuiscono dal pulsante Abilità col tetto pari ai DV.

E con i livelli arrivano i traguardi, automatici e senza scelte da fare:

- **Eludere (3°):** se supera un tiro salvezza su Riflessi, non subisce danni invece di dimezzarli.
- **Devozione (6°):** resiste meglio agli incantesimi che controllano la mente.
- **Multiattacco (9°):** gli attacchi secondari penalizzano meno, e da qui in poi attacca tre volte.

Il compagno del ranger **condivide inoltre la lista dei Nemici Prescelti** del padrone.

<div class="wotsc-esempio" markdown="1">
Ranger di 12°: livello effettivo 9 (12−3) → 3 scatti, 4 comandi bonus, 2 aumenti a scelta, 4 talenti, multiattacco. Druido di 8°: effettivo 8 → 2 scatti, 3 comandi, 1 aumento, 4 talenti.
</div>

### Opzioni di crescita

Dal pulsante Crescita si decide come la specie evolve al raggiungimento della sua soglia (colonna Crescita in tabella):

- **Avanzamento naturale:** la specie fiorisce nella sua forma adulta, più grossa e più forte, con dadi di danno e poteri aggiornati.
- **Taglia contenuta:** niente cambi di taglia né attacchi nuovi, in cambio +2 a Destrezza e Costituzione.
- **Aumenti di caratteristica:** si assegnano uno a uno dal pulsante Caratteristiche.
- **Gradi di abilità:** si distribuiscono dal pulsante Abilità col tetto pari ai DV (con Intelligenza sotto 3 solo quelle base).
- **Talenti:** quelli guadagnati coi DV si completano dal pulsante Talenti.

<div class="wotsc-esempio" markdown="1">
Un lupo che tocca la soglia 7 con avanzamento naturale: Forza da 13 a 21, Costituzione da 15 a 19 (ma Destrezza da 15 a 13), armatura +2, taglia maggiore e morso da 1d6 a 1d8. Più potenza bruta, meno scatto.
</div>

## Se muore

Se il compagno muore può essere **rianimato con le magie apposite**; altrimenti bisogna attendere il tempo previsto (24 ore di cooldown) prima di richiamarne uno nuovo con `.compagni`.

## Vedi anche

- [Druido](/classi/druido/) e [Ranger](/classi/ranger/): privilegi e comandi di classe
- [Elenco dei comandi](/sistemi/elencocomandi/): sintassi di tutti i comandi citati
