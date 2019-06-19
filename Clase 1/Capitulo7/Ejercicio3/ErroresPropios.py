## Lanzar propias excepciones

def ValidandoEdad(Edad):
	if edad<0:
		raise ValueError ('La edad no puede ser negativa')
	elif edad<18:
		print('Eres muy joven')
	elif edad<30:
		print('Eres joven')
	elif edad<50:
		print('Eres Maduro')

while True:
	
	edad = int(input('Ingrese su edad: '))
	
	try:
		ValidandoEdad(edad)
	except ValueError as EdadNegativa:
		print('Error -> Edad Negativa')

print('Programa terminado')
		