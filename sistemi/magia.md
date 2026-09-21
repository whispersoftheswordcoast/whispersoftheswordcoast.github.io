---
title: Magia
layout: sistemi
order: 7
excerpt: Tutto quel che serve sapere sulla magia prima del primo giorno di gioco
---

# Magia

La magia funziona a slot giornalieri divisi per livello di incantesimo: ogni lancio consuma uno slot del suo livello, e gli slot si ricaricano solo con riposo e memorizzazione. Le classi si dividono in preparate (scelgono in anticipo cosa tenere pronto) e spontanee (lanciano dai conosciuti fino a esaurimento slot).

## Il tuo primo incantesimo

Si lancia scrivendo `.casta` seguito dal nome o dal numero dell'incantesimo. Esempio: `.casta armatura magica` ti mette addosso la protezione prima di entrare in un dungeon; `.casta 8` lancia l'ottavo della tua lista senza stare a scriverlo. Se sei incollato a un nemico, `.casta difensivo` ti fa lanciare proteggendoti dagli attacchi di opportunità. Esempio multiclasse: un mago/chierico usa `.castamago` per pescare dalla lista arcana e `.castachierico` per quella divina; con `.sceglicast mago` fissa l'arcana come predefinita e da lì `.casta` usa sempre quella (con `nessuna` si torna al selettore).

## Preparati e spontanei: le due famiglie

Le classi si dividono in due famiglie, e conviene capirlo subito. Mago, Chierico, Druido, Paladino e Ranger **preparano**: al mattino (si fa per dire) scelgono con `.preparaspells` quali incantesimi tenere pronti, li controllano con `.memo` e li sfogliano con `.spells`. Ogni slot lanciato è andato, e per averne di nuovi serve riposare e rimemorizzare.

Stregone e Bardo invece sono **spontanei**: conoscono pochi incantesimi, ma li tirano fuori al momento finché hanno slot. Esempio: uno stregone che conosce dardo incantato e mani brucianti può decidere sul momento quale dei due lanciare e quante volte, senza averlo deciso al mattino. Niente preparazione, più rapidità, meno scelta. Se ami improvvisare, sono la tua casa; se ami pianificare, prendi un preparato.

## Il riposo: dove tutto ricomincia

Niente riposo, niente magia. Per ricaricare serve un letto vicino, nessun nemico attorno e ferite chiuse: il gioco controlla tutto prima di farti sedere. Il Mago studia il Libro, i divini pregano col simbolo sacro in mano, gli spontanei recuperano gli slot dormendo. Esempio pratico di routine: torni in locanda, ti siedi al letto, `.memo` per vedere gli slot vuoti, `.preparaspells` per riempirli, e riparti carico. Regola d'oro del primo giorno: prima di uscire per una spedizione, controlla di aver memorizzato. Dopo, è tardi.

## Slot, bonus e piccoli privilegi

Ogni livello dà un certo numero di slot per livello di incantesimo, e li trovi nelle schede delle classi. Sopra ci piovono i bonus: caratteristica alta (Intelligenza per il Mago, Saggezza per divini e Ranger, Carisma per Stregone, Bardo e Paladino), uno slot di dominio per livello per il Chierico, uno slot di scuola per livello per il Mago specialista. Morale: la caratteristica da incantatore non è un optional, è il serbatoio.

## Metamagia: i talenti si armano

Avere un talento di metamagia non basta: va anche armato con `.metamagia`, dal gump o per nome, con `tutto` per attivarli tutti e `reset` per spegnerli. Gli intensificati si armano col livello (`intensificati N`) e costano slot extra alzando la CD: esempio, un dardo incantato intensificato a 2 occupa uno slot di 2° e picchia più forte. E attenzione: le metamagie armate valgono solo per gli incantesimi che le consentono, gli altri le ignorano.

## Duelli, controincantesimi e pergamene

La magia è anche un duello di nervi: con `.controincantesimo` puoi provare a spezzare il lancio di un avversario mentre lo sta facendo, e con `.duellomagico` due incantatori arcani si sfidano in regola. Le pergamene sono la scorta di emergenza: si elencano con `.elencopergamene` e si lanciano con `.castapergamene`, anche senza averle preparate. Portane sempre qualcuna il primo giorno: quando finisci gli slot, ti salvano la pelle.
