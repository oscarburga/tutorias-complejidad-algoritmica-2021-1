#!/usr/bin/python3.7

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)
from collections import deque

def read_graph() -> list:
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x, y = [int(k)-1 for k in input().split()]
        adj[x].append(y)
    return adj

def get_topo_sort(adj: list):
    n = len(adj)

    in_degree = [0] * n
    
    # Calcular grados de entrada de cada vertice
    for v in range(n):
        for e in adj[v]:
            in_degree[e] += 1

    topo = []
    q = deque([v for v in range(n) if in_degree[v] == 0])
    # Nota: si hay ciclos, no retorna nodos alcanzables por ciclos
    # Esto quiere decir que si hay algun ciclo, len(topo) < n
    while len(q) > 0:
        v = q.popleft()
        topo.append(v)
        for e in adj[v]:
            in_degree[e] -= 1
            if in_degree[e] == 0:
                q.append(e)

    return topo

if __name__ == '__main__':
    adj = read_graph()
    topo = get_topo_sort(adj)
    if len(topo) < len(adj): print('IMPOSSIBLE')
    else: 
        for x in topo: 
            print(x+1, end=' \n'[x==topo[-1]])
    pass

