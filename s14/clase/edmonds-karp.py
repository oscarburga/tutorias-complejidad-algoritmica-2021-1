#!/usr/bin/python3.7
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

inf = 10**18
# math.inf es de tipo float
# aqui estamos usando puros enteros, 
# entonces mejor trabajemos al 100% con enteros
# buena practica: evitar convertir tipos de datos constantemente

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

# Matriz de capacidades:
# cap[u][v]: capacidad restante en la arista de u->v
cap = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, input().split())
    x -= 1
    y -= 1
    cap[x][y] += w
    adj[x].append(y)
    adj[y].append(x)

# ford-fulkerson: utilizamos DFS para hallar los caminos aumentantes
# recordar que un camino aumentante es simplemente un camino en el grafo
# residual que permite enviar un flujo positivo de la fuente al sumidero

# en este caso, la fuente es el vertice 0 y el sumidero es el vertice N-1

from collections import deque

def bfs(s, t): #vertice, flujo que esta llegando al vertice
    p = [-1] * n # arreglo de padres
    p[s] = -2
    q = deque()
    q.append((s, inf))
    while len(q):
        v, f = q.popleft()
        if v == t: 
            return f, p
        for e in adj[v]:
            if p[e] == -1 and cap[v][e]:
                p[e] = v
                new_flow = min(f, cap[v][e])
                q.append((e, new_flow))
    return 0, p

# Loop principal - ford fulkerson

flujo_total = 0
# mientras existe camino aumentante 
# enviar flujo por ese camino aumentante
while True:
    vis = [False] * n
    sent_flow, p = bfs(0, n-1)
    if sent_flow == 0: break
    flujo_total += sent_flow

    # a diferencia del ford fulkerson
    # ahora necesitamos actualizar manualmente
    # las capacidades del grafo residual luego del BFS
    v = n-1
    while v != 0:
        u = p[v]
        cap[u][v] -= sent_flow
        cap[v][u] += sent_flow
        v = u

print(flujo_total) 
