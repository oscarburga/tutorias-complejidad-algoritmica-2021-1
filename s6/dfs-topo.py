#!/usr/bin/python3.7

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

def read_graph():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x, y = [int(k)-1 for k in input().split()]
        adj[x].append(y)
    return adj

def get_topo_sort(adj: list):
    n = len(adj)
    vis = [0] * n
    topo = []
    def dfs(v: int):
        vis[v] = 1
        for e in adj[v]:
            ## Si vis[e] == 2 ya fue visitado y terminado de procesar.
            ## En ese caso, no es necesario hacer nada

            if vis[e] == 0: 
                # No ha sido visitado nunca
                dfs(e)
            elif vis[e] == 1: 
                # Ya fue visitado y ahorita soy su descendiente
                # Aquí hay un ciclo, no existe ord. topologico
                print('IMPOSSIBLE')
                exit(0)
        vis[v] = 2
        topo.append(v)
    for i in range(n):
        if vis[i] == 0:
            dfs(i)
    topo.reverse()
    return topo

if __name__ == '__main__':
    topo = get_topo_sort(read_graph())
    for x in topo: print(x+1, end=' \n'[x==topo[-1]])
    pass

