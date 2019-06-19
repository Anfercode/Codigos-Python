##Ejercicio 3


print('Inserte el numero en la lista')
valor = int(input('->'))

Lista = []
while valor != 0:
	Lista.append(valor)
	print('Inserte otro valor')
	valor = int(input('->'))
	
Lista.sort()

print(f'La lista ordenada es {Lista}')


############################################
#Solucion Elegante
############################################+

Lista = []

salir = False

while not salir:
	print('Inserte el numero en la lista')
	valor = int(input('->'))
	if valor == 0:
		salir = True
	else:
		Lista.append(valor)
	
	
Lista.sort()

print(f'La lista ordenada es {Lista}')


