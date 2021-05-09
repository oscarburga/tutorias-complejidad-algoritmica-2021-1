#!/usr/bin/python3.7
from random import randint
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

# nodos, aristas
n, m = map(int, input().split())

adj = [[] for _ in range(n)]
rev = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append(y)
    rev[y].append(x)

### Fase 1
topo = []
vis = [False] * n

def dfs_topo(v):
    vis[v] = True
    for e in adj[v]:
        if not vis[e]:
            dfs_topo(e)
    topo.append(v)

for i in range(n):
    if not vis[i]:
        dfs_topo(i)

topo.reverse()

### Fase 2: DFSs en el grafo TRANSPUESTO en el orden generado por el ord. topológico
vis = [False] * n
color = [-1] * n

def dfs_scc(v, col): # Strongly Connected Component
    vis[v] = True
    color[v] = col
    for e in rev[v]: 
        if not vis[e]:
            dfs_scc(e, col)

cnt = 0
for x in topo:
    if not vis[x]:
        cnt += 1
        dfs_scc(x, cnt)

print(cnt)
for x in color:
    print(x, end=' ')
print()
