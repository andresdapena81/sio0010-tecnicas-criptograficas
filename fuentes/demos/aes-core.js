/* AES-128 con captura de cada estado intermedio, para el demo paso a paso.
   Estado como arreglo de 16 bytes en orden por columnas: idx = fila + 4*col. */

const SBOX = (function(){
  // Genera la S-box de AES (inverso multiplicativo en GF(2^8) + transformación afín).
  const p = new Uint8Array(256), inv = new Uint8Array(256);
  let x = 1;
  for (let i = 0; i < 255; i++){ p[i] = x; x ^= (x << 1) ^ ((x & 0x80) ? 0x11b : 0); x &= 0xff; }
  for (let i = 0; i < 255; i++) inv[p[i]] = p[(255 - i) % 255];
  inv[0] = 0;
  const s = new Uint8Array(256);
  for (let i = 0; i < 256; i++){
    let b = inv[i], r = b;
    for (let k = 0; k < 4; k++){ b = ((b << 1) | (b >> 7)) & 0xff; r ^= b; }
    s[i] = r ^ 0x63;
  }
  return s;
})();

function mul(a, b){                       // multiplicación en GF(2^8)
  let r = 0;
  for (let i = 0; i < 8; i++){ if (b & 1) r ^= a; const hi = a & 0x80; a = (a << 1) & 0xff; if (hi) a ^= 0x1b; b >>= 1; }
  return r & 0xff;
}

const RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36];

function expandirLlave(key){              // key: 16 bytes → 11 round keys de 16 bytes (col-major)
  const w = [];                            // 44 palabras de 4 bytes
  for (let i = 0; i < 4; i++) w.push([key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]]);
  for (let i = 4; i < 44; i++){
    let t = w[i-1].slice();
    if (i % 4 === 0){
      t = [t[1], t[2], t[3], t[0]];                       // RotWord
      t = t.map(b => SBOX[b]);                            // SubWord
      t[0] ^= RCON[i/4 - 1];
    }
    w.push(w[i-4].map((b, j) => b ^ t[j]));
  }
  const rks = [];
  for (let r = 0; r < 11; r++){
    const rk = new Uint8Array(16);
    for (let c = 0; c < 4; c++) for (let fila = 0; fila < 4; fila++) rk[fila + 4*c] = w[4*r + c][fila];
    rks.push(rk);
  }
  return rks;
}

function subBytes(s){ const o = new Uint8Array(16); for (let i = 0; i < 16; i++) o[i] = SBOX[s[i]]; return o; }

function shiftRows(s){                     // fila r se corre a la izquierda r posiciones
  const o = new Uint8Array(16);
  for (let fila = 0; fila < 4; fila++) for (let c = 0; c < 4; c++) o[fila + 4*c] = s[fila + 4*((c + fila) % 4)];
  return o;
}

function mixColumns(s){
  const o = new Uint8Array(16);
  for (let c = 0; c < 4; c++){
    const a0 = s[4*c], a1 = s[4*c+1], a2 = s[4*c+2], a3 = s[4*c+3];
    o[4*c]   = mul(a0,2) ^ mul(a1,3) ^ a2 ^ a3;
    o[4*c+1] = a0 ^ mul(a1,2) ^ mul(a2,3) ^ a3;
    o[4*c+2] = a0 ^ a1 ^ mul(a2,2) ^ mul(a3,3);
    o[4*c+3] = mul(a0,3) ^ a1 ^ a2 ^ mul(a3,2);
  }
  return o;
}

function addRoundKey(s, rk){ const o = new Uint8Array(16); for (let i = 0; i < 16; i++) o[i] = s[i] ^ rk[i]; return o; }

/* Cifra un bloque y devuelve la traza: [{ronda, op, antes, despues, rk?}, ...] */
function cifrarConTraza(bloque, key){
  const rks = expandirLlave(key);
  const traza = [];
  let s = Uint8Array.from(bloque);
  const paso = (ronda, op, antes, despues, rk) =>
    traza.push({ ronda, op, antes: Uint8Array.from(antes), despues: Uint8Array.from(despues), rk: rk ? Uint8Array.from(rk) : null });

  let ns = addRoundKey(s, rks[0]); paso(0, "AddRoundKey", s, ns, rks[0]); s = ns;
  for (let r = 1; r <= 10; r++){
    ns = subBytes(s);        paso(r, "SubBytes", s, ns);       s = ns;
    ns = shiftRows(s);       paso(r, "ShiftRows", s, ns);      s = ns;
    if (r !== 10){ ns = mixColumns(s); paso(r, "MixColumns", s, ns); s = ns; }
    ns = addRoundKey(s, rks[r]); paso(r, "AddRoundKey", s, ns, rks[r]); s = ns;
  }
  return { traza, cifrado: s, rks };
}

if (typeof module !== "undefined") module.exports = { cifrarConTraza, expandirLlave, SBOX };
