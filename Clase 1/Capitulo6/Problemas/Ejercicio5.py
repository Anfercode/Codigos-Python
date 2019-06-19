## Ejercicio 5

def SumaRecursiva(Num):
	if Num == 0:
		f = 0
	else:
		f = SumaRecursiva(round(Num/10)) + (Num%10)
	return f
	
a = int(input('Ingrese un numero -> '))
	
print(SumaRecursiva(a))
		