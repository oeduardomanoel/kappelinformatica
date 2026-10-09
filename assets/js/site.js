(function () {
  "use strict";

  var WHATS = "5547989289589";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Header ganha borda ao rolar
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Menu mobile
  var toggle = document.querySelector(".menu-toggle");
  var links = document.getElementById("nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      links.classList.toggle("is-open", !open);
    });
    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        toggle.setAttribute("aria-expanded", "false");
        links.classList.remove("is-open");
      }
    });
  }

  // Ano no rodapé
  var y = document.getElementById("ano");
  if (y) y.textContent = new Date().getFullYear();

  // Formulário de troca: monta a mensagem e abre o WhatsApp
  var form = document.getElementById("form-troca");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ""; };
      var msg = [
        "Oi, Kappel! Quero avaliar meu usado na troca.",
        "Aparelho: " + (v("troca-tipo") || "não informado"),
        "Modelo: " + (v("troca-modelo") || "não informado"),
        "Estado: " + (v("troca-estado") || "não informado"),
        "Cidade: " + (v("troca-cidade") || "não informada"),
        v("troca-obs") ? "Obs: " + v("troca-obs") : "",
        "Posso mandar as fotos por aqui."
      ].filter(Boolean).join("\n");
      window.location.href = "https://wa.me/" + WHATS + "?text=" + encodeURIComponent(msg);
    });
  }

  // Malha wireframe da marca (fundo do topo)
  var canvas = document.querySelector(".hero-mesh");
  if (!canvas || !canvas.getContext) return;
  var ctx = canvas.getContext("2d");
  var w = 0, h = 0, dpr = 1, t = 0, raf = 0, visible = true;

  function size() {
    var r = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = r.width; h = r.height;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    var rows = 22, cols = 46;
    var horizon = h * 0.34;
    for (var i = 0; i < rows; i++) {
      var p = i / (rows - 1);
      var depth = Math.pow(p, 1.8);
      var baseY = horizon + depth * (h * 0.78);
      var amp = 10 + depth * 46;
      ctx.beginPath();
      for (var j = 0; j <= cols; j++) {
        var q = j / cols;
        var spread = 0.55 + depth * 0.9;
        var x = w / 2 + (q - 0.5) * w * spread * 1.4;
        var yy = baseY
          + Math.sin(q * 6.2 + t * 0.6 + i * 0.35) * amp * 0.5
          + Math.cos(q * 3.1 - t * 0.4 + i * 0.2) * amp * 0.35;
        if (j === 0) ctx.moveTo(x, yy); else ctx.lineTo(x, yy);
      }
      ctx.strokeStyle = "rgba(243, 238, 230," + (0.04 + depth * 0.16).toFixed(3) + ")";
      ctx.lineWidth = 0.6 + depth * 0.6;
      ctx.stroke();
    }
  }

  function loop() {
    t += 0.012;
    draw();
    raf = visible ? requestAnimationFrame(loop) : 0;
  }

  size();
  draw();
  window.addEventListener("resize", function () { size(); draw(); });

  if (!reduce) {
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
        if (visible && !raf) raf = requestAnimationFrame(loop);
      }).observe(canvas);
    }
    raf = requestAnimationFrame(loop);
  }
})();
