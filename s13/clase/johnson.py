# Testeado en Eolymp https://www.e-olymp.com/en/problems/974
inf = 10**18

n = int(input())

#visistados, distancias finales, pesos de las aristas y funcion potencial
vis = [[False for j in range(n)] for i in range(n)]
d = [[inf for i in range(n)] for j in range(n)]
w = [[] for i in range(n)]
h = [0] * n

for i in range(n):
    w[i] = [int(x) for x in input().split()]
	
# bellman (en este caso asumo que no hay ciclos negativos)
# en el caso general, se debe verificar que no exista ningun ciclo 
# negativo o finalizar la ejecucion del algoritmo si es que existe
for i in range(n-1):
    for u in range(n):
        for v in range(n):
            if w[u][v] < inf:
                h[v] = min(h[v], h[u] + w[u][v])

# nuevos pesos de las aristas usando la funcion potencial
for u in range(n):
    for v in range(n):
        if w[u][v] < inf: 
            w[u][v] += h[u] - h[v]
			
# Dijkstra con cola de prioridad (O(ElogV) por ejecucion)
# Para el ejemplo del e-olymp tenemos E = V^2 así que no es lo óptimo

import heapq as pq
for src in range(n):
    d[src][src] = 0
    q = []
    pq.heappush(q, (0, src))
    while len(q) > 0:
        c, u = pq.heappop(q)
        if vis[src][u]: continue
        vis[src][u] = True
        for v, peso in enumerate(w[u]):
            if peso >= inf: continue # no hay arista
            if d[src][u] + peso < d[src][v]:
                d[src][v] = d[src][u] + peso
                pq.heappush(q, (d[src][v], v))
    #restaurar pesos
    for i in range(n):
        d[src][i] += h[i] - h[src]

for i in range(n):
    for j in range(n):
        print(d[i][j], end = ' ')
    print()

