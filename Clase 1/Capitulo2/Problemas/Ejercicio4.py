#Ejercicio 4

print('\n')
print('Calculadora Aritmetica')
print('\n')

Num1 = int(input('Numero 1 -> '))
Num2 = int(input('Numero 2 -> '))

print('\n')
print('Seleccione la operacion deseada')
print('Suma            -> s')
print('Resta           -> r')
print('Multiplicacion  -> m')
print('Division        -> d')
print('\n')
operacion = input('->').upper()

if operacion == 'S':
	Resultado = Num1 + Num2
	print(f'{Num1} + {Num2} = {Resultado}')
elif operacion == 'R':	
	Resultado = Num1 - Num2
	print(f'{Num1} - {Num2} = {Resultado}')
elif operacion == 'M':	
	Resultado = Num1 * Num2
	print(f'{Num1} * {Num2} = {Resultado}')
elif operacion == 'D':	
	Resultado = Num1 / Num2
	print(f'{Num1} / {Num2} = {Resultado:.2f}')
else:
	print('Valor invalido')

print('\n')
print('######################')	
print('###FIN DEL PROGRAMA###')	
print('######################')	