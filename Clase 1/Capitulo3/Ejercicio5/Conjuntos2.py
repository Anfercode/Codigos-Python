
a = {1,2,3}
b = {4,5,6}

print(a == b)

a = {1,2,3}
b = {3,2,1}

print(a == b)

print(len(a))
print(len(b))

# union

a = {1,2,3}
b = {4,5,6}

c = a | b

print(c)

# Interseccion

a = {1,2,3}
b = {2,3,6}

c = a & b

print(c)

# diferencia

a = {1,2,3}
b = {2,3,6}

c = a - b

print(c)

c = b - a

print(c)

#Diferencia simetrica

a = {1,2,3}
b = {2,3,6}

c = a ^ b
print(c)

#Determinar subconjuntos, superconjuntos y disconexos

a = {1,2,3}
b = {3,4,5}
c = {1,2,3,4,5}

print(a.issubset(c))
print(b.issubset(c))
print(c.issuperset(a))
print(c.issuperset(b))
print(a.isdisjoint(b))

#inmutable

a = frozenset({1,2,3})
b = {3,4,5}

a.add(8)