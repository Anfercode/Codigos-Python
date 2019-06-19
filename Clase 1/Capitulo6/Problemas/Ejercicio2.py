## Ejercicio 2

def Rectangulo(Anch,Alt):
	for i in range(Alt):
		for j in range(Anch):
			print('*',end = '')
		print('')

print('Ingrese la ancho del rectangulo')
Ancho = int(input('->'))
print('Ingrese la altura del rectangulo')
Alto = int(input('->'))

Rectangulo(Ancho,Alto)
