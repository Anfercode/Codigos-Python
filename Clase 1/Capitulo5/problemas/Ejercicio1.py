### Ejercicio 1

print('Ingrese la primera palabra:')
Palabra1 = input('->')


print('Ingrese la segunda palabra:')
Palabra2 = input('->')

if len(Palabra1) > len(Palabra2):
	print('La palabra 1 es mayor')
elif len(Palabra2) > len(Palabra1):
	print('La palabra 2 es mayor')	
else:
	print('Las 2 palabras son igual de largas')