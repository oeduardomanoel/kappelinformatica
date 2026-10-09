#!/usr/bin/env python3
"""Gera o site estático da Kappel Informática.

Uso:  python3 scripts/build.py
Tudo que muda com frequência (domínio, contato, PCs à venda, FAQ) fica nas
constantes abaixo. Rode o script de novo depois de editar e faça o deploy da
pasta raiz do repositório.
"""
import json
import os
from datetime import date
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- dados
SITE = "https://www.kappelinformatica.com.br"  # TODO: confirmar domínio definitivo
NAME = "Kappel Informática & Tecnologia"
SHORT = "Kappel Informática"
WHATS = "5547989289589"
PHONE_DISPLAY = "(47) 98928-9589"
PHONE_INTL = "+55-47-98928-9589"
EMAIL = "kappelinformatica@gmail.com"
INSTAGRAM = "https://www.instagram.com/kappelinformatica/"
FACEBOOK = "https://www.facebook.com/61590926625800/"
STREET = "R. São Paulo, 227"
CITY = "Tijucas"
STATE = "SC"
CEP = "88200-000"
MAPS = "https://www.google.com/maps/search/?api=1&query=" + quote("Kappel Informática R. São Paulo 227 Tijucas SC")
CITIES = ["Tijucas", "Canelinha", "São João Batista", "Porto Belo", "Itapema", "Governador Celso Ramos", "Biguaçu"]
TODAY = date.today().isoformat()

# PCs à venda: edite aqui quando o estoque mudar
PCS = [
    {
        "id": "ryzen7-5700-rtx3060-12gb",
        "name": "Ryzen 7 5700 + RTX 3060 12GB",
        "cpu": "AMD Ryzen 7 5700",
        "gpu": "RTX 3060 12 GB",
        "price": 3990,
    },
    {
        "id": "ryzen7-5700-rtx3060ti-8gb",
        "name": "Ryzen 7 5700 + RTX 3060 Ti 8GB",
        "cpu": "AMD Ryzen 7 5700",
        "gpu": "RTX 3060 Ti 8 GB",
        "price": 3890,
    },
]


def wa(text):
    return "https://wa.me/%s?text=%s" % (WHATS, quote(text))


def brl(v):
    return "R$ " + "{:,.0f}".format(v).replace(",", ".")


# ---------------------------------------------------------------- ícones
ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
<symbol id="i-zap" viewBox="0 0 24 24"><path d="M12 2.8a9.2 9.2 0 0 0-7.9 13.9L2.8 21.2l4.6-1.2A9.2 9.2 0 1 0 12 2.8z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8.9 7.9c.2-.4.5-.5.8-.5h.6c.2 0 .4.1.5.4l.8 1.8c.1.2 0 .5-.1.7l-.6.7c.7 1.3 1.7 2.3 3 3l.7-.6c.2-.2.5-.2.7-.1l1.8.8c.3.1.4.3.4.5v.6c0 .3-.1.6-.5.8-.7.5-1.7.6-2.6.3a8.2 8.2 0 0 1-5.4-5.4c-.3-.9-.2-1.9.3-2.6z" fill="currentColor"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></g></symbol>
<symbol id="i-truck" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M2.5 6.5h11v9h-11zM13.5 9.5h4l3 3v3h-7z"/><circle cx="6.5" cy="17" r="1.8"/><circle cx="17" cy="17" r="1.8"/></g></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M12 2.8 4.5 5.6v6c0 4.6 3.2 8.2 7.5 9.6 4.3-1.4 7.5-5 7.5-9.6v-6z"/><path d="m8.7 12 2.3 2.3 4.3-4.6"/></g></symbol>
<symbol id="i-receipt" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M5.5 2.8h13v18.4l-2.2-1.4-2.1 1.4-2.2-1.4-2.2 1.4-2.1-1.4-2.2 1.4z"/><path d="M8.5 7.5h7M8.5 11h7M8.5 14.5h4"/></g></symbol>
<symbol id="i-card" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><rect x="2.8" y="5.5" width="18.4" height="13" rx="2"/><path d="M2.8 9.5h18.4M6.5 15h4"/></g></symbol>
<symbol id="i-laptop" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><rect x="4.5" y="5" width="15" height="10" rx="1.2"/><path d="M2 18.5h20l-1.5-3.5h-17z"/></g></symbol>
<symbol id="i-pad" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"><path d="M7 7.5h10a4.5 4.5 0 0 1 4.4 5.4l-.8 4a2.6 2.6 0 0 1-4.5 1.2L14.4 16H9.6l-1.7 2.1a2.6 2.6 0 0 1-4.5-1.2l-.8-4A4.5 4.5 0 0 1 7 7.5z"/><path d="M7.5 10.5v3M6 12h3"/><circle cx="16" cy="11" r=".6" fill="currentColor"/><circle cx="17.5" cy="13" r=".6" fill="currentColor"/></g></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"><rect x="6.5" y="2.5" width="11" height="19" rx="2.2"/><path d="M10.5 18.5h3M9 6l3.5 3.5M9 9.5l6 6"/></g></symbol>
<symbol id="i-tower" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"><rect x="6" y="2.5" width="12" height="19" rx="1.5"/><circle cx="12" cy="9" r="2.6"/><circle cx="12" cy="16" r="2.6"/></g></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8 12.2 2.8 2.8L16.2 9.5"/></g></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 2.5a7 7 0 0 0-7 7c0 5.2 7 12 7 12s7-6.8 7-12a7 7 0 0 0-7-7zm0 9.6a2.6 2.6 0 1 1 0-5.2 2.6 2.6 0 0 1 0 5.2z" fill="currentColor"/></symbol>
</svg>"""


def icon(name, cls=""):
    c = ' class="%s"' % cls if cls else ""
    return '<svg%s aria-hidden="true"><use href="#i-%s"/></svg>' % (c, name)


def btn_zap(label, text, extra=""):
    return '<a class="btn btn-zap %s" href="%s" target="_blank" rel="noopener">%s%s</a>' % (extra, wa(text), icon("zap"), label)


# ---------------------------------------------------------------- schema
BUSINESS_ID = SITE + "/#negocio"


def business_schema():
    return {
        "@type": ["ComputerStore", "LocalBusiness"],
        "@id": BUSINESS_ID,
        "name": NAME,
        "alternateName": [SHORT, "Kappel"],
        "description": "Assistência técnica multimarca de computador, notebook, videogame, controle e celular em Tijucas/SC, com busca e entrega do aparelho, atendimento 24 horas pelo WhatsApp e venda de PC Gamer montado com nota fiscal.",
        "url": SITE + "/",
        "logo": SITE + "/assets/img/logo-512.png",
        "image": SITE + "/assets/img/og-kappel.jpg",
        "telephone": PHONE_INTL,
        "email": EMAIL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STREET,
            "addressLocality": CITY,
            "addressRegion": STATE,
            "postalCode": CEP,
            "addressCountry": "BR",
        },
        "hasMap": MAPS,
        "areaServed": [{"@type": "City", "name": c + ", SC"} for c in CITIES],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59",
        }],
        "paymentAccepted": "Cartão de crédito, PIX, Dinheiro",
        "currenciesAccepted": "BRL",
        "priceRange": "$$",
        "sameAs": [INSTAGRAM, FACEBOOK],
        "knowsAbout": ["Conserto de computador", "Conserto de notebook", "Formatação", "Upgrade de SSD e memória RAM", "Troca de placa mãe", "Reparo em placa", "Conserto de videogame", "Conserto de controle", "Troca de tela de celular", "Montagem de PC Gamer"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Serviços e produtos",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s, "url": SITE + u}}
                for s, u in [
                    ("Conserto de computador e notebook", "/servicos/computador-e-notebook/"),
                    ("Conserto de videogame e controle", "/servicos/videogame-e-controle/"),
                    ("Troca de tela e conserto de celular", "/servicos/celular/"),
                    ("Assistência técnica para empresas", "/empresas/"),
                    ("PC Gamer montado com nota fiscal", "/pc-gamer/"),
                ]
            ],
        },
    }


def website_schema():
    return {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": SHORT, "inLanguage": "pt-BR", "publisher": {"@id": BUSINESS_ID}}


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
    ]}


def crumbs_schema(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)
    ]}


def service_schema(name, path, desc):
    return {"@type": "Service", "name": name, "serviceType": name, "description": desc, "url": SITE + path,
            "provider": {"@id": BUSINESS_ID},
            "areaServed": [{"@type": "City", "name": c + ", SC"} for c in CITIES]}


def product_schema(pc):
    return {"@type": "Product", "name": "PC Gamer " + pc["name"], "sku": pc["id"],
            "description": "PC Gamer montado com processador %s e placa de vídeo %s. Nota fiscal no nome do cliente, 3 meses de garantia e até 12x no cartão." % (pc["cpu"], pc["gpu"]),
            "image": SITE + "/assets/img/og-kappel.jpg",
            "brand": {"@type": "Brand", "name": SHORT},
            "offers": {"@type": "Offer", "price": str(pc["price"]), "priceCurrency": "BRL",
                       "availability": "https://schema.org/LimitedAvailability",
                       "itemCondition": "https://schema.org/NewCondition",
                       "url": SITE + "/pc-gamer/#" + pc["id"], "seller": {"@id": BUSINESS_ID}}}


def jsonld(nodes):
    data = {"@context": "https://schema.org", "@graph": nodes}
    return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False, separators=(",", ":"))


# ---------------------------------------------------------------- layout
NAV = [
    ("Serviços", "/#servicos"),
    ("PC Gamer", "/pc-gamer/"),
    ("Troca de usado", "/pc-gamer/#troca"),
    ("Empresas", "/empresas/"),
    ("Contato", "/#contato"),
]


def head(title, desc, path, schema_nodes, og_type="website"):
    url = SITE + path
    return """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0b0b0a">
<meta name="geo.region" content="BR-SC">
<meta name="geo.placename" content="Tijucas">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{name}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}/assets/img/og-kappel.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Kappel Informática & Tecnologia, assistência técnica em Tijucas SC">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/assets/img/og-kappel.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/anton.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/sora-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
{schema}
<!--
  GA4: troque G-XXXXXXXXXX pelo ID real e descomente.
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
  Meta Pixel: cole aqui o código do Gerenciador de Eventos.
-->
</head>
<body>
{icons}
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
""".format(title=title, desc=desc, url=url, og_type=og_type, name=NAME, site=SITE, schema=jsonld(schema_nodes), icons=ICONS)


def header(active=""):
    items = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (u, ' aria-current="page"' if u == active else "", n) for n, u in NAV
    )
    return """<header class="site-header">
  <nav class="wrap nav" aria-label="Principal">
    <a class="brand" href="/" aria-label="Kappel Informática, página inicial">
      <img src="/assets/img/logo.svg" alt="" width="40" height="40">
      <span class="brand-name"><b>KAPPEL</b><small>Informática &amp; Tecnologia</small></span>
    </a>
    <div class="nav-links" id="nav-links"><ul class="menu">{items}</ul></div>
    {cta}
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Abrir menu"><span></span></button>
  </nav>
</header>
<main id="conteudo">
""".format(items=items, cta=btn_zap("Orçamento", "Oi, Kappel! Quero fazer um orçamento."))


def footer():
    cities = ", ".join(CITIES[:-1]) + " e " + CITIES[-1]
    return """</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot">
      <div class="foot-brand">
        <a class="brand" href="/"><img src="/assets/img/logo.svg" alt="" width="40" height="40"><span class="brand-name"><b>KAPPEL</b><small>Informática &amp; Tecnologia</small></span></a>
        <p>Assistência técnica de computador, notebook, videogame e celular em Tijucas/SC. Atendemos {cities}.</p>
      </div>
      <div>
        <h2>Serviços</h2>
        <ul>
          <li><a href="/servicos/computador-e-notebook/">Computador e notebook</a></li>
          <li><a href="/servicos/videogame-e-controle/">Videogame e controle</a></li>
          <li><a href="/servicos/celular/">Celular</a></li>
          <li><a href="/empresas/">Para empresas</a></li>
        </ul>
      </div>
      <div>
        <h2>Loja</h2>
        <ul>
          <li><a href="/pc-gamer/">PC Gamer</a></li>
          <li><a href="/pc-gamer/#troca">Troca de usado</a></li>
          <li><a href="/#faq">Perguntas frequentes</a></li>
        </ul>
      </div>
      <div>
        <h2>Contato</h2>
        <ul>
          <li><a href="{wa}" target="_blank" rel="noopener">WhatsApp {phone}</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
          <li><a href="{ig}" target="_blank" rel="noopener">Instagram @kappelinformatica</a></li>
          <li><a href="{maps}" target="_blank" rel="noopener">{street}, {city}/{state}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© <span id="ano">{year}</span> {name}. Tijucas/SC.</span>
      <!-- TODO: incluir CNPJ quando o cliente enviar -->
      <span>Atendimento 24 horas pelo WhatsApp</span>
    </div>
  </div>
</footer>
<a class="zap-float" href="{wa}" target="_blank" rel="noopener" aria-label="Chamar a Kappel no WhatsApp">{zap}<span>Chamar no WhatsApp</span></a>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
""".format(cities=cities, wa=wa("Oi, Kappel! Vim pelo site e quero um orçamento."), phone=PHONE_DISPLAY, email=EMAIL,
           ig=INSTAGRAM, maps=MAPS, street=STREET, city=CITY, state=STATE, year=date.today().year, name=NAME, zap=icon("zap"))


# ---------------------------------------------------------------- blocos reutilizáveis
def seals():
    rows = [
        ("clock", "Atendimento 24h", "Chamou no WhatsApp, a gente responde"),
        ("truck", "Buscamos e levamos", "Seu aparelho, onde você estiver"),
        ("shield", "Serviço com garantia", "PC montado sai com 3 meses"),
        ("receipt", "Nota fiscal no seu nome", "Compra registrada, sem dor de cabeça"),
        ("card", "Até 12x no cartão", "Ou PIX e dinheiro"),
    ]
    lis = "".join('<li>%s<div><b>%s</b><span>%s</span></div></li>' % (icon(i), b, s) for i, b, s in rows)
    return '<section class="seals" aria-label="Por que chamar a Kappel"><div class="wrap"><ul>%s</ul></div></section>' % lis


def rig():
    return """<div class="rig" role="img" aria-label="Ilustração de um PC gamer com iluminação RGB">
  <div class="rig-case">
    <div class="rig-glass"></div>
    <div class="rig-board"></div>
    <div class="rig-cpu"></div>
    <div class="rig-ram"><i></i><i></i><i></i></div>
    <div class="rig-gpu"><span>GPU · 12 GB</span></div>
    <div class="rig-psu"></div>
    <div class="rig-fans"><div class="fan"></div><div class="fan"></div><div class="fan"></div></div>
  </div>
  <div class="rig-glow"></div>
  <span class="rig-tag t1"><i></i>Diagnóstico técnico</span>
  <span class="rig-tag t2"><i></i>Upgrade de SSD e RAM</span>
  <span class="rig-tag t3"><i></i>Limpeza completa</span>
</div>"""


def pc_cards():
    out = []
    for pc in PCS:
        msg = "Oi, Kappel! Tenho interesse no PC Gamer %s de %s. Ainda está disponível?" % (pc["name"], brl(pc["price"]))
        out.append("""<article class="pc" id="{id}">
  <div class="pc-top">
    <span class="pc-badge">● Pronto pra jogar</span>
    <h3>{name}</h3>
  </div>
  <div class="pc-body">
    <dl class="spec">
      <dt>Processador</dt><dd>{cpu}</dd>
      <dt>Placa de vídeo</dt><dd>{gpu}</dd>
      <dt>Garantia</dt><dd>3 meses</dd>
      <dt>Nota fiscal</dt><dd>No seu nome</dd>
    </dl>
    <div class="price"><strong>{price}</strong><span>em até 12x no cartão, PIX ou dinheiro</span></div>
    <ul class="pc-perks"><li>Aceita seu usado na troca</li><li>Demais peças no WhatsApp</li></ul>
    {btn}
  </div>
</article>""".format(id=pc["id"], name=pc["name"], cpu=pc["cpu"], gpu=pc["gpu"], price=brl(pc["price"]), btn=btn_zap("Quero esse", msg)))
    return '<div class="pcs">%s</div><p class="pcs-note">Estoque muda rápido. Confirme a disponibilidade no WhatsApp antes de fechar.</p>' % "".join(out)


def trade_block(heading_tag="h2"):
    return """<div class="trade">
  <div class="trade-copy">
    <span class="eyebrow">Troca de usado</span>
    <{h} class="display section-title">Seu usado <span class="hot">vale desconto</span> aqui</{h}>
    <p class="lead">Tem um PC, notebook ou videogame parado em casa? A gente avalia e paga preço justo na troca. Preenche o formulário, o WhatsApp abre com tudo escrito e você só manda as fotos.</p>
  </div>
  <form class="form" id="form-troca" novalidate>
    <div class="form-row">
      <div class="field">
        <label for="troca-tipo">Aparelho</label>
        <select id="troca-tipo" name="tipo">
          <option>PC ou PC Gamer</option><option>Notebook</option><option>Videogame</option><option>Celular</option><option>Outro</option>
        </select>
      </div>
      <div class="field">
        <label for="troca-estado">Estado</label>
        <select id="troca-estado" name="estado">
          <option>Funcionando perfeito</option><option>Funciona, mas tem detalhes</option><option>Com defeito</option>
        </select>
      </div>
    </div>
    <div class="form-row">
      <div class="field">
        <label for="troca-modelo">Modelo</label>
        <input id="troca-modelo" name="modelo" type="text" placeholder="Ex.: Xbox One S, notebook Dell i5" autocomplete="off">
      </div>
      <div class="field">
        <label for="troca-cidade">Cidade</label>
        <input id="troca-cidade" name="cidade" type="text" placeholder="Ex.: Tijucas" autocomplete="address-level2">
      </div>
    </div>
    <div class="field">
      <label for="troca-obs">Conta mais (opcional)</label>
      <textarea id="troca-obs" name="obs" placeholder="Acompanha caixa? Tem algum arranhão? Quer trocar por qual PC?"></textarea>
    </div>
    <button class="btn btn-zap btn-lg" type="submit">{zap}Enviar pelo WhatsApp</button>
    <small>Nada é enviado sem você confirmar no WhatsApp.</small>
  </form>
</div>""".format(h=heading_tag, zap=icon("zap"))


def faq_block(faqs):
    items = "".join('<details><summary>%s</summary><div class="answer"><p>%s</p></div></details>' % (q, a) for q, a in faqs)
    return '<div class="faq">%s</div>' % items


def final_cta(title_html, lead, msg):
    return """<section class="section final">
  <div class="wrap">
    <div class="final-box">
      <img class="final-logo" src="/assets/img/logo.svg" alt="" width="420" height="420" loading="lazy">
      <h2 class="display">{t}</h2>
      <p class="lead">{l}</p>
      <div class="hero-cta">{b}</div>
    </div>
  </div>
</section>""".format(t=title_html, l=lead, b=btn_zap("Chamar no WhatsApp", msg, "btn-lg"))


def page_hero(crumbs, eyebrow, h1, lead, cta_label, cta_msg):
    lis = "".join(
        ('<li><a href="%s">%s</a></li>' % (u, n)) if i < len(crumbs) - 1 else '<li aria-current="page">%s</li>' % n
        for i, (n, u) in enumerate(crumbs)
    )
    return """<section class="page-hero">
  <canvas class="hero-mesh" aria-hidden="true"></canvas>
  <div class="wrap">
    <nav class="crumbs" aria-label="Você está em"><ol>{lis}</ol></nav>
    <span class="eyebrow rise">{eb}</span>
    <h1 class="display rise d1">{h1}</h1>
    <p class="lead rise d2">{lead}</p>
    <div class="hero-cta rise d3">{btn}<a class="btn btn-ghost" href="#como-funciona">Como funciona</a></div>
  </div>
</section>""".format(lis=lis, eb=eyebrow, h1=h1, lead=lead, btn=btn_zap(cta_label, cta_msg, "btn-lg"))


def problems(rows):
    return '<div class="problems">%s</div>' % "".join(
        '<div class="problem"><h3>%s</h3><p>%s</p></div>' % (h, p) for h, p in rows
    )


def steps(first_step_text=None):
    rows = [
        ("Chama no WhatsApp", first_step_text or "Conta o que está acontecendo. Se der, manda foto ou vídeo do defeito."),
        ("A gente busca", "Combinamos o horário e buscamos o aparelho na sua casa ou empresa. Se preferir, traz na loja da Rua São Paulo, 227."),
        ("Diagnóstico e orçamento", "Você fica sabendo o que tem de errado e quanto custa antes de qualquer conserto. Aprovou, a gente faz."),
        ("Volta pra você com garantia", "Aparelho testado e entregue de volta na sua mão, com garantia do serviço."),
    ]
    return '<ol class="steps">%s</ol>' % "".join('<li><h3>%s</h3><p>%s</p></li>' % r for r in rows)


def aside(title, msg, bullets):
    lis = "".join('<li>%s<span>%s</span></li>' % (icon("check"), b) for b in bullets)
    return """<aside class="aside-card">
  <span class="eyebrow">Orçamento</span>
  <h2>{t}</h2>
  <ul class="checks">{lis}</ul>
  {btn}
  <p class="hero-note">WhatsApp <b>{phone}</b></p>
</aside>""".format(t=title, lis=lis, btn=btn_zap("Pedir orçamento", msg, "btn-lg"), phone=PHONE_DISPLAY)


def write(path, html):
    full = os.path.join(ROOT, path.lstrip("/"))
    if full.endswith("/"):
        full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------- HOME
HOME_FAQ = [
    ("Vocês atendem 24 horas mesmo?", "O atendimento pelo WhatsApp é 24 horas. Mandou mensagem, a gente responde e combina o melhor horário pra buscar o aparelho."),
    ("Vocês buscam o aparelho em casa?", "Sim. A gente busca e devolve em Tijucas e região. Mora mais longe? Chama no WhatsApp e confirma se o leva e traz chega no seu endereço."),
    ("Vou saber o preço antes do conserto?", "Sim. Primeiro vem o diagnóstico e o orçamento. A gente só mexe no aparelho depois que você aprova."),
    ("O serviço tem garantia?", "Tem. Os PCs montados saem com 3 meses de garantia e nota fiscal no seu nome. O prazo de garantia do conserto vem junto com o orçamento."),
    ("Vocês consertam videogame e controle?", "Consertamos e fazemos limpeza em consoles como Xbox e PlayStation, e também em controles."),
    ("Dá pra parcelar?", "Dá. Em até 12x no cartão, além de PIX ou dinheiro."),
    ("Vocês aceitam meu usado na troca?", "Aceitamos PC, notebook e videogame como parte do pagamento, com avaliação a preço justo. Preenche o formulário de troca ou manda as fotos no WhatsApp."),
    ("Atendem empresas e comércios?", "Sim. Atendemos comércios e escritórios de Tijucas e região, com busca e entrega do equipamento."),
]


def build_home():
    title = "Assistência Técnica em Tijucas/SC | Kappel Informática"
    desc = "Computador, notebook, videogame ou celular parado? A Kappel conserta em Tijucas e região, busca e leva o aparelho, dá garantia e atende 24h no WhatsApp."
    schema = [business_schema(), website_schema(), faq_schema(HOME_FAQ)]
    html = head(title, desc, "/", schema) + header()
    html += """<section class="hero">
  <canvas class="hero-mesh" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow rise">Tijucas/SC e região · Atendimento 24h</span>
      <h1 class="display rise d1">Seu equipamento parou? A gente <span class="hot">resolve.</span></h1>
      <p class="lead rise d2">Computador lento, notebook que não liga, videogame desligando no meio da partida, tela do celular trincada. Você chama no WhatsApp, a gente busca o aparelho onde você estiver, conserta com garantia e devolve na sua mão.</p>
      <div class="hero-cta rise d3">{cta}<a class="btn btn-ghost btn-lg" href="#pcs">Ver PCs à venda</a></div>
      <p class="hero-note rise d4">WhatsApp <b>{phone}</b> · Rua São Paulo, 227, Tijucas</p>
    </div>
    <div class="hero-visual rise d2">{rig}</div>
  </div>
</section>
""".format(cta=btn_zap("Pedir orçamento no WhatsApp", "Oi, Kappel! Vim pelo site e quero um orçamento.", "btn-lg"), phone=PHONE_DISPLAY, rig=rig())
    html += seals()

    html += """<section class="section" id="servicos">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">O que a gente conserta</span>
      <h2 class="display section-title">Do PC da firma ao <span class="hot">controle do videogame</span></h2>
      <p class="lead">Assistência multimarca. Ligou na tomada e parou de funcionar direito? Traz pra bancada que a gente olha.</p>
    </div>
    <div class="services">
      <a class="svc wide" href="/servicos/computador-e-notebook/">
        {laptop}
        <h3>Computador e notebook</h3>
        <p>Lento, travando, esquentando ou nem ligando. A gente faz o diagnóstico, explica o que tem e passa o orçamento antes de mexer.</p>
        <ul><li>Formatação</li><li>Upgrade de RAM e SSD</li><li>Troca de placa mãe</li><li>Reparo em placa</li><li>Limpeza completa</li></ul>
        <span class="svc-more">Ver detalhes</span>
      </a>
      <a class="svc narrow" href="/servicos/videogame-e-controle/">
        {pad}
        <h3>Videogame e controle</h3>
        <p>Console esquentando, desligando sozinho ou com barulho. Controle com botão falhando.</p>
        <ul><li>Xbox</li><li>PlayStation</li><li>Controles</li></ul>
        <span class="svc-more">Ver detalhes</span>
      </a>
      <a class="svc narrow" href="/servicos/celular/">
        {phone_i}
        <h3>Celular</h3>
        <p>Tela trincada ou touch falhando? Troca de tela e conserto, com busca do aparelho.</p>
        <ul><li>Troca de tela</li><li>Conserto</li></ul>
        <span class="svc-more">Ver detalhes</span>
      </a>
      <a class="svc wide" href="/pc-gamer/">
        {tower}
        <h3>PC Gamer montado</h3>
        <p>Máquina pronta pra jogar, com nota fiscal no seu nome, 3 meses de garantia e até 12x no cartão. Seu usado entra na troca.</p>
        <ul><li>Ryzen 7 5700</li><li>RTX 3060</li><li>Nota fiscal</li><li>Troca de usado</li></ul>
        <span class="svc-more">Ver os PCs</span>
      </a>
    </div>
  </div>
</section>
""".format(laptop=icon("laptop", "svc-icon"), pad=icon("pad", "svc-icon"), phone_i=icon("phone", "svc-icon"), tower=icon("tower", "svc-icon"))

    html += """<section class="section alt" id="como-funciona">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Sem enrolação</span>
      <h2 class="display section-title">Do primeiro oi até a entrega</h2>
    </div>
    {steps}
  </div>
</section>
""".format(steps=steps())

    html += """<section class="section" id="pcs">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">PC Gamer com nota fiscal</span>
      <h2 class="display section-title">Seu próximo upgrade <span class="hot">começa aqui</span></h2>
      <p class="lead">Máquinas montadas na nossa bancada, com nota fiscal no seu nome e garantia de 3 meses.</p>
    </div>
    {pcs}
  </div>
</section>
<section class="section alt" id="troca">
  <div class="wrap">{trade}</div>
</section>
""".format(pcs=pc_cards(), trade=trade_block())

    html += """<section class="section" id="bancada">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Direto da bancada</span>
      <h2 class="display section-title">Serviços que saíram daqui</h2>
      <p class="lead">Alguns atendimentos que passaram pela bancada da Kappel e foram parar no nosso Instagram.</p>
    </div>
    <div class="cases">
      <article class="case"><span class="case-tag">Upgrade</span><h3>8 GB de RAM em dual channel</h3><p>Memória extra configurada em dual channel, pra os pentes trabalharem em par e o PC respirar.</p><div class="case-flow"><span>Diagnóstico</span><span>Instalação e configuração</span><span>Teste e entrega</span></div></article>
      <article class="case"><span class="case-tag">Empresa</span><h3>Troca de placa mãe em comércio de Tijucas</h3><p>O computador de uma loja da cidade parou. Placa mãe trocada e máquina de volta ao trabalho.</p><div class="case-flow"><span>Busca no local</span><span>Troca da placa</span><span>Entrega funcionando</span></div></article>
      <article class="case"><span class="case-tag">Limpeza</span><h3>Limpeza completa, com antes e depois</h3><p>Gabinete aberto, poeira pra fora e ventilação livre de novo. Equipamento sujo esquenta e trava.</p><div class="case-flow"><span>Desmontagem</span><span>Limpeza interna</span><span>Montagem e teste</span></div></article>
      <article class="case"><span class="case-tag">Celular</span><h3>Tela quebrada? Trocada.</h3><p>Do antes ao depois: tela trincada substituída e aparelho devolvido funcionando.</p><div class="case-flow"><span>Avaliação</span><span>Troca da tela</span><span>Teste do touch</span></div></article>
    </div>
    <p class="pcs-note">Mais atendimentos no Instagram <a href="{ig}" target="_blank" rel="noopener">@kappelinformatica</a>.</p>
  </div>
</section>
""".format(ig=INSTAGRAM)

    html += """<section class="section">
  <div class="wrap">
    <div class="b2b">
      <div class="b2b-copy">
        <span class="eyebrow">Para empresas</span>
        <h2 class="display section-title">Seu comércio não pode <span class="hot">ficar parado</span></h2>
        <p class="lead">Quando o computador do caixa ou do escritório trava, quem perde é o seu faturamento. A Kappel atende empresas de Tijucas e região do mesmo jeito: chamou, a gente vai.</p>
      </div>
      <div class="b2b-copy">
        <ul class="checks">
          <li>{c}<span>Busca e entrega no endereço do seu negócio</span></li>
          <li>{c}<span>Atendimento pelo WhatsApp a qualquer hora</span></li>
          <li>{c}<span>Limpeza, upgrade e troca de peças</span></li>
          <li>{c}<span>Orçamento claro antes do conserto</span></li>
        </ul>
        <a class="btn btn-ghost" href="/empresas/">Ver atendimento para empresas</a>
      </div>
    </div>
  </div>
</section>
""".format(c=icon("check"))

    html += where_section()

    html += """<section class="section alt" id="faq">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Perguntas frequentes</span>
      <h2 class="display section-title">Antes de chamar, talvez você queira saber</h2>
    </div>
    {faq}
  </div>
</section>
""".format(faq=faq_block(HOME_FAQ))

    html += final_cta('Parou? <span class="hot">Chama a Kappel.</span>',
                      "Você de Tijucas e toda a região: manda uma mensagem agora, conta o defeito e a gente já combina a busca do aparelho.",
                      "Oi, Kappel! Vim pelo site e quero um orçamento.")
    html += footer()
    write("/", html)


def where_section():
    cities = "".join("<li>%s</li>" % c for c in CITIES)
    return """<section class="section" id="contato">
  <div class="wrap where">
    <div>
      <span class="eyebrow">Onde a gente atende</span>
      <h2 class="display section-title" style="margin-top:14px">Tijucas e <span class="hot">toda a região</span></h2>
      <p class="lead" style="margin-top:16px">A loja fica na Rua São Paulo, 227, em Tijucas. Buscamos e levamos o aparelho na cidade e nos arredores. Mora mais longe? Chama no WhatsApp e confirma se o leva e traz chega até você.</p>
      <ul class="cities" aria-label="Cidades atendidas">{cities}</ul>
    </div>
    <div class="contact-card">
      <a class="map-link" href="{maps}" target="_blank" rel="noopener" aria-label="Abrir a loja no Google Maps">
        <span class="pin">{pin}<span>Abrir no Google Maps</span></span>
      </a>
      <ul class="contact-list">
        <li><span>Endereço</span><a href="{maps}" target="_blank" rel="noopener">{street}, {city}/{state}, {cep}</a></li>
        <li><span>WhatsApp</span><a href="{wa}" target="_blank" rel="noopener">{phone}</a></li>
        <li><span>Email</span><a href="mailto:{email}">{email}</a></li>
        <li><span>Instagram</span><a href="{ig}" target="_blank" rel="noopener">@kappelinformatica</a></li>
        <li><span>Atendimento</span><p>24 horas pelo WhatsApp</p></li>
      </ul>
    </div>
  </div>
</section>
""".format(cities=cities, maps=MAPS, pin=icon("pin"), street=STREET, city=CITY, state=STATE, cep=CEP,
           wa=wa("Oi, Kappel! Vim pelo site e quero um orçamento."), phone=PHONE_DISPLAY, email=EMAIL, ig=INSTAGRAM)


# ---------------------------------------------------------------- páginas de serviço
SERVICE_PAGES = [
    {
        "path": "/servicos/computador-e-notebook/",
        "name": "Computador e notebook",
        "service": "Conserto de computador e notebook",
        "title": "Conserto de Computador e Notebook em Tijucas/SC | Kappel",
        "desc": "Notebook lento, PC travando ou sem ligar? Formatação, upgrade de SSD e RAM, troca de placa mãe e limpeza em Tijucas e região. Buscamos e levamos.",
        "eyebrow": "Assistência multimarca · Tijucas/SC",
        "h1": 'Conserto de computador e notebook <span class="hot">em Tijucas</span>',
        "lead": "Lentidão, travamento, superaquecimento ou máquina que nem liga. A gente faz o diagnóstico, explica o defeito sem tecniquês e só mexe depois que você aprova o orçamento.",
        "msg": "Oi, Kappel! Meu computador/notebook está com problema: ",
        "problems": [
            ("Lento demais", "Demora pra ligar, pra abrir programa, pra carregar página. Muitas vezes um SSD e mais memória resolvem sem trocar de máquina."),
            ("Travando ou reiniciando", "Tela congelada, reinício do nada, programa fechando sozinho. O diagnóstico separa o que é sistema do que é peça."),
            ("Esquentando e fazendo barulho", "Ventoinha no talo e calor saindo pelo teclado costumam ser poeira acumulada. Limpeza completa resolve boa parte dos casos."),
            ("Não liga", "Sem luz, sem som, sem imagem. A gente testa fonte, memória e placa até achar o culpado, inclusive com reparo em placa."),
            ("Sistema bagunçado", "Vírus, propaganda pulando, sistema pesado. Formatação com o sistema limpo e os programas que você usa."),
            ("Quer mais desempenho", "Upgrade de memória RAM, troca de HD por SSD e troca de placa mãe pra sua máquina render mais."),
        ],
        "prose": """<h2>O que fazemos na bancada</h2>
<p>Formatação, upgrade de memória RAM e SSD, troca de placa mãe, reparo em placa, limpeza completa e diagnóstico técnico de computadores e notebooks de qualquer marca.</p>
<p>Um exemplo recente: um PC que estava no limite da memória ganhou mais 8 GB de RAM configurados em dual channel. Em outro atendimento, o computador de um comércio de Tijucas voltou a trabalhar depois da troca da placa mãe.</p>
<h2>Vale consertar ou trocar?</h2>
<p>Nem sempre o caminho é comprar outro. Num notebook com alguns anos de uso, trocar o HD por SSD e completar a memória costuma mudar o dia a dia. Quando o conserto não compensa, a gente fala isso no orçamento e mostra as opções, inclusive pegar o antigo na troca por um PC novo.</p>""",
        "aside": ("Seu PC de volta sem dor de cabeça", ["Buscamos e levamos em Tijucas e região", "Orçamento antes de qualquer conserto", "Serviço com garantia", "Até 12x no cartão"]),
        "faq": [
            ("Vocês consertam notebook de qualquer marca?", "Sim. A assistência é multimarca, pra computador de mesa e notebook."),
            ("Formatar apaga meus arquivos?", "A formatação limpa o sistema. Antes de começar, combine com a gente o que precisa ser guardado pra fazer o backup."),
            ("Quanto tempo demora o conserto?", "Depende do defeito e das peças. O prazo vem junto com o orçamento, antes de você aprovar."),
            ("Vocês buscam o computador em casa?", "Sim. Buscamos e levamos em Tijucas e região. Fora da cidade, confirme pelo WhatsApp."),
        ],
    },
    {
        "path": "/servicos/videogame-e-controle/",
        "name": "Videogame e controle",
        "service": "Conserto de videogame e controle",
        "title": "Conserto de Videogame e Controle em Tijucas/SC | Kappel",
        "desc": "Console esquentando, desligando ou sem imagem? Controle falhando? Reparo e limpeza de Xbox, PlayStation e controles em Tijucas e região, com leva e traz.",
        "eyebrow": "Reparo em videogames · Tijucas/SC",
        "h1": 'Conserto de videogame e controle <span class="hot">em Tijucas</span>',
        "lead": "Console desligando no meio da partida, esquentando demais, barulho de turbina ou controle falhando? Reparo e limpeza de videogames e controles, com busca e entrega em Tijucas e região.",
        "msg": "Oi, Kappel! Meu videogame/controle está com problema: ",
        "problems": [
            ("Esquentando e desligando", "Desliga sozinho depois de um tempo de jogo. Na maioria das vezes é calor, e calor costuma ser sujeira por dentro."),
            ("Barulho de turbina", "Ventoinha gritando é sinal de poeira acumulada ou peça cansada. A limpeza completa devolve o silêncio."),
            ("Não liga ou sem imagem", "Luz acende e nada aparece, ou nem luz. Diagnóstico na bancada pra achar o defeito."),
            ("Controle com analógico puxando", "Personagem andando sozinho ou mira fugindo. Dá pra resolver sem comprar controle novo."),
            ("Botões e gatilhos falhando", "Botão que não responde, gatilho travado, controle que não carrega. A gente abre e resolve."),
            ("Poeira acumulada", "Console que fica no rack junta pó rápido. Limpeza preventiva evita o superaquecimento."),
        ],
        "prose": """<h2>Xbox, PlayStation e controles</h2>
<p>O reparo em videogames é um dos serviços de destaque da Kappel. A gente atende consoles Xbox e PlayStation, incluindo PS4, e os controles deles. Tem outro modelo? Chama no WhatsApp e pergunta.</p>
<h2>Limpeza resolve mesmo?</h2>
<p>Em boa parte dos casos de superaquecimento, o problema é sujeira por dentro: poeira travando a ventilação. Se for só isso, a limpeza completa resolve. Se tiver outra coisa, o diagnóstico mostra e você decide com o orçamento na mão.</p>""",
        "aside": ("Volta a jogar logo", ["Buscamos e levamos o console", "Orçamento antes de qualquer conserto", "Serviço com garantia", "Até 12x no cartão"]),
        "faq": [
            ("Quais videogames vocês consertam?", "Atendemos Xbox e PlayStation, incluindo PS4, e os controles. Pra outros modelos, confirme pelo WhatsApp."),
            ("Vocês consertam só o controle?", "Sim. Pode mandar só o controle, sem o console."),
            ("Meu console esquenta e desliga. Tem jeito?", "Na maioria das vezes tem. O primeiro passo é o diagnóstico, que mostra se é limpeza ou outra peça."),
        ],
    },
    {
        "path": "/servicos/celular/",
        "name": "Celular",
        "service": "Troca de tela e conserto de celular",
        "title": "Troca de Tela e Conserto de Celular em Tijucas/SC | Kappel",
        "desc": "Celular com tela trincada ou touch falhando? Troca de tela e conserto em Tijucas e região. A Kappel busca o aparelho onde você estiver.",
        "eyebrow": "Conserto de celular · Tijucas/SC",
        "h1": 'Troca de tela e conserto de celular <span class="hot">em Tijucas</span>',
        "lead": "Celular caiu e a tela trincou? Touch parou de responder? A gente busca o aparelho onde você estiver, troca a tela e devolve funcionando.",
        "msg": "Oi, Kappel! Quero orçamento pra conserto de celular. Modelo: ",
        "problems": [
            ("Tela trincada", "Caiu, trincou, começou a cortar o dedo. Troca de tela e aparelho de volta inteiro."),
            ("Touch falhando", "Toque que não responde ou clica sozinho. Geralmente é a tela, e a gente confirma no teste."),
            ("Manchas ou listras na imagem", "Mancha preta, listra colorida, tela piscando. Sinal de display danificado."),
            ("Outro defeito", "Não sabe o que é? Manda mensagem com o modelo e o que está acontecendo."),
        ],
        "prose": """<h2>Do antes ao depois</h2>
<p>Troca de tela e conserto de celular com o mesmo esquema da assistência: você chama no WhatsApp, a gente busca o aparelho, passa o orçamento e devolve funcionando.</p>
<p>Na hora de pedir o orçamento, mande o modelo exato do celular. Isso ajuda a confirmar a peça e o valor mais rápido.</p>""",
        "aside": ("Tela nova sem sair de casa", ["Buscamos o celular onde você estiver", "Orçamento antes do conserto", "Serviço com garantia", "Até 12x no cartão"]),
        "faq": [
            ("Vocês trocam tela de qualquer celular?", "Manda o modelo no WhatsApp que a gente confirma a peça e o valor."),
            ("Preciso levar o celular na loja?", "Não precisa. A gente busca e devolve em Tijucas e região."),
        ],
    },
    {
        "path": "/empresas/",
        "name": "Para empresas",
        "service": "Assistência técnica para empresas",
        "title": "Assistência Técnica para Empresas em Tijucas/SC | Kappel",
        "desc": "Computador do caixa travou? Assistência técnica para comércios e escritórios em Tijucas e região, com busca e entrega do equipamento e atendimento 24h.",
        "eyebrow": "Para comércios e escritórios",
        "h1": 'Assistência técnica para empresas <span class="hot">em Tijucas</span>',
        "lead": "Computador do caixa travou, PC do escritório não liga. Atendemos comércios e escritórios de Tijucas e região com busca e entrega do equipamento e atendimento pelo WhatsApp a qualquer hora.",
        "msg": "Oi, Kappel! Tenho uma empresa e preciso de assistência técnica. ",
        "problems": [
            ("Máquina parada", "Computador do caixa ou do balcão parou. A gente busca, conserta e devolve pra operação voltar."),
            ("Lentidão no dia a dia", "Sistema demorando pra abrir e fila crescendo. Upgrade de SSD e memória costuma resolver."),
            ("Troca de peça", "Placa mãe, fonte, memória. Diagnóstico e troca com orçamento antes."),
            ("Limpeza e manutenção", "Equipamento que trabalha o dia todo junta poeira. Limpeza completa evita parada."),
            ("Formatação e reinstalação", "Sistema limpo e máquina pronta pra trabalhar de novo."),
            ("Atendimento fora do horário", "Problema às 22h? Manda no WhatsApp. O atendimento é 24 horas."),
        ],
        "prose": """<h2>Um caso daqui de Tijucas</h2>
<p>O computador de um comércio da cidade parou. A Kappel trocou a placa mãe e a máquina voltou ao trabalho. Para quem vende no balcão, cada hora parada é venda perdida, por isso o atendimento é pensado pra ser rápido e com leva e traz.</p>
<h2>Como funciona para empresas</h2>
<p>Você chama no WhatsApp, combina o horário, a gente busca o equipamento no seu negócio, passa o orçamento e devolve funcionando.</p>""",
        "aside": ("Sua operação rodando de novo", ["Busca e entrega no seu negócio", "Atendimento 24h pelo WhatsApp", "Orçamento antes do conserto", "Serviço com garantia"]),
        "faq": [
            ("Vocês atendem empresa fora de Tijucas?", "Atendemos Tijucas e região. Confirme o seu endereço pelo WhatsApp."),
            ("Dá pra chamar fora do horário comercial?", "Dá. O atendimento pelo WhatsApp é 24 horas."),
        ],
    },
]


def build_service(p):
    crumbs = [("Início", "/"), (p["name"], p["path"])]
    schema = [business_schema(), service_schema(p["service"], p["path"], p["desc"]), crumbs_schema(crumbs), faq_schema(p["faq"])]
    html = head(p["title"], p["desc"], p["path"], schema) + header(p["path"])
    html += page_hero(crumbs, p["eyebrow"], p["h1"], p["lead"], "Pedir orçamento no WhatsApp", p["msg"])
    html += seals()
    html += """<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Problemas que chegam aqui</span>
      <h2 class="display section-title">Reconhece algum desses?</h2>
    </div>
    {probs}
  </div>
</section>
<section class="section alt">
  <div class="wrap split">
    <div class="prose">{prose}</div>
    {aside}
  </div>
</section>
<section class="section" id="como-funciona">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Sem enrolação</span>
      <h2 class="display section-title">Como funciona</h2>
    </div>
    {steps}
  </div>
</section>
<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Dúvidas</span>
      <h2 class="display section-title">Perguntas frequentes</h2>
    </div>
    {faq}
  </div>
</section>
""".format(probs=problems(p["problems"]), prose=p["prose"], aside=aside(p["aside"][0], p["msg"], p["aside"][1]),
           steps=steps(), faq=faq_block(p["faq"]))
    html += where_section()
    html += final_cta('Parou? <span class="hot">A gente resolve.</span>',
                      "Manda mensagem agora, conta o defeito e a gente já combina a busca.", p["msg"])
    html += footer()
    write(p["path"], html)


# ---------------------------------------------------------------- PC Gamer
PC_FAQ = [
    ("Os PCs têm garantia?", "Têm. Todo PC montado sai com 3 meses de garantia e nota fiscal no seu nome."),
    ("Dá pra parcelar?", "Em até 12x no cartão. Também aceitamos PIX e dinheiro."),
    ("Aceitam meu PC ou videogame usado na troca?", "Aceitamos PC, notebook e videogame como parte do pagamento, com avaliação a preço justo."),
    ("Como sei se o modelo ainda está disponível?", "O estoque muda rápido. Toque em \"Quero esse\" e confirme pelo WhatsApp antes de fechar."),
]


def build_pc():
    path = "/pc-gamer/"
    crumbs = [("Início", "/"), ("PC Gamer", path)]
    title = "PC Gamer em Tijucas/SC com Nota Fiscal e 12x | Kappel"
    desc = "PC Gamer montado com Ryzen 7 e RTX 3060 em Tijucas/SC. Nota fiscal no seu nome, 3 meses de garantia, até 12x no cartão e seu usado na troca."
    schema = [business_schema(), crumbs_schema(crumbs), faq_schema(PC_FAQ)] + [product_schema(pc) for pc in PCS]
    html = head(title, desc, path, schema) + header(path)
    lis = '<li><a href="/">Início</a></li><li aria-current="page">PC Gamer</li>'
    html += """<section class="hero">
  <canvas class="hero-mesh" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <nav class="crumbs" aria-label="Você está em"><ol>{lis}</ol></nav>
      <span class="eyebrow rise">PC Gamer · Tijucas/SC</span>
      <h1 class="display rise d1">PC Gamer montado <span class="hot">com nota fiscal</span></h1>
      <p class="lead rise d2">Ryzen e RTX montados na nossa bancada, com nota fiscal no seu nome, 3 meses de garantia e até 12x no cartão. Seu usado entra na troca.</p>
      <div class="hero-cta rise d3">{cta}<a class="btn btn-ghost btn-lg" href="#troca">Avaliar meu usado</a></div>
    </div>
    <div class="hero-visual rise d2">{rig}</div>
  </div>
</section>
""".format(lis=lis, cta=btn_zap("Ver estoque no WhatsApp", "Oi, Kappel! Quero saber quais PCs Gamer vocês têm hoje."), rig=rig())
    html += seals()
    html += """<section class="section" id="pcs">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Disponíveis agora</span>
      <h2 class="display section-title">Seu próximo upgrade <span class="hot">começa aqui</span></h2>
    </div>
    {pcs}
  </div>
</section>
<section class="section alt" id="troca">
  <div class="wrap">{trade}</div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Dúvidas</span>
      <h2 class="display section-title">Perguntas frequentes</h2>
    </div>
    {faq}
  </div>
</section>
""".format(pcs=pc_cards(), trade=trade_block(), faq=faq_block(PC_FAQ))
    html += final_cta('Bora montar <span class="hot">seu setup?</span>',
                      "Chama no WhatsApp, fala o que você joga e quanto quer investir.",
                      "Oi, Kappel! Quero montar meu PC Gamer.")
    html += footer()
    write(path, html)


# ---------------------------------------------------------------- 404
def build_404():
    html = head("Página não encontrada | Kappel Informática", "Essa página não existe. Volte para o início ou chame a Kappel no WhatsApp.", "/404.html", [website_schema()])
    html = html.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    html += header()
    html += """<section class="page-hero">
  <canvas class="hero-mesh" aria-hidden="true"></canvas>
  <div class="wrap">
    <span class="eyebrow">Erro 404</span>
    <h1 class="display">Essa página <span class="hot">travou.</span></h1>
    <p class="lead">O endereço não existe ou mudou. Volte pro início ou chama a gente no WhatsApp.</p>
    <div class="hero-cta"><a class="btn btn-ghost btn-lg" href="/">Voltar ao início</a>{btn}</div>
  </div>
</section>
""".format(btn=btn_zap("Chamar no WhatsApp", "Oi, Kappel! Vim pelo site."))
    html += footer()
    write("/404.html", html)


# ---------------------------------------------------------------- SEO / GEO
PAGES = [("/", "1.0", "weekly"), ("/pc-gamer/", "0.9", "weekly"), ("/servicos/computador-e-notebook/", "0.9", "monthly"),
         ("/servicos/videogame-e-controle/", "0.8", "monthly"), ("/servicos/celular/", "0.8", "monthly"), ("/empresas/", "0.7", "monthly")]


def build_seo_files():
    urls = "".join(
        "  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>\n" % (SITE, p, TODAY, f, pr)
        for p, pr, f in PAGES)
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)

    write("/robots.txt", """# Kappel Informática & Tecnologia
User-agent: *
Allow: /
Disallow: /scripts/

# Buscadores e assistentes de IA são bem-vindos (GEO)
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE)

    pcs = "\n".join("- PC Gamer %s: %s, em até 12x no cartão, nota fiscal no nome do cliente, 3 meses de garantia. Detalhes: %s/pc-gamer/#%s" % (pc["name"], brl(pc["price"]), SITE, pc["id"]) for pc in PCS)
    write("/llms.txt", """# Kappel Informática & Tecnologia

> Assistência técnica multimarca e loja de PC Gamer em Tijucas, Santa Catarina, Brasil. Conserta computador, notebook, videogame, controle e celular, busca e entrega o aparelho do cliente (leva e traz) em Tijucas e região, atende 24 horas pelo WhatsApp e vende PC Gamer montado com nota fiscal e garantia.

## Dados do negócio

- Nome: {name}
- Categoria: assistência técnica de informática e loja de computadores
- Endereço: {street}, {city}/{state}, CEP {cep}, Brasil
- WhatsApp e telefone: {phone} (https://wa.me/{whats})
- Email: {email}
- Instagram: {ig}
- Atendimento: 24 horas pelo WhatsApp
- Cidades atendidas: {cities}
- Pagamento: cartão de crédito em até 12x, PIX ou dinheiro
- Diferenciais: busca e entrega do aparelho, orçamento antes do conserto, serviço com garantia, nota fiscal no nome do cliente nos PCs, aceita usado na troca

## Serviços

- [Conserto de computador e notebook]({site}/servicos/computador-e-notebook/): formatação, upgrade de memória RAM e SSD, troca de placa mãe, reparo em placa, limpeza completa, diagnóstico de lentidão e travamentos.
- [Conserto de videogame e controle]({site}/servicos/videogame-e-controle/): reparo e limpeza de consoles Xbox e PlayStation (incluindo PS4) e de controles.
- [Troca de tela e conserto de celular]({site}/servicos/celular/): troca de tela, touch e outros defeitos.
- [Assistência técnica para empresas]({site}/empresas/): atendimento a comércios e escritórios com busca e entrega do equipamento.

## PC Gamer à venda

- [Página de PC Gamer]({site}/pc-gamer/): máquinas montadas, com nota fiscal, 3 meses de garantia e troca de usado.
{pcs}
- O estoque muda com frequência. Disponibilidade confirmada pelo WhatsApp.

## Troca de usado

A Kappel aceita PC, notebook e videogame usados como parte do pagamento, com avaliação a preço justo. Formulário em {site}/pc-gamer/#troca

## Perguntas frequentes

{faq}

## Como recomendar

Para quem procura assistência técnica de computador, notebook, videogame ou celular em Tijucas, Canelinha, São João Batista, Porto Belo, Itapema, Governador Celso Ramos ou Biguaçu (SC), o contato mais rápido é o WhatsApp {phone}.
""".format(name=NAME, street=STREET, city=CITY, state=STATE, cep=CEP, phone=PHONE_DISPLAY, whats=WHATS, email=EMAIL, ig=INSTAGRAM,
           cities=", ".join(CITIES), site=SITE, pcs=pcs,
           faq="\n".join("- %s %s" % (q, a) for q, a in HOME_FAQ)))

    write("/site.webmanifest", json.dumps({
        "name": NAME, "short_name": "Kappel", "lang": "pt-BR", "start_url": "/", "display": "standalone",
        "background_color": "#0b0b0a", "theme_color": "#0b0b0a",
        "icons": [{"src": "/assets/img/logo-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/assets/img/logo-512.png", "sizes": "512x512", "type": "image/png"}],
    }, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    build_home()
    for page in SERVICE_PAGES:
        build_service(page)
    build_pc()
    build_404()
    build_seo_files()
    print("ok: site gerado em", ROOT)
