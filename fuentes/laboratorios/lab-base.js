/* Utilidades comunes de los laboratorios de SIO0010.
   Todo ocurre en el navegador: no hay peticiones de red ni almacenamiento persistente. */

const $  = id => document.getElementById(id);
const $$ = sel => Array.prototype.slice.call(document.querySelectorAll(sel));

/* ---------- bytes, hexadecimal y texto ---------- */
const UTF8 = new TextEncoder();
const DEC  = new TextDecoder();

function bytes(txt){ return UTF8.encode(txt); }
function texto(buf){ return DEC.decode(buf instanceof ArrayBuffer ? new Uint8Array(buf) : buf); }
function hex(buf){
  const b = buf instanceof ArrayBuffer ? new Uint8Array(buf) : buf;
  return Array.prototype.map.call(b, v => v.toString(16).padStart(2, "0")).join("");
}
function desdeHex(s){
  s = (s || "").replace(/[^0-9a-fA-F]/g, "");
  const b = new Uint8Array(s.length >> 1);
  for (let i = 0; i < b.length; i++) b[i] = parseInt(s.substr(i * 2, 2), 16);
  return b;
}
function aleatorio(n){ const b = new Uint8Array(n); crypto.getRandomValues(b); return b; }
function bloques(h, n){ return (h.match(new RegExp(".{1," + (n * 2) + "}", "g")) || []).join(" "); }

/* ---------- copiar bloques de comandos ---------- */
function montarCopias(){
  $$(".cmd").forEach(function(caja){
    if (caja.querySelector(".copiar")) return;
    const b = document.createElement("button");
    b.className = "copiar"; b.type = "button"; b.textContent = "copiar";
    b.addEventListener("click", function(){
      const t = caja.querySelector("pre").innerText;
      const listo = function(){ b.textContent = "copiado"; setTimeout(function(){ b.textContent = "copiar"; }, 1400); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(t).then(listo, function(){ manual(t, listo); });
      } else { manual(t, listo); }
    });
    caja.appendChild(b);
  });
  function manual(t, listo){          // sin permiso de portapapeles: selección manual
    const a = document.createElement("textarea");
    a.value = t; a.style.position = "fixed"; a.style.opacity = "0";
    document.body.appendChild(a); a.select();
    try { document.execCommand("copy"); listo(); } catch (e) {}
    document.body.removeChild(a);
  }
}

/* ---------- repaso de opción múltiple ----------
   preguntas: [[enunciado, respuesta, explicación], ...]   ·   opciones: ["A", "B", ...] */
function montarQuiz(cont, preguntas, opciones, idVer, idReset, idMarca){
  const caja = $(cont);
  const elegido = {};

  function pinta(){
    caja.innerHTML = "";
    preguntas.forEach(function(p, i){
      const d = document.createElement("div"); d.className = "preg";
      const q = document.createElement("div"); q.className = "q"; q.textContent = (i + 1) + ". " + p[0];
      const ops = document.createElement("div"); ops.className = "ops";
      opciones.forEach(function(o){
        const b = document.createElement("button"); b.type = "button"; b.textContent = o;
        if (elegido[i] === o) b.className = "elegida";
        b.addEventListener("click", function(){ elegido[i] = o; pinta(); marca(); });
        ops.appendChild(b);
      });
      const fb = document.createElement("div"); fb.className = "fb"; fb.id = cont + "-fb" + i;
      d.appendChild(q); d.appendChild(ops); d.appendChild(fb);
      caja.appendChild(d);
    });
  }
  function marca(){
    const n = Object.keys(elegido).length;
    if (idMarca) $(idMarca).textContent = n ? n + " de " + preguntas.length + " respondidas" : "";
  }
  function ver(){
    preguntas.forEach(function(p, i){
      const fb = $(cont + "-fb" + i);
      const bien = elegido[i] === p[1];
      fb.style.display = "block";
      fb.innerHTML = '<span class="' + (bien ? "ok" : "mal") + '">' + (bien ? "Correcto" : "Respuesta: " + p[1]) +
                     '</span> · <span style="color:var(--tinta-2)">' + p[2] + "</span>";
    });
  }
  function reinicia(){ for (const k in elegido) delete elegido[k]; pinta(); marca(); }

  if (idVer)   $(idVer).addEventListener("click", ver);
  if (idReset) $(idReset).addEventListener("click", reinicia);
  pinta();
}

/* ---------- cronómetro ---------- */
async function cronometra(fn){
  const t = performance.now();
  const r = await fn();
  return { ms: performance.now() - t, r: r };
}
function ms(v){ return v >= 1000 ? (v / 1000).toFixed(2) + " s" : v.toFixed(1) + " ms"; }

/* ---------- impresión: los desplegables salen abiertos ---------- */
function abreTodo(){ $$("details").forEach(function(d){ d.open = true; }); }
window.addEventListener("beforeprint", abreTodo);
if (window.matchMedia) {
  const mq = window.matchMedia("print");
  if (mq.addEventListener) mq.addEventListener("change", function(e){ if (e.matches) abreTodo(); });
}

document.addEventListener("DOMContentLoaded", montarCopias);
