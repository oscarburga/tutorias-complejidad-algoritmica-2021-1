# https://cses.fi/problemset/task/1672/
n, m, q = map(int, input().split())
inf = 10**18

d = [[inf] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    d[u][v] = min(d[u][v], w)
    d[v][u] = min(d[v][u], w)

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    dis = d[u][v]
    print(-1 if dis == inf else dis)
