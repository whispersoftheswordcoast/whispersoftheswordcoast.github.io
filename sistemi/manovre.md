---
title: Manovre di combattimento
layout: sistemi
permalink: /sistemi/manovre/
order: 28
excerpt: Come funzionano disarmare, sbilanciare, lotta, sporchi trucchi e le altre manovre, con comandi e azioni
---

# Manovre di combattimento

Oltre a colpire, in combattimento si può disarmare, sbilanciare, spingere, afferrare, fintare e molto altro. Le manovre si risolvono con una prova di BMC contro la DMC del bersaglio e seguono tutte le stesse regole di base. Questa guida spiega come si usano, cosa fa ognuna e quanto costa.

## Come funzionano

Tutte le manovre passano dalla finestra **`.manovre`**, che mostra solo le opzioni davvero disponibili con il motivo quando una è bloccata, oppure dai comandi testuali dedicati, uno per manovra. La manovra scelta resta preparata e parte alla prima azione utile. Non serve colpire prima, perché ci pensa il ciclo di combattimento.

La prova è **BMC contro DMC**. Il Bonus di Manovra in Combattimento è Bonus di Attacco Base più Forza più modificatore di taglia speciale; la Difesa dalle Manovre in Combattimento è 10 più Bonus di Attacco Base più Forza più Destrezza più taglia speciale. Le taglie minute usano Destrezza al posto di Forza, dal –8 della Piccolissima al +8 della Colossale passando per lo +0 della Media.

A meno che non sia indicato diversamente, tentare provoca un **attacco di opportunità** da chi è a portata: se si viene colpiti si subiscono i danni normalmente e li si applica come penalità al tiro. Contro bersagli immobilizzati, privi di sensi o incapacitati la manovra riesce automaticamente; contro bersagli storditi si ha bonus +4. Un 20 naturale è sempre successo, un 1 sempre fallimento. Contro bersagli di più di una taglia sopra la propria, spingere, sbilanciare, oltrepassare, trascinare e riposizionare non si possono nemmeno tentare. Una finta riuscita si consuma al primo uso e vale per l'attacco successivo.

<div class="wotsc-esempio" markdown="1">

Vuoi disarmare senza esporti a colpi gratuiti? Occorre Disarmare Migliorato. Vuoi trascinare un elefante essendo di taglia Media? Non si può, perché è due taglie sopra.

</div>

## La tabella completa

| Manovre | Comando | Azione |
|---|---|---|
| Disarmare | `.manovre` | Sostituisce un attacco |
| Sbilanciare | `.manovre` | Sostituisce un attacco |
| Lancio Ki | `.lancioki` | Sostituisce un attacco (richiede talento) |
| Botta Sbilanciante | `.bottasbilanciante` | Standard + veloce se il colpo riesce (richiede Attacco Poderoso) |
| Spingere | `.spinta` | Standard |
| Spezzare arma | `.spezzare` | Sostituisce un attacco |
| Spezzare oggetto indossato | `.spezzare oggetto` | Sostituisce un attacco |
| Oltrepassare | `.oltrepassare` | Standard + movimento |
| Trascinare | `.trascinare` | Standard + movimento |
| Riposizionare | `.riposizionare` | Standard |
| Rubare | `.rubare` | Standard |
| Stile dello Scorpione | `.scorpione` | Standard (richiede talento) |
| Pugno della Gorgone | `.gorgone` | Standard (richiede talento) |
| Fintare | `.fintare` | Standard (movimento con Fintare Migliorato) |
| Finta con due armi | `.fintare duearmi` | Sacrifica il primo attacco primario |
| Finta a distanza | `.fintare distanza` | Come Fintare; consuma un proiettile |
| Finta gemella | `.fintare gemella` | Come Fintare, su due bersagli vicini |
| Sporco trucco<br>(accecato, abbagliato, assordato,<br>intralciato, scosso, infermo) | `.sporcotrucco <effetto>` | Standard |
| Rimuovere un trucco | `.rimuovitrucco <effetto>` | Azione di movimento |
| Iniziare una presa | `.lotta` | Standard |
| Mantenere la presa | `.lotta mantieni` | Standard (movimento con Lottare Superiore) |
| Infliggere danni letali | `.lotta danno` | Come mantenimento |
| Infliggere danni non letali | `.lotta nonletale` | Come mantenimento |
| Immobilizzare | `.lotta immobilizza` | Come mantenimento |
| Muovere la presa | `.lotta muovi` | Come mantenimento |
| Liberarsi con BMC | `.lotta libera` | Standard |
| Artista della Fuga | `.lotta fuga` | Standard |
| Invertire la presa | `.lotta inverti` | Standard |
| Rilasciare | `.lotta rilascia` | Gratuita |
| Legare con corde | `.lotta lega` | Standard (richiede una corda) |
| Aiutare un alleato | `.lotta aiuta` | Standard |
| Sciogliere le corde | `.lotta sciogli` | Standard |
| Acrobazia | `.acrobazia` | Movimento |
| Acrobazia veloce | `.acrobazia veloce` | Movimento |
| Colpo Basso | `.colpobasso` | Completa |
| Giravolta Sbilanciante | `.giravoltasbilanciante` | Completa (bastone ferrato a due mani) |
| Attacco Rapido | `.attaccorapido` | Completa |
| Tiro in Movimento | `.tiroinmovimento` | Completa |
| Carica | `.caricare` | Vedi sotto |

## Manovra per manovra

**Disarmare**: come azione che sostituisce un attacco, fa cadere un oggetto trasportato a scelta di chi tenta, anche impugnato con due mani. Tentare disarmati comporta penalità –4. Se l'attacco eccede la DMC di 10 o più, cadono gli oggetti di entrambe le mani; se fallisce di 10 o più, cade la tua. A mani nude la si può raccogliere al volo.

**Sbilanciare**: manda prono il bersaglio. Fallendo di 10 o più, finisci prono tu, a meno di lasciare la presa sull'arma se impugni un bastone o un'arma adatta.

**Spingere**: come azione standard, sposta il bersaglio di un numero di caselle pari al margine della prova.

**Spezzare**: come azione che sostituisce un attacco, danneggia l'arma (si applicano durezza e punti ferita) oppure un oggetto indossato a scelta, indicando prima la creatura e poi l'oggetto.

**Oltrepassare**: come azione standard con movimento, attraversa lo spazio di una creatura adiacente non più grande di una taglia. Se fallisce, ci si ferma davanti all'avversario. Con `.oltrepassare evita` o `.oltrepassare resisti` si imposta la reazione automatica ai tentativi altrui.

**Trascinare**: come azione standard con movimento, arretra trascinando il bersaglio con sé.

**Riposizionare**: come azione standard, sposta il bersaglio in una casella a scelta.

**Rubare**: come azione standard, sottrae un oggetto non impugnato né nascosto indicando prima la creatura e poi l'oggetto, con almeno una mano libera. Per le armi e gli oggetti impugnati serve Disarmare.

**Fintare**: prova di Raggirare contro la difesa dalla finta. Se riesce, il bersaglio perde il bonus di Destrezza contro il tuo prossimo attacco. Le varianti richiedono i talenti. Con due armi si sacrifica il primo attacco primario, a distanza si consuma un proiettile, gemella copre due bersagli vicini.

**Sporco trucco**: come azione standard applica accecato, abbagliato, assordato, intralciato, scosso o infermo per un numero di round pari al margine. Si rimuove solo l'effetto corrispondente con `.rimuovitrucco`, spendendo un'azione di movimento.

**Lotta**: con `.lotta` si inizia la presa come azione standard. Le creature umanoidi senza due mani libere subiscono penalità –4. Poi la si mantiene di round in round scegliendo ogni volta cosa farne. Si possono infliggere danni letali o non letali, immobilizzare, muovere entrambi oppure rilasciare con un'azione gratuita. Chi subisce tenta di liberarsi con BMC (`.lotta libera`), con Artista della Fuga (`.lotta fuga`) o di rovesciare i ruoli (`.lotta inverti`). Con una corda si lega (`.lotta lega`) e si scioglie (`.lotta sciogli`); un alleato vicino si aiuta con `.lotta aiuta`. In lotta servono due mani libere e le armi a due mani restano fuori.

**Stili del monaco**: Stile dello Scorpione e Pugno della Gorgone sono colpi senz'armi con effetti su velocità e condizione; Lancio Ki è uno sbilanciare senz'armi che sceglie la casella di arrivo. Botta Sbilanciante parte solo a colpo riuscito con Attacco Poderoso attivo.

**Movimento e attacchi speciali**: Acrobazia evita gli attacchi di opportunità muovendosi (veloce: movimento pieno, più difficile); Colpo Basso attraversa lo spazio di un avversario più grande; Giravolta Sbilanciante colpisce i nemici vicini col bastone ferrato a due mani; Attacco Rapido e Tiro in Movimento combinano spostamento e attacco in un'azione completa.

## Carica e rialzarsi

La **Carica** si avvia con `.caricare` sul nemico e procede in linea retta verso il bersaglio. Le varianti sono `prossimo` per preparare la prossima, `annulla` per interrompere, `impetuosa` e `radiosa` da talenti, `passaggio` per proseguire oltre il bersaglio con Attacco in sella. Chi finisce prono si rialza con `.alzati` oppure con un tentativo automatico dopo un round, un secondo con Rialzarsi, subendo gli attacchi di opportunità di chi minaccia.

## Talenti che contano

Ogni manovra ha il suo talento **Migliorato**, che evita l'attacco di opportunità del tentativo. **Lottare Migliorato** apre la lotta senza rischi, **Lottare Superiore** permette di mantenere spendendo il movimento. I talenti di stile (Scorpione, Gorgone, Lancio Ki, Botta Sbilanciante) sbloccano le rispettive opzioni; Fintare Migliorato rende la finta con il movimento.
