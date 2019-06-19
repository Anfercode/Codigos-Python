#BucleWhile

import math

print('digite un numero')
Numero = int(input('->'))

while Numero < 0:
	print('el numero es negativo')
	print('digite un numero')
	Numero = int(input('->'))
Rta = math.sqrt(Numero)
print(f'El resultado es {Rta:.2f}')

print('###############################################')

i = 0

while i < 10:
	print(f'{i + 1}. hola mundo')
	i += 1
	