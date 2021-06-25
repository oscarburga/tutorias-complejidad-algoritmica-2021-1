#!/usr/bin/python3.7
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

inf = 10**18
# math.inf es de tipo float
# aqui estamos usando puros enteros, 
# entonces mejor trabajemos al 100% con enteros
# buena practica: evitar convertir tipos de datos constantemente

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

# Matriz de capacidades:
# cap[u][v]: capacidad restante en la arista de u->v
cap = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, input().split())
    x -= 1
    y -= 1
    cap[x][y] += w
    adj[x].append(y)
    adj[y].append(x)

# ford-fulkerson: utilizamos DFS para hallar los caminos aumentantes
# recordar que un camino aumentante es simplemente un camino en el grafo
# residual que permite enviar un flujo positivo de la fuente al sumidero

# en este caso, la fuente es el vertice 0 y el sumidero es el vertice N-1

vis = [False] * n
def dfs(v, f): #vertice, flujo que esta llegando al vertice
    # dfs(v, f) va a retornar el flujo que llegue al sumidero 
    # enviado desde este vertice
    vis[v] = True
    if v == n-1: # si el vertice actual es el sumidero
        return f #retorno el flujo que llegó aquí

    for e in adj[v]:
        if not vis[e] and cap[v][e] > 0:
            new_flow = min(f, cap[v][e])
            # sent_flow es el flujo que llega al sumidero
            sent_flow = dfs(e, new_flow) 
            if sent_flow > 0:
                cap[v][e] -= sent_flow
                cap[e][v] += sent_flow
                return sent_flow
    return 0


# Loop principal - ford fulkerson

flujo_total = 0
# mientras existe camino aumentante 
# enviar flujo por ese camino aumentante
while True:
    vis = [False] * n
    sent_flow = dfs(0, inf)
    if sent_flow == 0: break
    flujo_total += sent_flow

print(flujo_total) 
