'''
And = Multiplicacion logica
or = Suma Logica
Not = Negacion
^ = Xor(O Exclucivo)

Orden

1-not
2-and
3-or
'''

a = 10 
b = 12
c = 13 
d = 10

Resultado = ((a > b) or (a < c))and((a == c) or (a >= b))

print(Resultado)

'''
#####################################################################
Prioridad ejecucion operadores Python 

1- ()
2- **
3- *, /, %, not
4- +, -, and
5- <, >, ==,>=,<=,!=,or

######################################################################
'''

a = 10
b = 15
c = 20

Resultado = ((a>b)and(b<c))
print(Resultado)

Resultado = ((a>b)or(b<c))
print(Resultado)

Resultado = ((a>b)^(b>c))
print(Resultado)

Resultado = not((a>b)^(b>c))
print(Resultado)