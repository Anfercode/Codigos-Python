#Ejercicio 1

Lista = [1,2,3,4,5,6,7,8,9,1,5,4,6]

print(f'la Lista tiene los siguientes valores {Lista}')

print('Ingrese un numero')
Numero = int(input('->'))

conteo = Lista.count(Numero)

if conteo > 1:
	Lista.remove(Numero)
	print('Valores borrados')
	print(Lista)
else:
	print(f'No hay duplicados por el valor {Numero}')
	print(Lista)

print('#############################################')

Lista = [1,2,3,4,5,6,7,8,9,1,5,4,6]

Lista = list(set(Lista))



print(Lista)