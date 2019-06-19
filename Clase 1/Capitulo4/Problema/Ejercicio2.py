##Ejercicio2

Lista = list(range(1,11))

print(f'Los valores de la lista:')
for i in Lista:
		print(i,end = '-')

print('\nIngrese un numero')
Numero = int(input('->'))

for Indice,i in enumerate(Lista):
	Lista[Indice] *= Numero
	Indice +=1

print(f'la lista actual {Lista}')