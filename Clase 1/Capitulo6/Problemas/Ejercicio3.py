
def AgregarCliente(Lista,Nombre,Apellido,Documento):
	Cliente = {}
	Cliente['Nombre'] = Nombre
	Cliente['Apellido'] = Apellido
	Cliente['Documento'] = Documento
	Lista.append(Cliente)

def MostrarClientes(Lista):
	print('\t.:Clientes:.')
	for i in Lista:
		for j , k in i.items():
			print(f"{j}:{k}")
			print('#########################')

def MostrarCCCliente(Lista):
	print('Ingrese el documento')
	Doc = input('->')
	for i in Lista:
		if Doc in i['Documento']:
			print(f"Nombre:{i['Nombre']}")
			print(f"Apellido:{i['Apellido']}")
			print(f"CC:{i['Documento']}")
		else:
			print('Ese cliente no existe')

def BorrarCliente(Lista):
	print('Ingrese el nombre')
	Nombre = input('->')
	for i in Lista:
		if Nombre in i['Nombre']:
			Lista.remove(i)
			print('\ncliente borrado\n')
		else:
			print('Ese cliente no existe')
		
			
Clientes = []

while True:
	print('''.:Menu:.
1. Ingresar nuevo cliente
2. Mostrar todos los clientes
3  Mostrar cliente por Documento
4. Eliminar Cliente
5. Salir''')

	opcion = int(input('->'))
	
	if opcion == 1:
		Nombre = input('Nombre->')
		Apellido = input('Apellido->')
		CC = input('CC->')
		AgregarCliente(Clientes,Nombre,Apellido,CC)
	elif opcion == 2:
		MostrarClientes(Clientes)	
	elif opcion == 3:
		MostrarCCCliente(Clientes)
	elif opcion == 4:
		BorrarCliente(Clientes)
	elif opcion == 5:
		print('A salido satisfactoriamente')
		break
	else:
		print('Valor incorrecto')
		
	