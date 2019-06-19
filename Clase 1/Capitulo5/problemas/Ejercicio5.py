## Ejericicio 5 

print('Ingrese una cadena')
Palabra = input('->')

Palabra = Palabra.upper()

Conteo_A = Palabra.count('A')
Conteo_E = Palabra.count('E')
Conteo_I = Palabra.count('I')
Conteo_O = Palabra.count('O')
Conteo_U = Palabra.count('U')
Conteo_Total = Conteo_A + Conteo_E + Conteo_I + Conteo_O + Conteo_U

print(f'''\t.:Conteos:.
a = {Conteo_A}
e = {Conteo_E}
i = {Conteo_I}
o = {Conteo_O}
u = {Conteo_U}
Total = {Conteo_Total}''')