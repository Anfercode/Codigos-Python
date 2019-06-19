## Ejericicio1

def CambioADolar(num):
	return float(num * 0.00032)
	
def CambioAPesos(num):
	return float(num / 0.00032)

opcion = 0
	
while opcion != 3:		
	print('''
	.:Menu:.
1. pesos a dolares
2. dolares a pesos
3. Salir
''')
	opcion = int(input('->'))

	if opcion == 1:
		print('Ingrese el valor a convertir')
		Pesos = int(input('->'))
		if Pesos < 0:
			print('El valor es negativo')
		else:
			print(f'Su valor equivale a {CambioADolar(Pesos):.2f} Dolares')
	elif opcion == 2:	
		print('Ingrese el valor a convertir')
		Dolares = int(input('->'))
		if Dolares < 0:
			print('El valor es negativo')
		else:
			print(f'Su valor equivale a {CambioAPesos(Dolares):.2f} Pesos')
	elif opcion == 3:
		print('Gracias por usarnos')
	else:
		print('Valor incorrecto')
	