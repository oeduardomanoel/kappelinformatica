# Kappel Informática & Tecnologia · site

Site estático da Kappel Informática (Tijucas/SC), pronto para a Vercel. Sem framework e sem build em produção: é só HTML, CSS e JS servidos da raiz do repositório.

## Estrutura

```
index.html                         Home (hero, serviços, PCs, troca, bancada, empresas, região, FAQ)
servicos/computador-e-notebook/    Página SEO: conserto de PC e notebook
servicos/videogame-e-controle/     Página SEO: conserto de videogame e controle
servicos/celular/                  Página SEO: troca de tela e conserto de celular
pc-gamer/                          Vitrine de PCs + formulário de troca de usado
empresas/                          Assistência para comércios e escritórios
404.html
robots.txt  sitemap.xml  llms.txt  site.webmanifest
vercel.json  .vercelignore          Configuração de deploy na Vercel
assets/css/site.css  assets/js/site.js  assets/fonts/  assets/img/
scripts/build.py                   Gerador das páginas (fonte única de dados)
```

## Como editar

Todo o conteúdo sai de `scripts/build.py`. Edite lá e rode:

```bash
python3 scripts/build.py
```

O que mais muda no dia a dia:

- **PCs à venda**: lista `PCS` (nome, processador, placa de vídeo, preço). Atualiza vitrine, schema de produto e `llms.txt` de uma vez.
- **Domínio**: constante `SITE`. Hoje está `https://www.kappelinformatica.com.br` (provisório). Trocar antes do deploy, porque canonical, sitemap, Open Graph e schema usam esse valor.
- **FAQ**: `HOME_FAQ`, `PC_FAQ` e o campo `faq` de cada página de serviço (vira FAQPage no schema).
- **Contato e endereço**: constantes no topo do script.

## SEO e GEO incluídos

- Title e meta description por página, com foco em "assistência técnica Tijucas" e cauda longa por serviço.
- Schema.org em JSON-LD: `ComputerStore`/`LocalBusiness` (endereço, área atendida com as 7 cidades, horário, pagamento, Instagram e Facebook), `Service`, `Product` + `Offer` para cada PC, `FAQPage`, `BreadcrumbList` e `WebSite`.
- `sitemap.xml`, `robots.txt` liberando buscadores e crawlers de IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended etc.) e `llms.txt` com os fatos do negócio em texto limpo para assistentes de IA.
- Open Graph e Twitter Card com imagem 1200×630 (`assets/img/og-kappel.jpg`).
- Fontes auto-hospedadas com preload, imagens em SVG, JS mínimo e animações que respeitam `prefers-reduced-motion`.
- Botões de WhatsApp com mensagem pré-preenchida por serviço e por PC. O formulário de troca monta a mensagem e abre o WhatsApp.

## Deploy na Vercel

O projeto já vem configurado (`vercel.json` + `.vercelignore`). Não tem build nem dependência: a Vercel publica os arquivos da raiz.

1. Na Vercel: **Add New → Project → Import** o repositório `kappelinformatica`.
2. Framework Preset: **Other**. Deixe Build Command, Install Command e Output Directory como estão (o `vercel.json` já define).
3. **Deploy**.
4. Em **Settings → Domains**, adicione `www.seudominio.com.br` e `seudominio.com.br`, deixando o domínio sem www redirecionando para o www. Se o domínio final for outro, troque a constante `SITE` em `scripts/build.py`, rode o build e faça commit antes.

O que o `vercel.json` faz:

- **URLs limpas com barra no final** (`/pc-gamer/`), iguais ao canonical e ao sitemap, sem conteúdo duplicado.
- **Noindex automático em `*.vercel.app`**: as URLs de prévia da Vercel não entram no Google, só o domínio oficial.
- **Cache**: fontes, CSS e JS por 1 ano (o build coloca `?v=hash` no CSS e no JS, então toda alteração já chega no visitante); imagens por 7 dias.
- **Cabeçalhos de segurança**: nosniff, referrer policy, bloqueio de iframe externo e permissões de câmera, microfone e localização desligadas.
- **Atalhos curtos** para bio, QR code e cartão de visita:
  - `/whatsapp` (ou `/zap`) abre o WhatsApp com a mensagem de orçamento
  - `/troca` leva ao formulário de troca de usado
  - `/pc` leva à vitrine de PC Gamer
  - `/contato` e `/servicos` levam às seções da home
- **404 personalizado** (`404.html`).

Depois de publicar:

1. Cadastrar o domínio no Google Search Console e enviar `/sitemap.xml`.
2. Criar ou reivindicar o Perfil da Empresa no Google com o mesmo nome, endereço e telefone do site, e colocar o link do site nele.
3. Colocar o link do site na bio do Instagram (ou `seudominio.com.br/whatsapp` direto).
4. Ativar GA4 e Meta Pixel: os snippets estão comentados no `<head>` dentro de `scripts/build.py` (função `head`). Se preferir, ative também o Vercel Web Analytics no painel do projeto.

## Pendências com o cliente

- [ ] Domínio definitivo (atualizar `SITE`)
- [ ] Logo oficial em vetor (`assets/img/logo.svg` é uma vetorização feita a partir da arte; trocar pelo arquivo original e rodar o build para regenerar os PNGs se quiser)
- [ ] Confirmar se "24 horas" é atendimento presencial ou plantão no WhatsApp (o site diz "24 horas pelo WhatsApp" e o schema marca 24/7)
- [ ] Prazo de garantia dos serviços (só a garantia de 3 meses dos PCs está confirmada)
- [ ] Área exata do leva e traz
- [ ] Confirmar se faz manutenção preventiva para empresas (citada na página de empresas como limpeza e manutenção)
- [ ] PCs em estoque hoje e configuração completa (memória, SSD, fonte)
- [ ] Nome e foto do responsável e fotos reais da bancada (dar rosto ao negócio)
- [ ] Autorização para citar clientes marcados nos posts e prints do destaque "Clientes"
- [ ] CNPJ para o rodapé
- [ ] Corrigir o DDD (48) na legenda do post de limpeza no Instagram
