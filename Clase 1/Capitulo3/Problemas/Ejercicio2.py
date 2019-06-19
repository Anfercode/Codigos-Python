#Ejercicio 2

ListaA = [1,2,3,4,5]
ListaB = [4,5,6,7,8]

print(f'valores lista 1 {ListaA}')
print(f'valores lista 2 {ListaB}')

#Conjuntos

Conjunto1 = set(ListaA)
Conjunto2 = set(ListaB)

#Lista unida

ListaU = list(Conjunto1 | Conjunto2)

print(f'Lista unida {ListaU}')

#Lista Left

ListaL = list(Conjunto1 - Conjunto2)

print(f'Lista izquierda {ListaL}')

#Lista Right

ListaR = list(Conjunto2 - Conjunto1)

print(f'Lista derecha {ListaR}')

#Lista valores comunes

ListaI = list(Conjunto1 & Conjunto2)

print(f'Lista valores {ListaI}')