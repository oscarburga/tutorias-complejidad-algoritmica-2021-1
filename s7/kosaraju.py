#!/usr/bin/python3.7
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
rev = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append(y)
    rev[y].append(x)

vis = [False] * n
topo = []

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

vis = [False] * n
idx = [-1] * n

def dfs_scc(v, cur_idx):
    vis[v] = True
    idx[v] = cur_idx
    for e in rev[v]:
        if not vis[e]:
            dfs_scc(e, cur_idx)

cnt = 0
for x in topo:
    if not vis[x]:
        cnt += 1
        dfs_scc(x, cnt)

print(cnt)
for x in idx:
    print(x, end=' ')

