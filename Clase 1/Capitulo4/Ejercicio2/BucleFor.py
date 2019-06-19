#Bucle For
## itera con colecciones de datos(listas,conjuntos,tuplas,diccionarios)
##


##Lista

Lista = ['jose',2,3,True,5]

for i in Lista:
	print(f'El elemento de la Lista: {i}')
	#print('Hola mundo')
	
##Tuplas 

Tupla = ('jose',2,3,True,5)

for i in Tupla:
	print(f'El elemento de la Tupla: {i}')
	#print('Hola mundo')
	
##Conjuntos 

Conjunto = {'jose',2,3,True,5}

for i in Conjunto:
	print(f'El elemento de el Conjunto: {i}')
	#print('Hola mundo')
	
##Diccionarios

Diccionario = {'jose':22,'Miguel':12,'Raul':26}

for i in Diccionario:
	print(f'El elemento de el Diccionario:{i} -> {Diccionario[i]}')
	#print('Hola mundo')
	

for clave,valor in Diccionario.items():
	print(f'{clave} -> {valor}')
	#print('Hola mundo')
	
	
##CAdenas de texto

Cadena = 'Miguel'

for i in Cadena:
	print(f'{i}')
	#print('Hola mundo')
for i in Cadena:
	print(f'{i}',end = ' ')
	#print('Hola mundo')


	
