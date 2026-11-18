---
layout: post
title: "Nuove classi, magie, menu a rondella e traduzione multilingue"
date: 2026-11-18
excerpt: "Quattro nuove classi Pathfinder, parco incantesimi aggiornato, menu a rondella personalizzabile e prime funzioni di traduzione multilingue."
categories: [patch, aggiornamenti, classi, sistemi]
---

Questa settimana abbiamo parecchie cose da raccontarvi. Sono stati giorni di lavoro piuttosto intensi, con interventi che toccano aspetti molto diversi dello shard: dalla progressione dei personaggi alla gestione delle magie, passando per alcune novità del client e nuovi strumenti che speriamo possano aiutarci a crescere.

Alcune di queste aggiunte sono già pronte per essere utilizzate, altre sono ancora in fase di sperimentazione e avranno bisogno di un po' di tempo per essere messe a punto. Ma andiamo con ordine.

## Quattro nuove classi Pathfinder

Partiamo da una delle aggiunte più consistenti sul fronte delle classi: sono state introdotte quattro nuove classi ispirate a Pathfinder, ovvero Pistolero, Fattucchiere, Oracolo e Alchimista.

Si tratta di un primo rilascio, ancora in fase di test e affinamento. Ci sarà quindi bisogno di verificare il comportamento delle nuove classi sul campo e intervenire dove necessario, ma da oggi sono disponibili per chi vorrà iniziare a sperimentarle.

## Il nuovo parco incantesimi Pathfinder

Questo è probabilmente uno degli interventi più importanti di questa tornata di aggiornamenti, anche perché non riguarda soltanto chi deve ancora creare un personaggio, ma coinvolge direttamente chi gioca già da tempo.

È stato completato il lavoro di aggiornamento del parco incantesimi a Pathfinder, un intervento piuttosto ampio che porta con sé una revisione delle magie e delle relative implementazioni.

Anche i menu di consultazione sono stati completamente rifatti, passando a una nuova interfaccia HTML. Abbiamo introdotto una distinzione cromatica che sarà importante tenere presente:

Le magie in arancione sono quelle nuove, oppure quelle che hanno subito modifiche e devono ancora essere provate, verificate e perfezionate. Quelle che mantengono la normale colorazione sono invece già state controllate e considerate a posto.

In questo modo sarà più semplice distinguere ciò che è già consolidato da ciò che necessita ancora di qualche attenzione. Vi chiediamo quindi di prestare particolare attenzione alle voci arancioni e di segnalarci eventuali anomalie: il contributo di chi utilizza quotidianamente queste magie sarà fondamentale per completare il lavoro.

<img src="{{ '/assets/images/magiearancioni.webp' | relative_url }}" alt="Le magie nuove e modificate in arancione" style="display: block; margin: 0 auto;" />

## Un nuovo menu a rondella personalizzabile

Passiamo a qualcosa che riguarda più direttamente il modo di giocare.

È stato aggiunto il nuovo menu a rondella personalizzabile, con cinque preset già pronti da utilizzare. L'obiettivo è rendere più immediato l'accesso alle varie funzioni, lasciando allo stesso tempo la possibilità di organizzare il menu secondo le proprie abitudini.

È una di quelle modifiche che si apprezzano soprattutto utilizzando il client, e che speriamo possa rendere un po' più comoda la gestione delle tante funzioni ormai presenti.

<img src="{{ '/assets/images/clientrotella.webp' | relative_url }}" alt="Il menu a rondella personalizzabile" style="display: block; margin: 0 auto;" />

## Traduzione multilingue e parlato dei PNG: proviamo ad aprirci al mondo

Questa è forse la novità che guardiamo con maggiore curiosità per quello che potrebbe rappresentare in prospettiva.

Sono state introdotte le prime funzioni per la traduzione multilingue e per la gestione del parlato in PNG. L'idea alla base è abbastanza semplice: provare a rendere il nostro shard accessibile anche a giocatori che non parlano italiano, aprendoci così alla possibilità di incontrare nuove persone e, perché no, di allargare la nostra piccola comunità.

Dopotutto, uno degli aspetti più belli di questa esperienza è proprio poterla condividere con altri giocatori. Avere la possibilità di farlo con persone provenienti da altre parti del mondo potrebbe offrirci nuove occasioni di gioco, nuove interazioni e nuove storie da vivere insieme.

### Come provare le nuove funzioni

Per utilizzare queste funzionalità è necessario disporre di un modello LLM, ovvero un modello linguistico che verrà scaricato e utilizzato direttamente dal proprio computer.

Nel client è ora presente un apposito menu dal quale scegliere e scaricare i modelli disponibili. Per ciascuno viene indicato anche lo spazio di memoria RAM richiesto, un'informazione importante da tenere presente prima di procedere.

Il sistema è già in grado di riconoscere le risorse hardware disponibili, distinguendo tra CPU e GPU, e offre due modalità di gestione della memoria: automatica e manuale.

La modalità automatica cerca di sfruttare al massimo le risorse disponibili, riempiendo prima la memoria della GPU finché possibile e utilizzando poi la RAM di sistema per la parte restante, mantenendo comunque un piccolo buffer di memoria libero per evitare di saturare completamente le risorse del computer.

Chi preferisce avere un controllo maggiore può invece impostare manualmente quanta memoria dedicare alla GPU e quanta alla CPU.

Un consiglio: evitate, se possibile, di caricare tutto il modello sulla CPU. L'esecuzione in questo modo è decisamente più lenta. Per ottenere prestazioni migliori suggeriamo di provare a distribuire il carico tra GPU e CPU, indicativamente lasciando metà del modello sulla scheda video e metà sulla memoria di sistema, compatibilmente con le risorse del proprio PC.

Per chi possiede una scheda video NVIDIA sono inoltre disponibili appositi pacchetti per scaricare le librerie CUDA, che consentono di sfruttare l'accelerazione hardware e dovrebbero migliorare sensibilmente la velocità di esecuzione.

Per quanto riguarda i modelli, quello che consigliamo attualmente di provare è Rocinante, una versione basata su Mistral e sviluppata specificamente per l'interpretazione, la narrativa e il gioco di ruolo. È il modello che al momento riteniamo più interessante per questo tipo di utilizzo.

Naturalmente, prima di scegliere un modello, è bene verificare che le risorse indicate siano compatibili con quelle del proprio computer. Se un modello non può essere caricato rispettando i limiti di memoria impostati, non sarà possibile selezionarlo.

### Una precisazione sullo stato dei lavori

Siamo ancora in una fase sperimentale. Le funzioni sono già utilizzabili da chiunque voglia provarle, ma richiedono ancora parecchio lavoro e qualche compromesso: non tutto funzionerà sempre alla perfezione e bisognerà avere un po' di pazienza davanti ad alcuni errori o imprecisioni.

Preferiamo comunque renderle disponibili fin da subito, così da poterle mettere alla prova anche nell'utilizzo quotidiano, raccogliendo impressioni e segnalazioni mentre continuiamo a lavorarci.

È un primo passo che ci tenevamo a compiere, e che speriamo possa aprire qualche nuova strada per il futuro dello shard.

<img src="{{ '/assets/images/clientllm.webp' | relative_url }}" alt="Il parlato dei PNG tradotto" style="display: block; margin: 0 auto;" />

## E infine, qualche lavoro dietro le quinte

Non tutto quello che arriva con un aggiornamento è necessariamente qualcosa che si vede subito.

Sono stati effettuati numerosi bugfix e diversi interventi di aggiornamento e revisione del codice, con l'obiettivo di correggere problematiche esistenti e continuare a mantenere in ordine i sistemi già presenti.

Tra le aggiunte più concrete c'è anche la possibilità di ruotare una ventina di nuovi mobili, ampliando ulteriormente le possibilità di arredamento e personalizzazione delle abitazioni.

Sono interventi magari meno appariscenti rispetto alle nuove classi o alle magie, ma che contribuiscono comunque a rendere il mondo di gioco sempre più ricco e curato.

Come sempre, soprattutto per le funzionalità ancora in fase di test, ogni segnalazione e ogni prova sul campo saranno preziose. Abbiamo parecchio lavoro alle spalle, ma anche ancora tante cose da perfezionare.

Buon gioco a tutti!
