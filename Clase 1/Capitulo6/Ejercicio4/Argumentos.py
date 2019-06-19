#### Argumentos por valor o por referencia

def doblar_valor(numero):
	numero *= 2
	print(numero)

def doblar_valor2(numero):
	return numero * 2
	
def doblar_valores(numeros):
	for i,n in enumerate(numeros):
		numeros[i] *= 2

l = [1,2,3,4,5,10]
n = 5
doblar_valor(n)

doblar_valores(l[:])
print(l)
doblar_valores(l)
print(l)

n = doblar_valor2(n)
print(n)

