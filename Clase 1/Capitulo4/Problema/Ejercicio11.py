### Ejercicio11

print('####################')
print('#####Contactos######')
print('####################')

Diccionario = {}

while True:
	print('\t Menu')
	print('1. Nuevo Contacto')
	print('2. Borrar Contacto')
	print('3. Ver Contactos')
	print('4. Salir')
	opcion = int(input('-> '))
	print('\n')
	
	if opcion == 1:
		
		print('Ingrese el Nombre del contacto')
		Nombre = input('-> ')
		print('Ingrese el Numero del contacto')
		Numero = int(input('-> '))
		
		if Nombre not in Diccionario:
			Diccionario[Nombre] = Numero
			print(f'Contacto guardado')
		else:
			print('El contacto ya existe')
		
	elif opcion == 2:
		
		print('Ingrese el Nombre')
		Borrado = input('->')
		
		if Borrado in Diccionario:
			del(Diccionario[Borrado])
			print('\nContacto borrado\n')
		else:
			print('Ese contacto no existe')
		
	elif opcion == 3:
		print('\nContactos\n')
		for Clave, Valor in Diccionario.items():
			print(f'Nombre: {Clave}')
			print(f'Numero: {Valor}')
			print('#####################\n')
	elif opcion == 4:
		print('A salido satisfactoriamente')
		break
	else:
		print('Valor incorrecto')
	
print('\n')
print('######################')	
print('###FIN DEL PROGRAMA###')	
print('######################')	