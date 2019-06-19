##Ejercicio9
print('ingrese la cadena de texto')
Cadena = input('->')

Cadena = Cadena.replace(' ','')

print(f'Cadena: {Cadena}')
print(f'Largo: {len(Cadena)}')


##########################################################33

print('###################################')

print('ingrese la cadena de texto')
Cadena = input('->')

Cadena2 = ''

for i in Cadena:
	if i != ' ':
		Cadena2 += i
		
print(f'Cadena final: {Cadena2}')
print(f'Cadena Largo: {len(Cadena2)}')