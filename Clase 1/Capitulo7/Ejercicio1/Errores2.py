#Errores
while True:
	try: ##Prueba el error
		Numero = int(input('Digite un numero:'))
		
	except: ##Se ejecuta ciuando hay errores
		print('Ha ocurrido un error')
		
	else: ##Se ejecuta Cuando no hay errores
		print(f'La suma es {Numero + 1}')
		break
		
	finally: ##Siempre se va a ejecutar
		print('Iteracion finalizada')
		