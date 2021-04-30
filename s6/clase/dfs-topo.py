#!/usr/bin/python3.7
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

# cantidad de vertices y aristas
n, m = map(int, input().split())

# lista de adyacencia
adj = [[] for _ in range(n)]

for _ in range(m):
    x, y = [int(k)-1 for k in input().split()]
    adj[x].append(y)

# DFS para armar ord. topologico
# y detectar ciclos

color = [0] * n
topo = []

def dfs(v: int):
    color[v] = 1
    for e in adj[v]:
        if color[e] == 0:
            dfs(e)
        if color[e] == 1:
            # encontre un ciclo
            print('IMPOSSIBLE')
            exit(0)
        if color[e] == 2:
            #no hago nada
            pass
    topo.append(v)
    color[v] = 2

for v in range(n):
    if color[v] == 0:
        dfs(v)

topo.reverse()
for x in topo:
    print(x + 1, end=' ')
