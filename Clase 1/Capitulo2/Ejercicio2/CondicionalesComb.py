#Condiciones Combinadas

edad = int(input('Digite su edad: '))
if edad > 0 and edad < 110:
	if edad >= 18:
		print('Usted es mayor de edad')
	else:
		print('Usted es menor de edad')
else:
	print('Dato Incorrecto')

	