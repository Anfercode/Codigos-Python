## Ejercicio 1

Lista = []
i = 1

Lista = list(range(1,51))

##while i <= 50:
##	Lista.append(i)
##	i += 1
	
for i in Lista:
	if i != 50:
		print(i,end = '-')
	else:
		print(i)