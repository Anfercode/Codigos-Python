import os
 
class GenerarArchivo:
	def CrearAgenda(self,Ruta,Archivo):
		Arch = open(f"{Ruta}/{Archivo}.txt", "w")
		id = 1
		for i in range(11):
			print(f'\t.:{id}:.')
			print('Ingrese nombre')
			Nombre = input('->')
			
			print('Ingrese edad')
			Edad = input('->')
			
			print('Ingrese Telefono')
			Telefono = input('->')
			
			print('Ingrese Celular')
			Celular = input('->')
			
			print('Ingrese Email')
			Email = input('->')
			
			print('======================') 
			Arch.write(f"{id},{Nombre},{Edad},{Telefono},{Celular},{Email}" + os.linesep)
			id += 1
		Arch.close()
		
	