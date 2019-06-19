#Diccionarios

diccionario = {'azul':'blue','rojo':'red','verde':'green'}

diccionario['Amarillo'] = 'yellow'
diccionario['azul'] = 'BLUE'

del(diccionario['verde'])

print(diccionario['azul'])
print(diccionario['rojo'])
print(diccionario)

################################################

datos = {'Andres':{'edad':20,'estatura':1.71},'Miguel':[30,1.65],'Raul':[20,1.60]}

print(datos)
print(datos['Andres'])
