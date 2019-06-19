## Funciones con retorno de valor

print('Inserte el primer numero')
a = int(input('->'))

print('Inserte el segundo numero')
b = int(input('->'))

def Multiplicar(Num1,Num2):
	Mult = Num1 * Num2
	return Mult

def prueba():
		return 'hola',45,[213212,6568,'hola']
	
c = Multiplicar(a,b)

print(c)

print(prueba())

c,n,l = prueba()

print(c)
print(n)
print(l)