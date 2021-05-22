#!/usr/bin/python3.7

n = int(input())

p = [-1] * n #DSU - Padre
sz = [1] * n #DSU - Size (Tamano de componente)
mn = [None] * n #DSU - Minimo de la comp
mx = [None] * n #DSU - Maximo de la comp
ids = {}

def find(x): # asumo que x es el identificador de una persona
	if p[x] == -1: return x
	p[x] = find(p[x])
	return p[x]

def join(x, y): # x, y son los nombres de las personas
	x = find(ids[x])
	y = find(ids[y])

	if x == y: return

	# suposicion para union por tamano:
	# 'X' siempre va a ser la componente grande
	# si x no es la componente grande, entonces hacemos
	# un swap para que X ahora sea la grande y Y la pequeña

	if sz[x] < sz[y]:
	    x, y = y, x
	
	p[y] = x
	sz[x] += sz[y]
	mn[x] = min(mn[x], mn[y])
	mx[x] = max(mx[x], mx[y])

def are_friends(x, y): #x, y son los nombres de las personas
	return find(ids[x]) == find(ids[y])

def youngest(x): #x es nombre
	return mn[find(ids[x])]

def oldest(x): #x es nombre
	return mx[find(ids[x])]


# Leemos las N personas con sus edades
for i in range(n):
    name, age = input().split()
    age = int(age)
    # '10'
    # '7'
    ids[name] = i
    mn[i] = age
    mx[i] = age

# Leer cant de relaciones seguido de las relaciones
m = int(input())
for _ in range(m):
	x, y = input().split()
	# 'juan pepe'
	# el .split() por espacios
	# x, y = ['juan', 'pepe']
	join(x, y)

# Leer cant. de consultas y las consultas
q = int(input())
for _ in range(q):
	# friend x y -> responder si x, y son amigos
	# youngest x -> responder edad más joven en el circulo de amigos de x
	# oldest x -> responder edad mayor en el circulo de amigos de x
	line = input().split()
	
	if line[0] == 'friend':
		if are_friends(line[1], line[2]):
			print('yes')
		else: 
			print('no')

	elif line[0] == 'youngest':
		print(youngest(line[1]))
	
	elif line[0] == 'oldest':
		print(oldest(line[1]))
