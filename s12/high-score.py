# https://cses.fi/problemset/task/1673/

inf = 10**18
n, m = map(int, input().split())

edges = []
dist = [inf] * n
changed = [False] * n

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((u, v, -w))

def bellman_step(): 
    for u, v, w in edges:
        if dist[u] == inf: continue
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            changed[v] = True

dist[0] = 0
for i in range(n):
    changed = [False] * n
    bellman_step()

def propagate_changes():
    for u, v, _ in edges:
        changed[v] |= changed[u]

if any(changed): # propagar el alcance del ciclo negativo
    for i in range(n):
        propagate_changes()

if changed[n-1]:
    print(-1)
else:
    print(-dist[n-1])
