## Ejercicio 4

def Factorial(num1):
	if num1 > 0:
		f = num1 * Factorial(num1 - 1)
	else:
		f = 1
		
	return f
	
a = int(input('Ingrese un numero -> '))
		
print(Factorial(a))

