print('#################')
print('#####Cajero######')
print('#################')

Saldo = 1000

while True:
	print('\t Menu')
	print('1. ingresar dinero')
	print('2. retirar dinero')
	print('3. Mostrar dinero')
	print('4. Salir')
	opcion = int(input('-> '))
	print('\n')
	
	if opcion == 1:
		print('ingrese la cantidad de dinero')
		Cantidad = int(input('-> '))
		Saldo += Cantidad
		print(f'su Saldo actual es {Saldo}\n')
	elif opcion == 2:
		print('ingrese la cantidad de dinero')
		Cantidad = int(input('-> '))
		if Cantidad > Saldo:
			print('No tiene dinero suficiente\n')
		else:	
			Saldo -= Cantidad		
			print(f'Usted retiro {Cantidad}')
			print(f'su Saldo actual es {Saldo}\n')
	elif opcion == 3:
		print(f'su Saldo actual es {Saldo}\n')
	elif opcion == 4:
		print('Gracias por usarnos')
		break
	else:
		print('Valor incorrecto')
	
print('\n')
print('######################')	
print('###FIN DEL PROGRAMA###')	
print('######################')	