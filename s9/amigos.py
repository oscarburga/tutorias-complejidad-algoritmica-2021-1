#!/usr/bin/python3.7

n = int(input('Ingrese cantidad de personas: '))

ids = {}
p = [-1] * n
sz = [1] * n
age_min = [-1] * n
age_max = [-1] * n

print(f'Ingrese {n} lineas, cada una con 2 valores: Nombre y edad de cada persona')
for i in range(n):
    name, age = input().split()
    age = int(age)
    ids[name] = i
    age_min[i] = age
    age_max[i] = age

# -------------
# Funciones DSU

def find(x):
    if p[x] == -1: return x
    p[x] = find(p[x])
    return p[x]

def join(x, y):
    x, y = find(ids[x]), find(ids[y])
    if x == y: return
    if sz[x] < sz[y]: 
        x, y = y, x
    p[y] = x
    sz[x] += sz[y]
    age_min[x] = min(age_min[x], age_min[y])
    age_max[x] = max(age_max[x], age_max[y])

def are_friends(x, y):
    return find(ids[x]) == find(ids[y])

# ------------

# Leer relaciones de amistad
m = int(input('Ingrese cantidad de relaciones de amistad: '))
print(f'Ingrese {m} lineas, cada una con 2 nombres')
for _ in range(m):
    name1, name2 = input().split()
    join(name1, name2)

# Leer las consultas
q = int(input('Ingrese la cantidad de consultas a realizar: '))
print('Las consultas son las siguientes:')
print('\t \"friends? a b\" responde si existe rel. de amistad entre a y b.')
print('\t \"youngest a\" responde la edad de la persona mas joven en el circulo de amistad de a.')
print('\t \"oldest a\" responde la edad de la persona mas vieja en el circulo de amistad de a.')

for _ in range(q):
    qs = input().split()
    if qs[0] == 'friends?':
        if are_friends(qs[1], qs[2]): print('yes')
        else: print('no')
    elif qs[0] == 'youngest':
        name = qs[1]
        print(age_min[find(ids[name])])
    elif qs[0] == 'oldest':
        name = qs[1]
        print(age_max[find(ids[name])])

