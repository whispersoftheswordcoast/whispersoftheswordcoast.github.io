---
title: Stirpi dello stregone
layout: sistemi
permalink: /sistemi/stirpi/
order: 26
excerpt: Cosa sono le stirpi, come si scelgono e come si usano i poteri delle 9 stirpi fino al 12° livello
---

# Stirpi dello stregone

In base alla stirpe, gli stregoni hanno a disposizione poteri diversi: ogni stregone ne sceglie 1 e la tiene per sempre. La fonte può essere un'eredità del sangue o un evento estremo del passato di famiglia: un drago tra gli antenati o un nonno che firmò un patto col diavolo. Questa guida spiega come si sceglie, come si attivano i poteri e cosa fa ognuna delle **9 stirpi fino al 12° livello**.

## Scegliere la stirpe

Al primo livello da stregone, con `.poterestirpe`, il gioco ti chiede di sceglierne **1 tra le 9 stirpi**. Non puoi cambiarla dopo: la conferma è permanente. Due stirpi chiedono una scelta in più, sempre permanente: la draconica fa scegliere il drago tra 10 tipi, l'arcana fa scegliere una Conoscenza di classe.

<div class="wotsc-esempio" markdown="1">
Scegli la draconica e poi il rosso: avrai resistenza al fuoco e soffio a cono. Scegli il blu e avrai resistenza elettrica con soffio a linea. Una volta confermato il drago, resta quello.
</div>

## Usarli in gioco

Tutti i poteri passano da un unico comando:

`.poterestirpe [potere]`

<img src="{{ '/assets/images/stirpemenu.JPG' | relative_url }}" alt="menu dei poteri di stirpe" style="display: block; margin: 0 auto;" />

Se scrivi solo il comando si apre il **menu con i poteri disponibili al tuo livello**, con le cariche rimaste scritte accanto a ognuno: scegli la voce e il potere parte. Puoi anche scriverlo direttamente aggiungendo una delle seguenti parole dopo il comando. Vale anche il nome per esteso con i seguenti alias:

| Se scrivi | Il gioco attiva |
|---|---|
| `fuoco sacro`, `fuoco infernale` | `fuoco` |
| `fuoco celestiale` | `raggio` |
| `getto`, `furia del tuono`, `furia dell'acqua` | `furia` |
| `ilarita` | `tocco` |
| `fuggevolezza` | `invisibilita` |
| `stop` | `interrompi il potere` |
| `famiglio` | `pannello del famiglio` |

<div class="wotsc-esempio" markdown="1">
Stregone celestiale di 1°: scrivi `.poterestirpe`, scegli `Fuoco Celestiale` dal menu e colpisci il bersaglio col raggio. Al 9° lo stesso potere si chiama `fuoco`: scrivi `.poterestirpe fuoco`, punti un'area entro 12 caselle e scateni il Fuoco Sacro.
</div>

### Come si attivano

I poteri a tocco richiedono il contatto, i raggi giungono fino a 6 caselle e le aree si designano fino a 12. Quasi tutto richiede l'azione standard, mentre le cariche di artigli e invisibilità vengono consumate a round. I poteri segnati [GDR] sono al momento solo ruolistici.

Al 3°, 5°, 7°, 9° e 11° livello impari in automatico gli incantesimi bonus della tabella di stirpe, che si aggiungono ai conosciuti. Al 7° livello scegli anche un talento bonus dalla lista di stirpe con `.poterestirpe talento`, ma solo se ne hai i prerequisiti.

## Elenco delle stirpi

### Abissale

*Poteri concessi: il sangue demoniaco ribolle e chiede di uscire.*

Talenti: Abilità focalizzata: Conoscenze (piani), Attacco poderoso, Aumentare Evocazione, Incalzare, Incantesimi potenziati, Spaccare l'arma potenziato, Spinta migliorata, Tempra possente.

- **1°**: Conoscenze (piani) di classe; evoca artigli infernali per un numero di round pari a 3 più il modificatore di Carisma: 1d4 danni (1d3 se piccolo).
- **3°**: Resistenza all'elettricità 5; veleni +2.
- **5°**: Gli artigli diventano magici.
- **7°**: Gli artigli infliggono 1d6 danni (1d4 se piccolo).
- **9°**: Resistenza 10; veleni +4; Forza +2; le creature demoniache o immonde evocate guadagnano RD contro il bene pari a metà livello da stregone (minimo 1).
- **11°**: Gli artigli aggiungono fuoco.

Comandi: `.poterestirpe artigli` per far spuntare gli artigli, `.poterestirpe stop` per interromperli, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Incuti paura |
| 5° | Forza straordinaria |
| 7° | Ira (non attivo) |
| 9° | Pelle di pietra |
| 11° | Congedo |

### Arcana

*Poteri concessi: la magia pura scorre in famiglia da generazioni.*

Talenti: Abilità focalizzata: Conoscenze (arcane), Controincantesimo migliorato, Incantare in combattimento, Incantesimo focalizzato, Incantesimi immobili, Iniziativa migliorata, Scrivere pergamene, Volontà di ferro.

- **1°**: Una Conoscenza di classe a scelta; ottiene un famiglio come fosse un mago.
- **3°**: Adepto della metamagia: il prossimo incantesimo metamagico parte senza il tempo aggiuntivo (1 uso al giorno, +1 al 7° e all'11°); inoltre gli incantesimi metamagici hanno +1 alla CD.
- **9°**: Nuova magia: un incantesimo conosciuto in più, a scelta libera tra quelli che puoi lanciare.

Comandi: `.poterestirpe metamagia` per preparare l'Adepto, `.poterestirpe magia` per scegliere la Nuova magia, `.poterestirpe talento` per il talento bonus, `.poterestirpe stop`, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Identificare |
| 5° | Invisibilità |
| 7° | Dissolvi magie |
| 9° | Porta dimensionale |
| 11° | Volo giornaliero (non attivo) |

### Celestiale

*Poteri concessi: la luce dei piani alti ti ha scelto come messaggero.*

Talenti: Abilità focalizzata: Conoscenze (religioni), Arma Accurata, Attacco in sella, Combattere in sella, Incantesimi estesi, Mobilità, Schivare, Volontà di ferro.

- **1°**: Guarire di classe; ottiene un raggio divino per 3 più Carisma usi al giorno. Contro i malvagi infligge 1d4 più metà livello danni divini, contro i buoni cura la stessa quantità (ognuno una volta al giorno); contro i neutrali non fa nulla.
- **3°**: Resistenze ad acido e freddo 5; le creature buone evocate guadagnano RD contro il male pari a metà livello da stregone (minimo 1).
- **9°**: Fuoco sacro una volta al giorno: esplosione di 2 caselle che infligge 1d6 per livello da stregone, TS Riflessi dimezza e chi fallisce tra i malvagi resta scosso.

Comandi: `.poterestirpe raggio` per il Fuoco Celestiale, `.poterestirpe fuoco` per il Fuoco Sacro, `.poterestirpe stop`, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Benedizione |
| 5° | Resistere agli elementi |
| 7° | Cerchio magico contro il male |
| 9° | Rimuovi maledizione (non attivo) |
| 11° | Colpo infuocato |

### Djinni

*Poteri concessi: la tempesta del djinn abita nei tuoi polmoni.*

Talenti: Abilità focalizzata: Conoscenze (piani), Arma Accurata, Attacco poderoso, Incantesimi potenziati, Iniziativa migliorata, Riflessi fulminei, Schivare, Tempra possente.

- **1°**: Conoscenze (piani) di classe; ottiene un raggio elettrico da 1d6 più metà livello per 3 più Carisma usi al giorno; puoi convertire in elettricità i danni energetici dei prossimi incantesimi.
- **3°**: Resistenza all'elettricità 10.
- **9°**: Furia del tuono una volta al giorno: linea che infligge tanti d6 sonori quanto metà livello, TS Riflessi dimezza e chi fallisce resta assordato per 1d6 round; resistenza 20.

Comandi: `.poterestirpe raggio` per il raggio, `.poterestirpe conversione` per attivarla o disattivarla, `.poterestirpe furia` per la Furia del Tuono, `.poterestirpe stop`, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Stretta folgorante |
| 5° | Invisibilità |
| 7° | Volare (non attivo) |
| 9° | Creazione minore (non attivo) |
| 11° | Volo giornaliero (non attivo) |

### Draconica

*Poteri concessi: un drago dorme nel tuo sangue e sogna attraverso di te.*

Talenti: Abilità focalizzata: Conoscenze (arcane), Volare, Attacco poderoso, Combattere alla cieca, Incantesimi rapidi, Iniziativa migliorata, Robustezza, Tempra possente.

- **1°**: Percezione di classe; scegli la razza draconica; artigli per un numero di round pari a 3 più il modificatore di Carisma: 1d4 danni (1d3 se piccolo).
- **3°**: Armatura naturale +1; resistenza 5 all'elemento; +1 danno per ogni dado degli incantesimi del proprio elemento.
- **5°**: Gli artigli diventano magici.
- **7°**: Gli artigli infliggono 1d6 danni (1d4 se piccolo).
- **9°**: Soffio una volta al giorno (cono da 6 o linea da 12 secondo il drago) che infligge 1d6 per livello da stregone, TS Riflessi dimezza; armatura +2; resistenza 10.
- **11°**: Gli artigli aggiungono l'elemento.

Comandi: `.poterestirpe artigli` per far spuntare gli artigli, `.poterestirpe soffio` per il soffio, `.poterestirpe stop` per interromperli, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Armatura magica |
| 5° | Resistere agli elementi |
| 7° | Volare (non attivo) |
| 9° | Paura |
| 11° | Resistenza agli incantesimi |

I draghi tra cui scegliere: bianco e argento (freddo, cono), blu e bronzo (elettricità, linea), nero e rame (acido, linea), verde (acido, cono), rosso e oro (fuoco, cono), ottone (fuoco, linea).

### Efreeti

*Poteri concessi: il fuoco dell'efreeti ti ha adottato.*

Talenti: Abilità focalizzata: Conoscenze (piani), Arma Accurata, Attacco poderoso, Incantesimi potenziati, Iniziativa migliorata, Riflessi fulminei, Schivare, Tempra possente.

- **1°**: Conoscenze (piani) di classe; ottiene un raggio di fuoco da 1d6 più metà livello per 3 più Carisma usi al giorno; puoi convertire in fuoco i danni energetici dei prossimi incantesimi.
- **3°**: Resistenza al fuoco 10.
- **9°**: Forma di efreeti una volta al giorno: diventi un efreeti per un numero di round pari al livello e chi lotta con te subisce 1d6 da fuoco; resistenza 20.

Comandi: `.poterestirpe raggio` per il raggio, `.poterestirpe conversione` per attivarla o disattivarla, `.poterestirpe forma` per la Forma di Efreeti, `.poterestirpe stop`, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Ingrandire Persone |
| 5° | Raggio Rovente |
| 7° | Palla di fuoco |
| 9° | Muro di fuoco |
| 11° | Immagine persistente (non attivo) |

### Fatata

*Poteri concessi: le fate ti hanno riso in faccia e il riso ti è rimasto dentro.*

Talenti: Abilità focalizzata: Conoscenze (natura), Incantesimi rapidi, Iniziativa migliorata, Mobilità, Riflessi fulminei, Schivare, Tiro preciso, Tiro ravvicinato.

- **1°**: Conoscenze (natura) di classe; tocco d'ilarità per 3 più Carisma usi al giorno: chi fallisce ride per un round e può solo muoversi (immune per 24 ore, inutile contro menti immuni); +2 alla CD delle compulsioni.
- **9°**: Fuggevolezza: invisibilità fino a un numero di round pari al livello (un uso per round).

Comandi: `.poterestirpe tocco` per l'Ilarita, `.poterestirpe invisibilita` per la Fuggevolezza, `.poterestirpe stop` per interromperla, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Intralciare |
| 5° | Risata incontenibile di Tasha |
| 7° | Sonno Profondo |
| 9° | Veleno |
| 11° | Traslazione arborea |

### Infernale

*Poteri concessi: un contratto firmato col sangue ti lega all'inferno.*

Talenti: Abilità focalizzata: Conoscenze (piani), Combattere alla cieca, Disarmare migliorato, Incantesimi estesi, Incantesimo inarrestabile, Ingannevole, Maestria, Volontà di ferro.

- **1°**: Diplomazia di classe; tocco corruttore per 3 più Carisma usi al giorno: rende scosso per metà livello in round (minimo 1), con durate che si sommano; +2 alla CD degli charme.
- **3°**: Resistenza al fuoco 5; veleni +2.
- **9°**: Fuoco infernale una volta al giorno: esplosione di 2 caselle che infligge 1d6 per livello da stregone, TS Riflessi dimezza e i buoni che falliscono restano scossi; resistenza 10; veleni +4.

Comandi: `.poterestirpe tocco` per il Tocco Corruttore, `.poterestirpe fuoco` per il Fuoco Infernale, `.poterestirpe stop`, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Protezione dal bene |
| 5° | Raggio Rovente |
| 7° | Suggestione (non attivo) |
| 9° | Charme sui mostri |
| 11° | Dominare persone |

### Marid

*Poteri concessi: le profondità marine cantano nelle tue vene.*

Talenti: Abilità focalizzata: Conoscenze (piani), Arma Accurata, Attacco poderoso, Incantesimi potenziati, Iniziativa migliorata, Riflessi fulminei, Schivare, Tempra possente.

- **1°**: Conoscenze (piani) di classe; ottiene un raggio di freddo da 1d6 più metà livello per 3 più Carisma usi al giorno; puoi convertire in freddo i danni energetici dei prossimi incantesimi.
- **3°**: Resistenza al freddo 10.
- **9°**: Furia dell'acqua una volta al giorno: linea che infligge tanti d6 fisici quanto metà livello, TS Riflessi dimezza e chi fallisce resta accecato; resistenza 20.

Comandi: `.poterestirpe raggio` per il raggio, `.poterestirpe conversione` per attivarla o disattivarla, `.poterestirpe furia` per la Furia dell'Acqua, `.poterestirpe stop`, `.poterestirpe famiglio` per il pannello.

| Livello | Incantesimi concessi |
|---|---|
| 3° | Foschia occultante (non attivo) |
| 5° | Vedere invisibilità |
| 7° | Forma gassosa (non attivo) |
| 9° | Muro di ghiaccio |
| 11° | Immagine persistente (non attivo) |

## Vedi anche

- [Stregone](/classi/stregone/): incantesimi spontanei, famiglio e comandi
- [Magia](/sistemi/magia.html): slot, conosciuti e metamagie
- [Elenco dei comandi](/sistemi/elencocomandi.html): sintassi di `.poterestirpe`
- [Stirpi su Golarion](https://golarion.altervista.org/wiki/Stregone/Stirpi): stirpi e poteri nel manuale di riferimento
