#Ejercicio2

print('\n')

Num1 = int(input('Numero 1 -> '))
Num2 = int(input('Numero 2 -> '))
Num3 = int(input('Numero 3 -> '))

if Num1 == Num2:
	print(f'El numero {Num1} esta repetido')
elif Num1 == Num3:
	print(f'El numero {Num1} esta repetido')
elif Num2 == Num3:
	print(f'El numero {Num2} esta repetido')
elif Num1 > Num2 and Num1 > Num3:
	print(f'el numero {Num1} es mayor')
elif Num2 > Num1 and Num2 > Num3:
	print(f'el numero {Num2} es mayor')
elif Num3 > Num1 and Num3 > Num2:
	print(f'el numero {Num3} es mayor')
else:
	print(f'Todos los numeros son iguales')
	
print('\n')
print('######################')	
print('###FIN DEL PROGRAMA###')	
print('######################')	