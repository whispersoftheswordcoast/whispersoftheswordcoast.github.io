---
title: Magia
layout: sistemi
order: 22
excerpt: Tutto quel che serve sapere sulla magia prima del primo giorno di gioco
---

# Magia

<blockquote class="citazione">
  <p>“Il mondo è fatto di regole. Io ho solo speso abbastanza tempo sui libri per imparare a riscriverle.”</p>
  <footer>— <cite>anonimo</cite></footer>
</blockquote>

<img src="{{ '/assets/images/magia.webp' | relative_url }}" alt="magia" style="float: left; width: 20%; max-width: 200px; height: auto; margin: 0 1.5rem 1rem 0; border-radius: 10px;" />

La magia funziona a slot giornalieri divisi per livello di incantesimo: ogni lancio consuma uno slot del suo livello, e gli slot si ricaricano solo con riposo e memorizzazione. Le classi si dividono in preparate (scelgono in anticipo cosa tenere pronto) e spontanee (lanciano dai conosciuti fino a esaurimento slot).

<div class="wotsc-attention" markdown="1">
Non spaventarti per la quantità di comandi in questa pagina: molti sono già nei menu contestuali cliccando sul personaggio, e in genere si gioca legandoli a macro da tastiera e pulsanti a schermo su ClassicUO. Per partire, vedi [Macro per gli incantesimi](/primipassi/#macro-per-gli-incantesimi).
</div>

<div style="clear: both;"></div>

## Preparati e spontanei: le due famiglie

Le classi si dividono in due famiglie, e conviene capirlo subito. Mago, Chierico, Druido, Paladino e Ranger **preparano**: al mattino (si fa per dire) scelgono con `.preparaspells` quali incantesimi tenere pronti, li controllano con `.memo` e li sfogliano con `.spells`. Ogni slot lanciato è andato, e per averne di nuovi serve riposare e rimemorizzare. Al risveglio dopo il riposo il gioco chiede sempre se cambiare gli incantesimi o tenere i precedenti: non serve rifare tutto da zero ogni volta.

Stregone e Bardo invece sono **spontanei**: conoscono pochi incantesimi, ma li tirano fuori al momento finché hanno slot. Niente preparazione, più rapidità, meno scelta. Se ami improvvisare, sono la tua casa; se ami pianificare, prendi un preparato.

<div class="wotsc-esempio" markdown="1">
Uno stregone che conosce dardo incantato e mani brucianti decide sul momento quale lanciare e quante volte, senza averlo deciso al mattino.
</div>

## Il riposo: dove tutto ricomincia

Niente riposo, niente magia. Per ricaricare serve un letto vicino e nessun nemico attorno: il gioco controlla tutto prima di farti sedere. Il Mago studia il Libro, i divini pregano col simbolo sacro in mano, gli spontanei recuperano gli slot dormendo. Regola d'oro del primo giorno: prima di uscire per una spedizione, controlla di aver memorizzato. Dopo, è tardi.

<div class="wotsc-esempio" markdown="1">
Routine sicura: torni in locanda, ti siedi al letto, `.memo` per vedere gli slot vuoti, `.preparaspells` per riempirli, e riparti carico.
</div>

<div class="wotsc-viewer">

    <button class="wotsc-viewer-prev" aria-label="Immagine precedente">&#10094;</button>

    <figure class="wotsc-viewer-item active">
        <img src="{{ '/assets/images/rest.webp' | relative_url }}" alt="riposo in locanda">
        <figcaption><strong>riposo in locanda</strong>Letto vicino, niente nemici.</figcaption>
    </figure>

    <figure class="wotsc-viewer-item">
        <img src="{{ '/assets/images/rest2.webp' | relative_url }}" alt="preparazione">
        <figcaption><strong>preparazione</strong>Automatica dopo il riposo: tieni o cambia.</figcaption>
    </figure>

    <button class="wotsc-viewer-next" aria-label="Immagine successiva">&#10095;</button>

    <div class="wotsc-viewer-count">1 / 2</div>

</div>

## Il tuo primo incantesimo

Si lancia scrivendo `.casta` seguito dal nome o dal numero dell'incantesimo. Se sei incollato a un nemico, `.casta difensivo` ti fa lanciare senza provocare attacchi di opportunità, ma al prezzo di una prova di Concentrazione con CD 15 + 2 per livello dell'incantesimo (+4 col talento Incantesimo in Combattimento): se la fallisci, perdi lo slot. Chi ha più classi usa i comandi con nome (`casta` più il nome della classe) per scegliere da quale lista pescare; con `.sceglicast` ne fissa una come predefinita.

<div class="wotsc-esempio" markdown="1">
`.casta armatura magica` prima di entrare in un dungeon; `.casta 8` per l'ottavo della lista senza scriverlo. Un mago/chierico usa `.castamago` per l'arcana e `.castachierico` per la divina, oppure `.sceglicast mago` e da lì `.casta` usa sempre l'arcana (`nessuna` per tornare al selettore).
</div>

## Slot, bonus e piccoli privilegi

Ogni livello dà un certo numero di slot per livello di incantesimo, e li trovi nelle schede delle classi. Sopra si aggiungono gli slot bonus da caratteristica alta: Intelligenza per il Mago, Saggezza per Chierico, Druido e Ranger, Carisma per Stregone, Bardo e Paladino. Il bonus scatta solo se il punteggio arriva alle soglie in tabella, e vale solo per i livelli di incantesimo che sai già lanciare: un bonus di 3° a chi arriva al 2° non serve a niente. Il Chierico aggiunge uno slot di dominio per livello, il Mago specialista uno di scuola per livello.

| Punteggio | 1° | 2° | 3° | 4° | 5° | 6° | 7° | 8° | 9° |
|---|---|---|---|---|---|---|---|---|---|
| 12-13 | +1 | — | — | — | — | — | — | — | — |
| 14-15 | +1 | +1 | — | — | — | — | — | — | — |
| 16-17 | +1 | +1 | +1 | — | — | — | — | — | — |
| 18-19 | +1 | +1 | +1 | +1 | — | — | — | — | — |
| 20-21 | +2 | +1 | +1 | +1 | +1 | — | — | — | — |
| 22-23 | +2 | +2 | +1 | +1 | +1 | +1 | — | — | — |
| 24-25 | +2 | +2 | +2 | +1 | +1 | +1 | +1 | — | — |
| 26-27 | +2 | +2 | +2 | +2 | +1 | +1 | +1 | +1 | — |
| 28-29 | +3 | +2 | +2 | +2 | +2 | +1 | +1 | +1 | +1 |

## Metamagia: i talenti si armano

Avere un talento di metamagia non basta: va anche armato con `.metamagia`, dal gump o per nome, con `tutto` per attivarli tutti e `reset` per spegnerli. Chi prepara la impacchetta dentro lo slot maggiorato (un intensificato a 2 si prepara in uno slot di 2°); chi lancia spontaneo la applica al momento, ma il lancio rallenta di un round, salvo Incantesimi rapidi. E attenzione: le metamagie armate valgono solo per gli incantesimi che le consentono, gli altri le ignorano.

<div class="wotsc-esempio" markdown="1">
Un dardo incantato intensificato a 2 occupa uno slot di 2° livello e picchia più forte del normale.
</div>

<img src="{{ '/assets/images/metamagia2.webp' | relative_url }}" alt="metamagia" style="display: block; margin: 0 auto; max-width: 720px;" />

## Duelli e controincantesimi

La magia è anche un duello di nervi: con `.controincantesimo` puoi provare a spezzare il lancio di un avversario mentre lo sta facendo, e con `.duellomagico` due incantatori arcani si sfidano in regola.

## Pergamene: crearle, scriverle e lanciarle

Le pergamene sono oggetti a completamento di incantesimo: contengono una magia già quasi pronta, che chiunque abbia i requisiti può liberare leggendola. La scorta di emergenza per eccellenza, ma anche merce, bottino e fonte di studio.

Per scriverne una serve il talento **Scrivere Pergamene** e si lavora di penna e calamaio: doppio clic sulla penna, bersaglio su una pergamena vuota, e serve inchiostro a sufficienza (2 cariche). La magia da copiare viene dal grimorio — decifrato, o tuo — oppure dagli incantesimi memorizzati, se sei un mago; gli spontanei pescano dai conosciuti, i divini dai memorizzati. Il mago non può scrivere sopra il proprio livello di lancio e sceglie a che livello fissare la pergamena, da un minimo pari a due volte il circolo meno uno fino al proprio livello: più alto è, più la pergamena picchia — e più costa.

Il prezzo si paga in due monete: rame pari a livello di lancio per circolo per 1250 (minimo 1250) e punti esperienza pari a livello totale per circolo per 100 (minimo 100, senza mai scendere sotto il minimo del tuo livello). Nascono così pergamene **arcane** (mago, stregone, bardo, warlock) e **divine** (chierico, paladino, druido, ranger, oracolo), ciascuna del suo circolo.

<div class="wotsc-esempio" markdown="1">

Mago di 5° che scrive una Palla di Fuoco a livello 5: paga 5 × 3 × 1250 rame e 5 × 3 × 100 px, e la pergamena lancerà sempre come un 5°.

</div>

Per lanciarla basta il doppio clic dallo zaino — ma attento, ti rivela. Serve un livello di incantatore adeguato al circolo, la pergamena decifrata e l'incantesimo nella lista della tua classe; la magia parte al livello di lancio scritto sopra, non al tuo. Chi non ha la classe giusta può provarci con **Utilizzare Oggetti Magici** (CD pari a 5 per circolo): se fallisce, la pergamena si consuma e il contraccolpo fa male, danni puri. La regressione mentale impedisce del tutto la lettura, e in forma selvatica non parlante serve Lingua selvaggia. `.elencopergamene` apre l'interfaccia con tutte le pergamene del contenitore indicato, divise per circolo e lanciabili da lì; `.castapergamene` le lancia dal portapergamene marcato con `.sceltaportapergamene` (max 50 oggetti).

## Grimori: imparare e mantenere gli incantesimi

Il grimorio è la memoria esterna del mago: Libro dell'Apprendista, Libro del Mago, Grimorio o Arcanabula, ognuno con le sue pagine massime. Si scrive solo sui propri libri, con penna e inchiostro (tante cariche quanto il circolo), e ogni incantesimo occupa due pagine per circolo — l'Apprendista non va oltre il 2°. Senza il libro nello zaino, al riposo quegli incantesimi non si memorizzano: custodiscilo come la vita.

Imparare una magia nuova è copiare: da una pergamena altrui (decifrata, e la pergamena si dissolve), dal libro di un altro mago (che resta dov'è) o dalla propria memoria (e la memorizzazione si consuma). Copiare non è gratis: serve una prova di **Sapienza Magica con CD 15 più il circolo** (+2 se è della tua scuola di specializzazione), e la specializzazione può impedire alcuni apprendimenti. Se fallisci copiando da uno scritto altrui, dovrai aspettare prima di poter riprovare quello stesso incantesimo. I propri scritti, invece, sono sempre leggibili senza prove; quelli altrui vanno prima decifrati, di norma con **Lettura del Magico** (10 minuti per livello), scegliendo se renderli chiari per tutti o solo per sé.

<div class="wotsc-esempio" markdown="1">

Trovi una pergamena di Ragnatela di un collega: la decifri, superi Sapienza Magica CD 17, la pergamena si dissolve e Ragnatela entra nel tuo grimorio occupando 4 pagine. Dalla prossima preparazione potrai memorizzarla.

</div>
