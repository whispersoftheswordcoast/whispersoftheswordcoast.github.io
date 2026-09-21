---
title: Magia
layout: sistemi
order: 7
excerpt: Tutto quel che serve sapere sulla magia prima del primo giorno di gioco
---

# Magia

<blockquote class="citazione">
  <p>“Il mondo è fatto di regole. Io ho solo speso abbastanza tempo sui libri per imparare a riscriverle.”</p>
  <footer>— <cite>anonimo</cite></footer>
</blockquote>

La magia funziona a slot giornalieri divisi per livello di incantesimo: ogni lancio consuma uno slot del suo livello, e gli slot si ricaricano solo con riposo e memorizzazione. Le classi si dividono in preparate (scelgono in anticipo cosa tenere pronto) e spontanee (lanciano dai conosciuti fino a esaurimento slot).

<div class="wotsc-esempio" markdown="1">
Non spaventarti per la quantità di comandi in questa pagina: molti sono già nei menu contestuali cliccando sul personaggio, e in genere si gioca legandoli a macro da tastiera e pulsanti a schermo su ClassicUO. Per partire, vedi [Macro per gli incantesimi](/primipassi/#macro-per-gli-incantesimi).
</div>

## Preparati e spontanei: le due famiglie

Le classi si dividono in due famiglie, e conviene capirlo subito. Mago, Chierico, Druido, Paladino e Ranger **preparano**: al mattino (si fa per dire) scelgono con `.preparaspells` quali incantesimi tenere pronti, li controllano con `.memo` e li sfogliano con `.spells`. Ogni slot lanciato è andato, e per averne di nuovi serve riposare e rimemorizzare. Al risveglio dopo il riposo il gioco chiede sempre se cambiare gli incantesimi o tenere i precedenti: non serve rifare tutto da zero ogni volta.

Stregone e Bardo invece sono **spontanei**: conoscono pochi incantesimi, ma li tirano fuori al momento finché hanno slot. Niente preparazione, più rapidità, meno scelta. Se ami improvvisare, sono la tua casa; se ami pianificare, prendi un preparato.

<div class="wotsc-esempio" markdown="1">
Uno stregone che conosce dardo incantato e mani brucianti decide sul momento quale lanciare e quante volte, senza averlo deciso al mattino.
</div>

## Il riposo: dove tutto ricomincia

Niente riposo, niente magia. Per ricaricare serve un letto vicino, nessun nemico attorno e ferite chiuse: il gioco controlla tutto prima di farti sedere. Il Mago studia il Libro, i divini pregano col simbolo sacro in mano, gli spontanei recuperano gli slot dormendo. Regola d'oro del primo giorno: prima di uscire per una spedizione, controlla di aver memorizzato. Dopo, è tardi.

<div class="wotsc-esempio" markdown="1">
Routine sicura: torni in locanda, ti siedi al letto, `.memo` per vedere gli slot vuoti, `.preparaspells` per riempirli, e riparti carico.
</div>

## Il tuo primo incantesimo

Si lancia scrivendo `.casta` seguito dal nome o dal numero dell'incantesimo. Se sei incollato a un nemico, `.casta difensivo` ti fa lanciare senza provocare attacchi di opportunità, ma al prezzo di una prova di Concentrazione con CD 15 + 2 per livello dell'incantesimo (+4 col talento Incantesimo in Combattimento): se la fallisci, perdi lo slot. Chi ha più classi usa i comandi con nome (`casta` più il nome della classe) per scegliere da quale lista pescare; con `.sceglicast` ne fissa una come predefinita.

<div class="wotsc-esempio" markdown="1">
`.casta armatura magica` prima di entrare in un dungeon; `.casta 8` per l'ottavo della lista senza scriverlo. Un mago/chierico usa `.castamago` per l'arcana e `.castachierico` per la divina, oppure `.sceglicast mago` e da lì `.casta` usa sempre l'arcana (`nessuna` per tornare al selettore).
</div>

## Slot, bonus e piccoli privilegi

<div class="wotsc-attention" markdown="1">
Ogni livello dà un certo numero di slot per livello di incantesimo, e li trovi nelle schede delle classi. Sopra si aggiungono gli slot bonus da caratteristica alta: Intelligenza per il Mago, Saggezza per Chierico, Druido e Ranger, Carisma per Stregone, Bardo e Paladino. Il bonus scatta solo se il punteggio arriva alle soglie in tabella, e vale solo per i livelli di incantesimo che sai già lanciare: un bonus di 3° a chi arriva al 2° non serve a niente. Il Chierico aggiunge uno slot di dominio per livello, il Mago specialista uno di scuola per livello.
</div>

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

## Duelli, controincantesimi e pergamene

La magia è anche un duello di nervi: con `.controincantesimo` puoi provare a spezzare il lancio di un avversario mentre lo sta facendo, e con `.duellomagico` due incantatori arcani si sfidano in regola. Le pergamene sono la scorta di emergenza: `.castapergamene` le lancia solo dal portapergamene marcato con `.sceltaportapergamene` (max 50 oggetti), e solo se decifrate — `.elencopergamene` apre l'interfaccia con tutte le pergamene (arcane e divine) del contenitore indicato, divise per circolo e lanciabili da lì.
