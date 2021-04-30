#!/usr/bin/python3.7
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

import heapq as pq

# cantidad de vertices y aristas
n, m = map(int, input().split())

# lista de adyacencia
adj = [[] for _ in range(n)]

in_degree = [0] * n

for _ in range(m):
    x, y = [int(k)-1 for k in input().split()]
    adj[x].append(y)
    in_degree[y] += 1

topo = []

# Inicializar cola con vertices de grado 0
q = []
for v in range(n):
    if in_degree[v] == 0:
        pq.heappush(q, v)

while len(q):
    v = pq.heappop(q)
    topo.append(v)
    # simular que elimino 'v' del grafo
    for e in adj[v]:
        in_degree[e] -= 1
        # si el grado de entrada del vecino
        # se vuelve cero, lo agrego a la cola
        if in_degree[e] == 0:
            pq.heappush(q, e)

if len(topo) < n:
    print('IMPOSSIBLE')

else: 
    for x in topo:
        print(x + 1, end=' ')


