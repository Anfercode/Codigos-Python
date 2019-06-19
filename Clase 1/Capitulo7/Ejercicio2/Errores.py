## Ejemplo multiples excepciones

def Dividir():
	while True:
		try:
			Num1 = float(input('Digite el primer numero:'))
			Num2 = float(input('Digite el segundo numero:'))
			resultado = Num1/Num2
			print(f'El resultado de la division es {resultado:.2f}')
			break
		except ValueError:
			print('Error -> Digite correctamente los valores numericos')
			
		except ZeroDivisionError:
			print('Error -> No se puede realizar la division entre 0')
		
		except KeyboardInterrupt:
			print('\n')
			print('A salido del programa')
			break
			
		except EOFError:
			print('Error -> La combinacion de caracteres no es adecuada')
			
Dividir()
	