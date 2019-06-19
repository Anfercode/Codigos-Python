### funciones recursivas

def CuentaRegresiva(num):
	if num > 0:
		print(num)
		CuentaRegresiva(num - 1)
	else:
		print('boooom')
CuentaRegresiva(5)