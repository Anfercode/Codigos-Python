##Ejercicio 10

print('ingrese la cadena de texto')
Cadena = input('->')

Cadena = Cadena.upper()

Lista = []

for i in Cadena:
	Lista.append(i)
	
Lista = list(set(Lista))
	
print(f'La lista de caracteres es: {Lista}')	


print(f'################################3')


print('ingrese la cadena de texto')
Cadena = input('->')

Cadena = Cadena.upper()

Lista = []

for i in Cadena:
	if i not in Lista:
		Lista.append(i)

print(f'La lista de caracteres es: {Lista}')