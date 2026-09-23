---
title: La scheda
layout: sistemi
order: 3
excerpt: Lettura tecnica della scheda del personaggio, voce per voce
---

# La scheda del personaggio

La scheda raccoglie tutte le statistiche del personaggio: caratteristiche, punti ferita, valori di combattimento, abilità, talenti e progressione. In gioco si apre con il comando `.scheda` (l'alternativa `.char` mostra le stesse informazioni). Logica di lettura: quasi ogni voce è un bonus da sommare a 1d20 contro una Classe Difficoltà (CD) — risultato pari o superiore, la prova riesce. Questa pagina descrive le voci nell'ordine in cui compaiono.

<img src="{{ '/assets/images/scheda01.webp' | relative_url }}" alt="scheda del personaggio" style="display: block; margin: 0 auto; max-width: 100%;" />

## 1. Caratteristiche e modificatori

Le sei caratteristiche descrivono il personaggio in numeri, su una scala tipica da 3 a 18 con media 10. Nei calcoli non entra il punteggio ma il **modificatore**: (punteggio − 10) / 2, arrotondato per difetto. Forza 14 significa +2, Destrezza 8 significa −1.

- **Forza:** la potenza fisica. Decide quanto fa male un colpo in mischia, se riesci a sfondare una porta, trascinare un ferito o scalare una parete. Come l'impugnatura cambia il danno è spiegato nella sezione Danno.
- **Destrezza:** riflessi e coordinazione. Serve a colpire a distanza, a schivare i colpi (Classe Armatura), ad agire per primi (iniziativa) e a tutto ciò che richiede mano leggera: furtività, scasso, acrobazia.
- **Costituzione:** la salute. Ogni punto di modificatore aggiunge un punto ferita per livello e rende più facile resistere a veleni e malattie.
- **Intelligenza:** studio e memoria. Determina quanti gradi di abilità si guadagnano a ogni livello, quante lingue si conoscono e quanto si è ferrati in Conoscenze e Sapienza Magica.
- **Saggezza:** intuito e forza di volontà. Regge la resistenza mentale, la Percezione, Guarire e la Sopravvivenza. È la caratteristica con cui chierici e druidi lanciano gli incantesimi.
- **Carisma:** la presenza. Comanda le interazioni sociali — Diplomazia, Intimidire, Raggirare, Intrattenere — e l'uso dei congegni magici. È la caratteristica con cui bardi e stregoni lanciano gli incantesimi.

<div class="wotsc-esempio" markdown="1">
Un guerriero con Forza 16 (+3) tira +3 per colpire in mischia, aggiunge +3 ai danni (spada lunga: 1d8+3) e ha +3 nelle prove di Scalare. Un mago con Forza 8 (−1) con la stessa spada tirerebbe −1 per colpire e 1d8−1 di danni: la scheda mostra subito perché ciascuno fa il suo mestiere.
</div>

<!-- PLACEHOLDER IMMAGINE: primo piano della sezione Caratteristiche della scheda, con colonne Base e Mod ben visibili -->

## 2. Punti ferita

I punti ferita (PF) misurano quanto danno il personaggio può subire prima di cadere. Ogni livello assegna un Dado Vita di classe (d10 il guerriero, d6 il mago) più il modificatore di Costituzione, con minimo 1 PF per livello.

<div class="wotsc-esempio" markdown="1">
Un guerriero con Costituzione 14 (+2) guadagna in media 7 PF per livello (5 di dado + 2): al 4° livello ha intorno ai 28 PF. Un mago con Costituzione 10 (+0) guadagna in media 3-4 PF per livello: al 4° ne ha intorno ai 14, la metà. Con Costituzione 14 anche il mago prenderebbe +2 PF per livello: +8 PF al 4°, più della metà del suo totale.
</div>

## 3. Classe Armatura

La Classe Armatura (CA) è il numero che un attacco deve eguagliare o superare per andare a segno. Formula base:

**CA = 10 + bonus di armatura + bonus di scudo + modificatore di Destrezza + modificatore di taglia + altri modificatori** (armatura naturale, deviazione, schivare)

Nota bene:

- L'armatura limita il bonus di Destrezza applicabile alla CA: un'armatura pesante protegge molto ma lascia poco spazio alla schivata.
- Se il personaggio viene colto di sorpresa, non può reagire all'attacco: perde il bonus di Destrezza e i bonus di schivare.
- Per gli attacchi di contatto in mischia e a distanza degli incantesimi, armatura, scudo e armatura naturale non contano: basta toccare il bersaglio.

<div class="wotsc-esempio" markdown="1">
Un guerriero con CA 18 (10 base + 5 di armatura + 2 di scudo + 1 di Destrezza) affronta un goblin con +3 al tiro per colpire: il goblin deve tirare 15 o più sul d20 per ferirlo. Lo stesso goblin contro un mago con CA 12 lo colpisce già con un 9.
</div>

## 4. Tiro per colpire e bonus di attacco

Il tiro per colpire è 1d20 più il **bonus di attacco**. Composizione:

- **Mischia:** Bonus di Attacco Base + modificatore di Forza + modificatore di taglia.
- **Distanza:** Bonus di Attacco Base + modificatore di Destrezza + modificatore di taglia (più eventuali penalità di gittata).

Il Bonus di Attacco Base dipende da classe e livello: le classi marziali avanzano di +1 per livello (progressione piena), le altre più lentamente (media, scarsa). I bonus da classi diverse si sommano in caso di multiclasse. Al raggiungimento di +6 si ottiene un secondo attacco per round a −5, a +11 un terzo a −10: la scheda li riporta già calcolati. Un 1 naturale sul dado è sempre un colpo mancato, un 20 naturale sempre un colpo messo a segno (e minaccia un critico).

<div class="wotsc-esempio" markdown="1">
Un ranger di 4° livello con Bonus di Attacco Base +4 e Destrezza 16 (+3) tira +7 con l'arco. Contro un nemico con CA 15 deve fare 8 o più sul d20: più della metà dei colpi va a segno.
</div>

## 5. Danno

A colpo messo a segno, il danno è il dado dell'arma più il modificatore di Forza (in mischia e con armi da lancio). Come si impugna l'arma cambia il bonus:

- **Una mano:** dado + tutto il modificatore di Forza.
- **Mano secondaria:** dado + metà modificatore di Forza (le penalità valgono per intero).
- **Due mani:** dado + una volta e mezzo il modificatore di Forza (le penalità non si moltiplicano).

Se le penalità riducono il totale sotto 1, il colpo infligge comunque 1 danno. Sul 20 naturale il colpo minaccia un **critico**: confermato, i dadi di danno si tirano più volte e si sommano (i dadi bonus, come quelli di un'arma infuocata, si tirano una volta sola). La scheda riporta il danno già calcolato, così in combattimento si tira e basta.

<div class="wotsc-esempio" markdown="1">
Spada lunga con Forza 16 (+3): a una mano fa 1d8+3, a due mani 1d8+4. Con un critico x2 confermato: 2d8+6 a una mano, 2d8+8 a due mani.
</div>

## 6. Tiri salvezza

I tiri salvezza misurano la resistenza contro attacchi insoliti o magici. Formula:

**Tiro salvezza = bonus salvezza base + modificatore di caratteristica**

Le tre categorie, con la caratteristica associata:

- **Tempra + Costituzione:** veleni, malattie, sofferenze fisiche.
- **Riflessi + Destrezza:** attacchi ad area da schivare (esplosioni, trappole).
- **Volontà + Saggezza:** controllo mentale ed effetti magici sulla mente.

Ogni classe assegna progressione **buona** ad alcuni tiri e **scarsa** agli altri (colonna *Tiri buoni* nelle [schede delle classi](/classi/)): un tiro buono cresce di +2 più metà livello, uno scarso di circa un terzo del livello. I bonus da fonti diverse si cumulano. Un 1 naturale è sempre un fallimento, un 20 naturale sempre un successo.

<div class="wotsc-esempio" markdown="1">
Una palla di fuoco con CD 15 investe il gruppo. Il ladro con Riflessi +6 si salva con un 9 o più e dimezza il danno; il chierico con Riflessi +2 deve fare 13 o più. È per questo che il ladro ride delle esplosioni e il chierico no.
</div>

<!-- PLACEHOLDER IMMAGINE: primo piano della sezione Tiri salvezza (Base/Totale) della scheda -->

## 7. Abilità e gradi

Le abilità misurano tutto ciò che il personaggio sa fare fuori dal combattimento: Percezione, Guarire, Furtività, Conoscenze e le altre. Si acquistano con **gradi**: a ogni livello se ne ricevono un numero pari alla classe più il modificatore di Intelligenza (minimo 1 per livello), con tetto massimo pari ai Dadi Vita totali. Le **abilità di classe** — quelle dell'addestramento della propria classe — ricevono bonus +3 dal primo grado investito (non cumulabile in multiclasse).

Prova di abilità: **1d20 + gradi + modificatore di caratteristica (+3 se abilità di classe addestrata)** contro la CD dell'impresa. Le abilità basate su Forza e Destrezza subiscono la penalità dell'armatura indossata. A differenza di tiri per colpire e tiri salvezza, nelle prove di abilità il 20 e l'1 naturale non sono successo e fallimento automatici: conta solo il totale contro la CD.

<div class="wotsc-esempio" markdown="1">
Un ranger cerca tracce (Sopravvivenza, CD 15): 4 gradi + 2 di Saggezza + 3 di abilità di classe = +9. Gli basta un 6 sul dado. Un guerriero senza gradi nella stessa abilità tira solo il modificatore di Saggezza: deve sperare in un numero alto.
</div>

<img src="{{ '/assets/images/scheda03.webp' | relative_url }}" alt="sezione abilità della scheda" style="display: block; margin: 0 auto; max-width: 100%;" />

## 8. Talenti

I talenti sono capacità speciali non legate a razza, classe o abilità: stili di combattimento, magie aggiuntive, bonus alle statistiche, azioni altrimenti precluse. Ciascun talento riporta:

- **Prerequisiti:** punteggio di caratteristica minimo, altri talenti, Bonus di Attacco Base minimo, gradi di abilità o privilegi di classe. Un talento può averne più di uno e può essere selezionato già al livello in cui li si soddisfa.
- **Beneficio:** cosa consente di fare. Selezionare due volte lo stesso talento non cumula i benefici, salvo indicazione contraria.
- **Vincolo d'uso:** perso un prerequisito, il talento non è utilizzabile (ma non viene perso: torna attivo al ripristino del requisito).

I talenti si acquisiscono con l'avanzamento (vedi [livelli](/sistemi/livelli/)) e alcuni sono assegnati come bonus di classe. Esistono famiglie distinte: generali, di combattimento, di metamagia, di creazione oggetti e altre.

<div class="wotsc-esempio" markdown="1">
Un guerriero riceve un talento bonus al 1° livello e a ogni livello pari: al 1° sceglie Attacco Poderoso, al 2° Incalzare, costruendosi uno stile pezzo per pezzo. Un mago, che non ha talenti bonus, deve scegliere con più cura gli unici che il suo avanzamento gli concede.
</div>

<img src="{{ '/assets/images/scheda02.webp' | relative_url }}" alt="sezione talenti della scheda" style="display: block; margin: 0 auto; max-width: 100%;" />

## 9. Resistenze

Le resistenze riducono i danni da fonti elementali e magiche: fuoco, freddo, elettricità, acido, energia negativa. Resistenza al fuoco 10 significa che i primi 10 danni da fuoco di ogni colpo vengono ignorati — una torcia magica da 1d6 non scalfisce, una palla di fuoco da 30 resta comunque un problema. Fonti tipiche: tratti razziali, incantesimi, oggetti magici.

## 10. BMC e DMC

Servono per le **manovre in combattimento**: sbilanciare, disarmare, spingere, lottare, oltrepassare, spezzare e le altre — tutto ciò che non è un semplice colpo. Due valori:

- **BMC (Bonus di Manovra in Combattimento):** Bonus di Attacco Base + modificatore di Forza + modificatore di taglia. Misura l'attitudine a eseguire manovre.
- **DMC (Difesa di Manovra in Combattimento):** 10 + Bonus di Attacco Base + modificatore di Forza + modificatore di Destrezza + modificatore di taglia. È la CD da battere per riuscire nella manovra.

Eseguire una manovra significa tirare 1d20 + BMC contro la DMC del bersaglio (20 naturale sempre riuscito, 1 sempre fallito). Senza il talento migliorato corrispondente, tentare una manovra provoca un attacco di opportunità. Un bersaglio impreparato non applica la Destrezza alla DMC.

<div class="wotsc-esempio" markdown="1">
Un guerriero con BMC +5 vuole sbilanciare un orco con DMC 14: gli serve un 9 o più. Se riesce, l'orco finisce prono e si rialza sprecando il turno; se fa 1, la manovra fallisce e l'orco, senza il talento Sbilanciare Migliorato, gli assesta un attacco di opportunità.
</div>

## 11. Iniziativa

L'iniziativa è una prova di Destrezza tirata all'inizio di ogni combattimento e determina l'ordine dei turni, dal risultato più alto al più basso, ripetuto ogni round. Chi ha Destrezza alta agisce sistematicamente prima degli altri. Prima del primo turno il personaggio è impreparato: perde il bonus di Destrezza alla CA e non può compiere attacchi di opportunità.

## 12. Allineamento, divinità, esperienza

- **Allineamento:** la collocazione morale del personaggio (da Legale Buono a Caotico Malvagio). Alcune classi lo esigono come requisito: il Paladino solo Legale Buono, il Monaco solo legale.
- **Divinità:** rilevante per le classi divine (chierico, paladino, druido, ranger), che ne traggono gli incantesimi. La scelta vincola il personaggio e non si modifica con leggerezza.
- **PX e livello role:** punti esperienza e valutazione del gioco di ruolo (stelline da 1 a 12), che aprono la progressione fino al livello 12. Meccaniche descritte nelle pagine su [livelli](/sistemi/livelli/) e [voto ruolo](/mediaruolo/).

## Riferimenti

Le meccaniche descritte seguono il regolamento Pathfinder 1e. Approfondimenti, tabelle complete ed elenchi esaustivi su Golarion Insider (wiki italiana):

- Il tiro del dado e l'avanzamento: [Il gioco](https://golarion.altervista.org/wiki/Il_gioco)
- Le sei caratteristiche e i modificatori: [Le Sei Caratteristiche](https://golarion.altervista.org/wiki/Le_Sei_Caratteristiche)
- Tiro per colpire, CA, danni, punti ferita: [Statistiche di Combattimento](https://golarion.altervista.org/wiki/Statistiche_di_Combattimento)
- Tiri salvezza: [Tiri Salvezza](https://golarion.altervista.org/wiki/Tiri_Salvezza)
- Abilità e gradi: [Abilità](https://golarion.altervista.org/wiki/Abilit%C3%A0)
- Talenti e prerequisiti: [Talenti](https://golarion.altervista.org/wiki/Talenti)
- Manovre, BMC e DMC: [Manovre in Combattimento](https://golarion.altervista.org/wiki/Manovre_in_Combattimento)
