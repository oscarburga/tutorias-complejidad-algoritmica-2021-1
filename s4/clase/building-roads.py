#!/usr/bin/python3.7
import sys
sys.setrecursionlimit(10**7)

# n = cantidad de vertices
# m = cantidad de aristas

n, m = [int(x) for x in input().split()]
adj = [[] for _ in range(n)]
vis = [False for _ in range(n)]

for i in range(m):
    u, v = [int(x) for x in input().split()]
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)
    # Detallito de implementación:
    # En vez de tener los nodos del 1 al N
    # Usamos del 0 al N-1


def dfs(v): # DFS normalito como siempre, nada especial
    vis[v] = True # primer paso siempre marcar como visitado!
    for vecino in adj[v]:
        if not vis[vecino]:
            dfs(vecino)

# Como ENCUENTRO las nuevas aristas que necesito añadir?
representantes = []
for i in range(n):
    if not vis[i]:
        dfs(i)
        representantes.append(i)

# sumo 1 a todos los representantes 
# para restaurar los índices originales ([1 ... N])

representantes = [x+1 for x in representantes]
cant_rep = len(representantes)
print(cant_rep-1)

for i in range(cant_rep-1):
    print(representantes[i], representantes[i+1])   

if __name__ == '__main__':
    pass

