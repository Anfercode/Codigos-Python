### Ejercicio3

print('Ingrese una cadena')
Palabra = input('->')

Palabra = Palabra.replace(' ','')

Palindromo = Palabra[::-1]

print(f'La palabra es palindroma {Palindromo}')

if Palabra == Palindromo:
	print(f'La palabra es palindromo')
else:
	print(f'La palabra no es palindromo')

