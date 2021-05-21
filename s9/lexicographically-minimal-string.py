#!/usr/bin/python3.7

# Enlace del problema:
# https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/lexicographically-minimal-string-6edc1406/

a = input()
b = input()
c = input()

n = len(a)

def index(c) -> int: 
    return ord(c) - ord('a')
    # index('a') = 0, index('b') = 1 ...

def letter(i) -> str:
    return chr(i + ord('a'))
    # letter(0) = 'a', letter(1) = 'b' ...

p = [-1] * 26 # DSU - Parent
sz = [1] * 26 # DSU - Size (heuristica: tamano de componente)
mn = [letter(i) for i in range(26)] # DSU - Min. en la componente

def find(x):
    if p[x] == -1: return x
    p[x] = find(p[x])
    return p[x]

def join(x, y):
    x, y = find(index(x)), find(index(y))
    if x == y: return
    # Swap para que la comp de x siempre tenga tamaño mayor
    if sz[x] < sz[y]: 
        x, y = y, x

    p[y] = x
    sz[x] += sz[y]
    mn[x] = min(mn[x], mn[y])

def get_min(x):
    return mn[find(index(x))]

for x, y in zip(a, b):
    join(x, y)

ans = ''.join([get_min(x) for x in c])
print(ans)

