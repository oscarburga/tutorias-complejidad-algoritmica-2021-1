#!/usr/bin/python3.7

# https://cses.fi/problemset/task/1694

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
cap = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, input().split())
    x -= 1
    y -= 1
    cap[x][y] += w
    adj[x].append(y)
    adj[y].append(x)

global vis
vis = [False] * n

def dfs(v, f): #vertice, flujo
    vis[v] = True
    if v == n-1:
        return f
    for e in adj[v]:
        if not vis[e] and cap[v][e] > 0:
            new_flow = min(cap[v][e], f)
            sent_flow = dfs(e, new_flow)
            if sent_flow > 0:
                cap[v][e] -= sent_flow
                cap[e][v] += sent_flow
                return sent_flow
    return 0

def ford_fulkerson():
    global vis
    inf = 10**18
    flow = 0
    while True:
        vis = [False] * n
        added_flow = dfs(0, inf)
        if added_flow == 0: # no hay camino aumentante
            return flow
        flow += added_flow

print(ford_fulkerson())
