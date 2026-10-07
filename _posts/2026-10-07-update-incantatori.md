---
layout: post
title: "Stirpi, scuole di magia e canti: update incantatori"
date: 2026-10-07
excerpt: "Stregone, mago e bardo allineati alle regole Pathfinder: stirpi con poteri e talento bonus, scuole di magia, famiglio, canzoni del bardo, nuovi comandi, mappe delle Colline Lontane e nuove guide."
categories: [patch, aggiornamenti, classi, magia]
---

# Stirpi, scuole e canti

Con questo aggiornamento, **stregone, mago e bardo** vengono allineati alle regole Pathfinder: progressioni, poteri e meccaniche seguono d'ora in poi il regolamento di riferimento. Completano la patch nuovi comandi, le mappe aggiornate delle Colline Lontane e quattro nuove guide sul sito.

---

## Stregone: le stirpi

Lo **[stregone](/classi/stregone/)** sceglie una volta per tutte la propria **stirpe**, ossia l'origine del suo potere innato: sangue draconico, infernale, celestiale, fatato o altro ancora. La scelta avviene da menu dedicato, con conferma, ed è permanente. Ogni stirpe conferisce poteri tematici con usi giornalieri (`.poterestirpe [potere]`), resistenze, un **talento bonus al 7° livello** e cinque incantesimi bonus al 3°, 5°, 7°, 9° e 11° livello. La stirpe draconica prevede anche la scelta del drago tra dieci tipi. Il famiglio si gestisce da `.poterestirpe famiglio`, con richiamo tramite `.compagni`. Dettagli nella guida alle [stirpi](/sistemi/stirpi/).

<img src="{{ '/assets/images/stirpe.webp' | relative_url }}" alt="stirpi dello stregone" style="display: block; margin: 0 auto;" />

<img src="{{ '/assets/images/stirpemenu.webp' | relative_url }}" alt="menu scelta stirpe" style="display: block; margin: 0 auto;" />

## Mago: le scuole

Il **[mago](/classi/mago/)** sceglie la propria **scuola** tra Abiurazione, Ammaliamento, Divinazione, Evocazione, Illusione, Invocazione, Necromanzia e Trasmutazione, con migrazione automatica per i maghi esistenti. Lo specialista sacrifica due scuole opposte, le cui magie costano il doppio degli slot, e riceve in cambio uno slot vincolato per ogni cerchio. Senza scelta completata tramite `.poterescuola`, il riposo non ricostruisce le preparazioni. Ogni scuola conferisce un potere di 1° livello (3 utilizzi giornalieri più il modificatore di Intelligenza) e uno di 8° (durata in round pari al livello). Dettagli nella guida alle [scuole di magia](/sistemi/scuole/).

Rinnovato anche il **famiglio**: quattordici specie, ciascuna col proprio bonus, rituale di legame di 8 ore con `.sceglifamiglio`, richiamo con `.evocafamiglio` e riparo con `.portafamiglio`. Trasmette incantesimi a contatto, condivide le magie del padrone e può essere interrogato; in caso di morte, servono 168 ore di mondo prima di legarne uno nuovo.

<img src="{{ '/assets/images/scuole-magia.webp' | relative_url }}" alt="scuole di magia" style="display: block; margin: 0 auto;" />

Tra i talenti arriva **esplosione arcana** (`.esplosionearcana`): richiede una classe arcana da incantatore di livello 10 e consuma un incantesimo preparato oppure uno slot di livello da 1 a 9.

## Bardo: le canzoni

Le **canzoni del [bardo](/classi/bardo/)** tornano con `.canzonebardo`: riserva di punti pari a 4 più Carisma più 2 per livello oltre il primo, attivazione con azione standard (di movimento dal 7°) e mantenimento gratuito ogni round. Il repertorio comprende Ispirare Coraggio, Controcanto e Distrazione senza costo, quindi Affascinare, Competenza, Maestro del Sapere, Suggestione, Terrore e Grandezza, fino a Musica Lenitiva e Canto di Libertà al 12° livello. Con l'Esecuzione Versatile, il bonus di Intrattenere sostituisce a scelta altre abilità; con `.suona` e `.oratore` si alternano esecuzione strumentale e oratoria.

## Compagni: menu e nuove specie

Migliorato il **menu di scelta dei compagni** e ampliate le **specie selezionabili** per druidi e ranger, ora **118** in tutto. L'elenco completo con dati e progressione è nella guida al [compagno animale](/sistemi/compagni/).

<img src="{{ '/assets/images/compagni0003.webp' | relative_url }}" alt="scelta del compagno animale" style="display: block; margin: 0 auto;" />

## Nuovi comandi

Tra i comandi di nuova introduzione figura `.schedaabilita`: la scheda delle abilità consultabile con ritratto, consapevole di classi e domini. Arrivano anche i poteri di dominio `.armadanzante`, `.ragnatela` e `.unitafamiglia`. Gli altri interventi del periodo riguardano sistemi già annunciati in precedenza.

<img src="{{ '/assets/images/schedabilita.webp' | relative_url }}" alt="scheda delle abilità" style="display: block; margin: 0 auto;" />

## Mappe: Colline Lontane e Darkhold

Portati avanti i lavori sulle **Colline Lontane** e sul **bosco di Reaching**, collegando così la zona di **Darkhold** al resto della mappa. Predisposta per il futuro anche la zona di **Iriaebor**, che verrà edificata in un secondo momento. Riscaricate i file di gioco per esplorare le nuove aree.

<img src="{{ '/assets/images/farhills01.webp' | relative_url }}" alt="Colline Lontane" style="display: block; margin: 0 auto;" />

<img src="{{ '/assets/images/reachingwoods01.webp' | relative_url }}" alt="boschi delle Colline Lontane" style="display: block; margin: 0 auto;" />

## Guide aggiunte

Sul sito sono disponibili quattro nuove guide: il **[compagno animale](/sistemi/compagni/)**, gli **[allineamenti](/sistemi/allineamenti/)**, i **[domini](/sistemi/domini/)** e i **[racconti dal forum](/racconti/)**, questi ultimi con navigazione dedicata e aggiornamento automatico.
