## Ejericicio 5

print('Ingrese el numero a realizar el factorial')
Numero = int(input('->'))+1

Factorial = 1

if Numero < 0:
	print('El numero es negativo')
else:
	for i in range(1,Numero):
		Factorial *= i
	print(f'el factorial es {Factorial}')
		



######################################
##Solucion curso
######################################


print('########################################33')
Numero = int(input('Digite un numero:'))

while Numero < 0:
	print('Error -> El numero tiene que ser positivo')
	numero = int(input('Digite un numero:'))

Factorial = 1

for i in range(1,Numero+1):
	Factorial *= i
	
print(f'\nEl factorial es -> {Factorial}')
	