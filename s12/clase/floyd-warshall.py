#!/usr/bin/python3.7

n, m, q = map(int, input().split())
inf = 10**18

d = [[inf]*n for i in range(n)]

for i in range(n):
    d[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    d[u][v] = min(d[u][v], w)
    d[v][u] = min(d[v][u], w)

# inf - x < inf computacionalmente hablando
# matematicamente, es incorrecto

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] == inf or d[k][j] == inf: continue
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    dist = d[u][v]
    if dist == inf:
        print(-1)
    else:
        print(dist)
