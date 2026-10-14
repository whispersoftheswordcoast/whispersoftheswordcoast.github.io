---
layout: post
title: "Nuovo client avanzato: effetti migliori"
date: 2026-10-14
excerpt: "Finalmente disponibile un nuovo client avanzato con supporto per effetti migliori: ecco cosa cambia e come aggiornare."
categories: [patch, aggiornamenti, client]
---

È finalmente disponibile un nuovo client avanzato con supporto per effetti migliori. Questa pagina raccoglie cosa cambia e come aggiornare: le immagini del prima/dopo e i dettagli seguiranno qui sotto.

## Rive più morbide

Il rendering dell'acqua è stato corretto: le rive ora degradano in modo morbido invece di staccarsi a spigoli netti.

<div style="display: flex; gap: 1rem; margin: 1rem 0;">

    <figure style="flex: 1; margin: 0; text-align: center;">
        <img src="{{ '/assets/images/rive-prima.webp' | relative_url }}" alt="Rive prima della correzione" style="width: 100%; aspect-ratio: 1.44; object-fit: cover;" />
        <figcaption><strong>Prima</strong></figcaption>
    </figure>

    <figure style="flex: 1; margin: 0; text-align: center;">
        <img src="{{ '/assets/images/rive-dopo.webp' | relative_url }}" alt="Rive dopo la correzione" style="width: 100%; aspect-ratio: 1.44; object-fit: cover;" />
        <figcaption><strong>Dopo</strong></figcaption>
    </figure>

</div>

## Effetti acqua avanzati

Con il nuovo client l'acqua si muove: increspature e riflessi animati danno vita a fiumi, laghi e coste.

<video autoplay muted loop playsinline
       style="display: block; margin: 20px auto; max-width: 100%; width: 600px;">
  <source src="{{ '/assets/images/water.mp4' | relative_url }}" type="video/mp4">
</video>

## Erba animata

Con il nuovo client anche l'erba si muove al vento, con movimento e collisione al passaggio di personaggi e mostri.

<div style="display: flex; gap: 1rem; margin: 1rem 0;">

    <figure style="flex: 1; margin: 0; text-align: center;">
        <img src="{{ '/assets/images/erba-prima.webp' | relative_url }}" alt="Erba ferma prima" style="width: 100%; aspect-ratio: 1.31; object-fit: cover;" />
        <figcaption><strong>Prima</strong></figcaption>
    </figure>

    <figure style="flex: 1; margin: 0; text-align: center;">
        <video autoplay muted loop playsinline style="width: 100%; aspect-ratio: 1.31; object-fit: cover;">
            <source src="{{ '/assets/images/erba-dopo.mp4' | relative_url }}" type="video/mp4">
        </video>
        <figcaption><strong>Dopo</strong></figcaption>
    </figure>

</div>

## Lava animata

Con il nuovo client anche la lava scorre animata, con colate e cascate incandescenti.

<div style="display: flex; gap: 1rem; margin: 1rem 0;">

    <figure style="flex: 1; margin: 0; text-align: center;">
        <video autoplay muted loop playsinline style="width: 100%; aspect-ratio: 1.27; object-fit: cover;">
            <source src="{{ '/assets/images/lava-prima.mp4' | relative_url }}" type="video/mp4">
        </video>
        <figcaption><strong>Prima</strong></figcaption>
    </figure>

    <figure style="flex: 1; margin: 0; text-align: center;">
        <video autoplay muted loop playsinline style="width: 100%; aspect-ratio: 1.27; object-fit: cover;">
            <source src="{{ '/assets/images/lava-dopo.mp4' | relative_url }}" type="video/mp4">
        </video>
        <figcaption><strong>Dopo</strong></figcaption>
    </figure>

</div>

## I profili tra cui scegliere

<img src="{{ '/assets/images/client.JPG' | relative_url }}" alt="Selezione del profilo nel client" style="display: block; margin: 0 auto;" />

**Basic** (coincide con Default) è il profilo predefinito: include il fix della riva e alcuni fix minori alle animazioni.

**Advanced (Base)** è ottimo con macchine meno potenti. Nel dubbio lo si può testare attivando e disattivando gli shader base e attendendo qualche secondo.

**Advanced (High)** è studiato per avere meno chiamate ed essere più veloce su macchine potenti.

**Advanced (Experimental)** in teoria è il più veloce di tutti, ma non è testato.

Nota bene: sia AdvancedHighEnd che AdvancedLowEnd hanno comunque una penalità a livello di FPS anche a effetti spenti. Se gli upgrade grafici non vi interessano, restate pure sul Base.

### Opzioni di ottimizzazione

<img src="{{ '/assets/images/ottimizzazione.webp' | relative_url }}" alt="Opzioni di ottimizzazione" style="display: block; margin: 0 auto;" />

Gestiscono una generazione più lenta dei blocchi di mondo, prevenendo lo stuttering con la maggior parte delle macchine.

La prima opzione spalma le operazioni su più frame quando un grosso aggiornamento è in arrivo, rendendo morbida la transizione. La seconda rallenta l'upload degli asset distanti. La terza opzione ignora questi due limiti temporaneamente in caso di teletrasporti e simili. L'ultima disabilita gli shader semplici, cosa che può migliorare il gioco con macchine potenti.

### Dettagli Customizzabili

<img src="{{ '/assets/images/customize.webp' | relative_url }}" alt="Dettagli personalizzabili degli effetti" style="display: block; margin: 0 auto;" />

Si possono customizzare a preferenza aspetto di lava, acqua e steli d'erba, con molte voci con cui sbizzarrirsi.

## Showcase

Il nuovo client nei territori del Faerûn occidentale.

<div class="wotsc-viewer">

    <button class="wotsc-viewer-prev" aria-label="Immagine precedente">&#10094;</button>

    <figure class="wotsc-viewer-item active">
        <img src="{{ '/assets/images/vista-1.webp' | relative_url }}" alt="Fiume nella foresta">
        <figcaption><strong>Il fiume nella foresta</strong>Acqua, rive ed erba col nuovo rendering.</figcaption>
    </figure>

    <figure class="wotsc-viewer-item">
        <img src="{{ '/assets/images/vista-2.webp' | relative_url }}" alt="Costa desertica">
        <figcaption><strong>La costa desertica</strong>Palme, sabbia e mare animato.</figcaption>
    </figure>

    <figure class="wotsc-viewer-item">
        <img src="{{ '/assets/images/vista-3.webp' | relative_url }}" alt="Fortilizi nel bosco autunnale">
        <figcaption><strong>Fortilizi nel bosco</strong>Palizzate tra gli aceri d'autunno.</figcaption>
    </figure>

    <button class="wotsc-viewer-next" aria-label="Immagine successiva">&#10095;</button>

    <div class="wotsc-viewer-count">1 / 3</div>

</div>

## Come aggiornare

Non serve altro: basta aggiornare il gioco per avere tutta la nuova roba. Avviate il launcher e lasciatelo allineare: rispondete sì e siete pronti. In alternativa, la pagina [Download](/download/) resta sempre aggiornata.

## Note finali

<!-- TODO: note finali (da dettare) -->
