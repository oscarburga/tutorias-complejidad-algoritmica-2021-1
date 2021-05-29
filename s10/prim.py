#!/usr/bin/python3.7

import heapq as pq

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append((y, w))
    adj[y].append((x, w))

inf = 10**18
# c[v]: peso minimo de arista para llegar al vertice v
# vis[v]: True si v ya ha sido visitado
c = [inf] * n 
vis = [False] * n

# Vamos a empezar el Prim desde el vértice '0'
c[0] = 0

q = []
pq.heappush(q, (c[0], 0))

MST = 0
cnt = 0
while len(q):
    d, v = pq.heappop(q)
    if vis[v] == True:
        continue
    vis[v] = True
    MST += d
    cnt += 1
    for e, w in adj[v]:  # e: vertice vecino, w: peso de la arista
        if w < c[e]:
            c[e] = w
            pq.heappush(q, (w, e))

if cnt < n:
    print("IMPOSSIBLE")
else: 
    print(MST)

