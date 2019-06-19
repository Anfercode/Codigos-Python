## Ejercicio 6

print('Ingrese un numero:')
Numero = int(input('->'))
Respuesta = 0
Lista = []

for i in range(1,11):
	Respuesta = i * Numero
	Lista.append(f'{Numero} * {i} = {Respuesta}')

print(Lista)

print('Fin del programa')

print('#####################')

print('Ingrese un numero:')
Numero = int(input('->'))

Lista = []

for i in range(1,11):
	 Lista.append(i*Numero)

print(f'La tabla es {Lista}')	 
	 
