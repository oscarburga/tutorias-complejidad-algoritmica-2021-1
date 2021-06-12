#!/usr/bin/python3.7

n, m = map(int, input().split())

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v, w))


inf = 10**18
dist = [inf] * n
dist[0] = 0

changed = [False] * n

for i in range(n):
    changed = [False] * n
    for u, v, w in edges:
        if dist[u] == inf: continue
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            changed[v] = True

for i in range(n-1):
    for u, v, _ in edges:
        changed[v] |= changed[u]
        #   '|='  es or-igual
        # para variables booleanas
        # es lo mismo que decir
        # changed[v] = changed[v] or changed[u]

print(changed)
print(dist)
