from Lectura import *
from Escritura import *

Ruta = input('Inserte ruta: ')
Archivo = input('Inserte nombre archivo (Sin extenciones): ')

while True:
	print('1. Añadir contacto')
	print('2. Mostrar Contactos')
	print('3. Salir')
          
	opcion = int(input('Ingrese su opcion:'))
	
	if opcion == 1:
		Escritura = GenerarArchivo()
		Escritura.CrearAgenda(Ruta,Archivo)
	elif opcion == 2:
		Lectura = LecturaArchivo()
		Lectura.LeerAgenda(Ruta,Archivo)
	elif opcion == 3:
		print('Fin del programa')
		break



