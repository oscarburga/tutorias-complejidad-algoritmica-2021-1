#!/usr/bin/python3.7

inf = 10**18
n, m, q = map(int, input().split())

d = [[inf]*n for _ in range(n)]
for i in range(n):
    d[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = min(d[a][b], c)
    d[b][a] = min(d[b][a], c)

# fijar vertice intermedio
#   fijar vertice inicio
#	fijar vertice fin
# 	    actualizar camino mas corto de inicio
#	    a fin, considerando ahora pasar por
#	    intermedio

for k in range(n):
    d_k = d[k]
    for i in range(n):
        d_i = d[i]
        for j in range(n):
            d_i[j] = min(d_i[j], d_i[k] + d_k[j])

for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if d[a][b] == inf:
        print(-1)
    else: print(d[a][b])
