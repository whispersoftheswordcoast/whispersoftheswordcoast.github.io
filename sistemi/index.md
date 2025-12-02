---
title: Indice generale
layout: sistemi
permalink: /sistemi/
order: 1
---
<img src="{{ '/assets/images/cogs.png' | relative_url }}" alt="riposo" style="display: block; margin: 0 auto;" />

# Indice generale

{% assign pages_sistemi = site.pages | where_exp: "p", "p.path contains 'sistemi/'" %}
{% assign pages_ordered = pages_sistemi | sort: "order" %}

{% assign last_group = "" %}

{% for p in pages_ordered %}
  {% assign idx = p.order | default: 9999 %}

  {% if idx == 1 %}
    {% assign group = "Prefazione" %}
  {% elsif idx >= 2 and idx <= 99 %}
    {% assign group = "Meccaniche" %}
  {% elsif idx >= 100 and idx <= 199 %}
    {% assign group = "Sistemi di ruolo" %}
  {% else %}
    {% assign group = "Guide varie" %}
  {% endif %}

  {% if group != last_group %}
  
## {{ group }}

{% assign last_group = group %}
  {% endif %}

- [{{ p.title | default: p.name }}]({{ p.url }})

{% endfor %}
