#!/usr/bin/python3.7

# https://cses.fi/problemset/task/1694

from collections import deque
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

inf = 10**18
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

def bfs(s, t): #vertice, flujo
    p = [-1] * n
    p[s] = -2
    q = deque()
    q.append((s, inf))
    while len(q) > 0:
        v, f = q.popleft()
        if v == t: 
            return f, p
        for e in adj[v]:
            if p[e] == -1 and cap[v][e] > 0:
                new_flow = min(f, cap[v][e])
                p[e] = v
                q.append((e, new_flow))
    return 0, p

def edmonds_karp():
    flow = 0
    while True:
        added_flow, p = bfs(0, n-1)
        if added_flow == 0: # no hay camino aumentante
            return flow
        flow += added_flow
        
        # actualizar capacidades del camino aumentante
        v = n-1
        while v != 0:
            u = p[v]
            cap[u][v] -= added_flow
            cap[v][u] += added_flow
            v = u

print(edmonds_karp())
