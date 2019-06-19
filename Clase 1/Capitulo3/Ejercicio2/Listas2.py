#Listas parte 2

# Metodo append

print('######### Append ################')

Lista = ['Lunes','Martes','Miercoles','Jueves','Viernes']

Lista.append('Sabado')
Lista.append('Domingo')
print(Lista)
print(len(Lista)) #Longitud lista

print('##################################')

#Metodo insert

print('############insert##############')
Lista2 = ['Lunes','Martes','Jueves','Viernes']

Lista2.insert(2,'Miercoles')
print(Lista2)
print(len(Lista2)) #Longitud lista

print('#################################')

print('############extend##############')
Lista3 = ['Lunes','Martes','Jueves','Viernes']

Lista3.extend(['Sabado','Domingo'])
print(Lista3)
print(len(Lista3)) #Longitud lista

print('################################')

#Suma Listas

print('#############Suma#############')

ListaA = ['Lunes','Martes']
ListaB = ['Miercoles','Jueves']

ListaC = ListaA + ListaB

print(ListaC)
print(len(ListaC)) #Longitud lista
print('################################')

print('############Buscar#############')

Lista3 = ['Lunes','Martes','Jueves','Viernes']

print('Lunes' in Lista3)
print(10 in Lista3)

print('###############################')

print('#############Indice############')

Lista3 = ['Lunes','Martes','Jueves','Viernes']

print(Lista3.index('Lunes'))

print('###############################')

print('############duplicados#########')

Lista3 = ['Lunes','Martes','Jueves','Viernes','Lunes']

print(Lista3.count('Lunes'))

print('###############################')

print('##########Eliminar comn pop#########')

Lista3 = ['Lunes','Martes','Jueves','Viernes','Lunes']

Lista3.pop()

print(Lista3)

Lista3.pop(1)

print(Lista3)

print('###########################')


print('##########Eliminar con remove#########')

Lista3 = ['Lunes','Martes','Jueves','Viernes','Lunes']

Lista3.remove('Lunes')

print(Lista3)

print('###########################')

print('##########Eliminar con clear#########')

Lista3 = ['Lunes','Martes','Jueves','Viernes','Lunes']

Lista3.clear()

print(Lista3)

print('###########################')

print('##########Invertir#########')

Lista3 = ['Lunes','Martes','Jueves','Viernes','Lunes']

Lista3.reverse()

print(Lista3)

print('##########################')

print('##########Multiplicar valores#########')

Lista3 = ['Lunes','Martes','Jueves','Viernes','Lunes']*2

Lista3.reverse()

print(Lista3)

print('##########################')

print('##########ordenar valores#########')

Lista3 = [2,5,6,8,9,7,10]

Lista3.sort()

print(Lista3)

Lista3.sort(reverse=True)

print(Lista3)

print('##########################')
