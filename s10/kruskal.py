#!/usr/bin/python3.7

n, m = map(int, input().split())
edges = []

p = [-1] * n
sz = [1] * n

def find(x):
    if p[x] == -1: return x
    p[x] = find(p[x])
    return p[x]

def join(x, y):
    x, y = find(x), find(y)
    if x == y: return 0

    if sz[x] < sz[y]: 
        x, y = y, x

    p[y] = x
    sz[x] += sz[y]
    return 1

for _ in range(m):
    x, y, w = map(int, input().split())
    x -= 1
    y -= 1
    edges.append((w, x, y))

edges.sort()

MST = 0
cnt = 0

for edge in edges:
    union = join(edge[1], edge[2])
    MST += union * edge[0]
    cnt += union

if cnt == n-1:
    print(MST)
else: 
    print("IMPOSSIBLE")
