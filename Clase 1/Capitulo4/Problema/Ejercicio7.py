## Ejercicio7

from random import randint, uniform, random

Aleatorio = randint(0,100)

print('Adivine el numero ingrese, ingrese un numero:')
Numero = int(input('->'))

Intentos = 0

while Aleatorio != Numero:
	
	Intentos += 1
	
	if Numero < Aleatorio:
		print('El numero es mayor')
		Numero = int(input('->'))
	elif Numero > Aleatorio:
		print('El numero es menor')
		Numero = int(input('->'))
	
print(f'Numero aleatorio es {Aleatorio}')
print(f'Intentos: {Intentos}')

print('#################################')

Aleatorio = randint(0,100)

print('\t Juego adivina el numero')

Contador = 0

while True:
	Numero = int(input('Digite un numero: '))
	Contador += 1
	if Numero > Aleatorio:
		print('\tNo es el numero, digita un numero menor')
	elif Numero <Aleatorio:
		print('\tNo es el numero, digita un numero mayor')
	else:
		print(f'\tFelicidades, adivinaste el numero {Aleatorio}')
		break
print(f'\nintentos: {Intentos}')