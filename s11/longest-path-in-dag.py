#!/usr/bin/python3.7

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append((y, w))

vis = [False] * n
topo = []

def dfs_topo(v):
    vis[v] = True
    for e, _ in adj[v]:
        if not vis[e]:
            dfs_topo(e)
    topo.append(v)

for i in range(n):
    if not vis[i]:
        dfs_topo(i)

topo.reverse()

dp = [0] * n

for vertice in topo:
    for vecino, peso in adj[vertice]:
        dp[vecino] = max(dp[vecino], dp[vertice] + peso)

for i, dist in enumerate(dp):
    print(f'vertice {i+1} tiene distancia maxima {dist}')


