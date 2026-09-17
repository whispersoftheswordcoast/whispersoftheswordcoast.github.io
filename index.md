---
layout: default

title: Whispers of the Sword Coast, Server Ultima Online Full GDR D&D Italiano

excerpt: WOTSC è un server roleplay ambientato nelle Terre Centrali Occidentali dei Forgotten Realms, basato su una versione moderna e pesantemente modificata di Ultima Online con regole Pathfinder 1e.
---

# Chi siamo

<img src="{{ '/assets/images/party.jpg' | relative_url }}" alt="eroi nuovi" style="display: block; margin: 0 auto;" />

**Whispers of the Sword Coast** è un server MMORPG basato sul gioco di ruolo **sempre nel personaggio**, su trame curate e sulla voglia di ricreare e vivere un bellissimo mondo fantasy, ispirato ai meravigliosi manuali di seconda edizione dedicati alle **Terre dell'Intrigo** e alle **Terre Centrali Occidentali**, casa della celebre **Baldur's Gate**.

## Lo stile

Il nostro desiderio è unire la **profondità di un play by chat** a un mondo sempre vivo e dinamico, dove le avventure non aspettano in un menu, ma sono da raggiungere insieme ai propri compagni, viaggiando attraverso il mondo di gioco.

**Sempre in ruolo**, tessendo le proprie storie in un contesto che vuole fieramente andare oltre il semplice *"Ciao Messere"*, le quest generiche e il PvP mascherato da gioco profondo.

Ogni cosa ha una causa, una conseguenza ed è parte di una **storia condivisa**, che i giocatori costruiscono e scrivono insieme.

## Il gioco

Il gioco è un raffinato **indie sandbox MMORPG**, basato su una versione pesantemente modificata di **Ultima Online**, adattata per ospitare le regole core di **Pathfinder 1e** e trasformarle in un'esperienza completamente in tempo reale.

Molte classi base e di prestigio, sistemi di multiclasse, centinaia di talenti, abilità e magie, accompagnati da una serie di sistemi custom, garantiscono una grande libertà nella costruzione del proprio personaggio e permettono di interpretare praticamente qualsiasi ruolo.

## Il mondo

<div class="wotsc-simple-gallery">

    <button onclick="this.parentElement.querySelector('.wotsc-gallery-scroll').scrollBy({left: -615, behavior: 'smooth'})">
        &#10094;
    </button>

    <div class="wotsc-gallery-scroll">

        <div class="wotsc-gallery-item">
            <img src="{{ '/assets/images/terrecentrali8.webp' | relative_url }}" alt="Baldur's Gate">

            <div class="wotsc-gallery-caption">
                <strong>Baldur's Gate</strong>
                La città del commercio e dell'avventura.
            </div>
        </div>

        <div class="wotsc-gallery-item">
            <img src="{{ '/assets/images/athkatlapromenade.jpg' | relative_url }}" alt="Athkatla">

            <div class="wotsc-gallery-caption">
                <strong>Athkatla</strong>
                La grande capitale dell'Amn.
            </div>
        </div>

        <div class="wotsc-gallery-item">
            <img src="{{ '/assets/images/picchi1.jpg' | relative_url }}" alt="Picchi delle Nuvole">

            <div class="wotsc-gallery-caption">
                <strong>Picchi delle Nuvole</strong>
                Le montagne che dominano le Terre Centrali Occidentali.
            </div>
        </div>

        <div class="wotsc-gallery-item">
            <img src="{{ '/assets/images/darkhold.jpg' | relative_url }}" alt="Colline dei Troll">

            <div class="wotsc-gallery-caption">
                <strong>Darkhold</strong>
                La tetra Darkhold.
            </div>
        </div>

    </div>

    <button onclick="this.parentElement.querySelector('.wotsc-gallery-scroll').scrollBy({left: 615, behavior: 'smooth'})">
        &#10095;
    </button>

</div>

La trasposizione delle **Terre Centrali Occidentali** è stata realizzata con una cura quasi maniacale: l'obiettivo è rendere ogni schermata **unica, riconoscibile e caratteristica**.

Ogni luogo, pianura, fiume, lago e montagna ha un nome. Poco o nulla è lasciato al generico, perché vogliamo che il mondo abbia carattere, identità e una propria storia.

**Baldur's Gate, Athkatla, i Picchi delle Nuvole, le Colline dei Troll** e molte altre regioni: ogni area è radicata nell'ambientazione e curata nei dettagli per costruire un mondo nel quale sia piacevole perdersi.

## Client moderno e customizzato

**Ultima Online è soltanto la base.**

Attraverso una profonda personalizzazione di **ClassicUO**, possiamo modellare l'esperienza visiva e funzionale del client per avvicinarla sempre di più alla nostra idea di mondo.

Rispetto all'esperienza tipica di Ultima Online, proponiamo numerose migliorie: **supporto alle razze di taglia piccola, fogliame animato, illuminazione avanzata** e molto altro ancora.

## I sistemi personalizzati

La nostra attenzione verso l'esperienza di gioco ci porta a creare e proporre **sistemi nuovi e fuori dagli schemi**, lontani dalle logiche più consuete degli MMORPG.

Ci piace osare, sperimentare e costruire nel tempo un universo di gioco sempre più stimolante, coerente e pulito.

Tra i sistemi sviluppati troviamo un **bestiario personale con oltre 700 voci collezionabili**, un **Craftbook** che permette di raccogliere e conservare progressi lavorativi e ricette, e un sistema di **crafting personalizzato** basato su avanzamenti iterativi.

Il mondo supporta inoltre lo **spawn casuale dei mostri**, per rendere le sfide meno prevedibili, un sistema di **housing automatizzato** che permette di acquistare e vendere edifici direttamente in gioco, la **personalizzazione delle skin facciali**, schede personali rivisitate con supporto alla personalizzazione di **ritratti e descrizioni**, **intelligenze artificiali avanzate per le boss fight** e molto altro.

## Inizia la tua avventura

Se quello che cerchi è un mondo in cui il personaggio non sia soltanto un avatar, ma il protagonista di una storia costruita insieme agli altri giocatori, **Whispers of the Sword Coast ti aspetta.**

- [Come giocare](/come-giocare/)
- [Regolamento](/regolamento/)
- [Ambientazione](/ambientazione/)
- [Classi e Razze](/classi-e-razze/)
- [Download client](/download/)
- [Manuale di gioco](/manuale/)

<!-- DI SEGUITO IL SUPPORTO ALLE ANTEPRIME, COPIABILE -->

<div id="wotsc-lightbox" class="wotsc-lightbox">
    <span class="wotsc-lightbox-close">&times;</span>
    <img id="wotsc-lightbox-image" src="" alt="">
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {

    const lightbox = document.getElementById('wotsc-lightbox');
    const lightboxImage = document.getElementById('wotsc-lightbox-image');
    const closeButton = document.querySelector('.wotsc-lightbox-close');

    document.querySelectorAll('.wotsc-gallery-item img').forEach(function (image) {

        image.addEventListener('click', function () {
            lightboxImage.src = this.src;
            lightboxImage.alt = this.alt;

            lightbox.classList.add('active');
        });

    });

    closeButton.addEventListener('click', function () {
        lightbox.classList.remove('active');
    });

    lightbox.addEventListener('click', function (event) {
        if (event.target === lightbox) {
            lightbox.classList.remove('active');
        }
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            lightbox.classList.remove('active');
        }
    });

});
</script>

