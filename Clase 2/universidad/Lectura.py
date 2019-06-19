import os
 
class LecturaArchivo:
	def LeerAgenda(self,Ruta,Archivo):
		Arch = open(f"{Ruta}\\{Archivo}.txt", "r")
		id = 1
		ListaContactos = []
		for i in Arch.readlines():
			ListaContactos = i.split(",")
			print(f'''\t.:{ListaContactos[0]}:.
Nombre...........{ListaContactos[1]}
Edad.............{ListaContactos[2]}
Telefono.........{ListaContactos[3]}
Celular..........{ListaContactos[4]}
Email............{ListaContactos[5]}''')
		Arch.close()
		
	