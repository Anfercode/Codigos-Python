#Problema 1

print('\n')

Num1 = int(input('Numero 1 -> '))
Num2 = int(input('Numero 2 -> '))

if Num1 % 2 == 0 and Num2 % 2 == 0:	
	print('Ambos numeros son pares')
elif Num1 % 2 == 0 and Num2 % 2 != 0:	
	print(f'el numero {Num1} es par')
elif Num1 % 2 != 0 and Num2 % 2 == 0:	
	print(f'el numero {Num2} es par')
else:
	print('Ningun numero es par')
	
print('\n')
print('######################')	
print('###FIN DEL PROGRAMA###')	
print('######################')	