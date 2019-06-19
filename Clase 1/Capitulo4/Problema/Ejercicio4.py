## Ejercicio 4

print('Ingrese el numero de inicio')
Inicio = int(input('->'))

print('Ingrese el numero de Fin')
Final = int(input('->')) + 1

Valor = 0

for i in range(Inicio,Final):
	if i % 2 == 0:
		Valor += i
	
print(f'El total es {Valor}')	
	