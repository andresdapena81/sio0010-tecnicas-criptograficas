# -*- coding: utf-8 -*-
"""Renumera los antetítulos «// NN» de un guion de sesión, en orden de aparición."""
import io, re, sys
p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()
c = [0]
def rep(m):
    c[0] += 1
    return f'{m.group(1)}(p, "// {c[0]:02d}  {m.group(2)}'
s = re.sub(r'(base|glosario|fuentes|trabajo_independiente)\(p, "// \d+\s+([A-ZÁÉÍÓÚÑ])', rep, s)
io.open(p, "w", encoding="utf-8").write(s)
print(f"{p}: {c[0]} antetítulos renumerados")
