#!/usr/bin/python3.7
from random import randint
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

from collections import deque # muy similar a una cola

# deque es double-ended queue

n, m = map(int, input().split())

# n, m = [int(x) for x in input().split()]

# la función map(f, args)
# map aplica la funcion 'f' a todos los elementos de args
# y lo retorna como una lista

mat = [input() for _ in range(n)]
vis = [[False for _ in range(m)] for _ in range(n)]

moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def valid(pos):
    row, col = pos
    # Qué debo validar?
    # La posicion a la que estoy tratando de moverme debe:
    # 1: Estar dentro del tablero
    # 2: No debe haber sido visitada antes
    # 3: No debe ser una pared
    return (row >= 0) and \
            (row < n) and \
            (col >= 0) and \
            (col < m) and \
            (vis[row][col] == False) and \
            (mat[row][col] != '#')


def bfs(start):
    q = deque([ start ])
    vis[start[0]][start[1]] = True
    # loop principal
    while len(q) > 0:
        # pos = (fila, columna)
        pos = q.popleft() # pos es un par de 2 elementos
        for move in moves:
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            if valid(new_pos):
                vis[new_pos[0]][new_pos[1]] = True
                q.append(new_pos)

cnt = 0
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell != '#' and (vis[i][j] == False):
            bfs((i, j))
            cnt += 1

print(cnt)
