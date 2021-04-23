#!/usr/bin/python3.7
from random import randint
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

from collections import deque 

n, m = map(int, input().split())
mat = [input() for _ in range(n)]

vis = [[False for _ in range(m)] for _ in range(n)]
last_move = [[None]*m for _ in range(n)]

moves = [(1,0,'D'), (-1,0,'U'), (0,-1,'L'), (0,1,'R')]

start, goal = (-1, -1), (-1, -1)

for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == 'A': start = (i, j)
        if cell == 'B': goal = (i, j)

def valid(pos):
    # Qué debo validar?
    # La posicion a la que estoy tratando de moverme debe:
    # 1: Estar dentro del tablero
    # 2: No debe haber sido visitada antes
    # 3: No debe ser una pared
    row, col = pos
    return (row >= 0) and \
            (row < n) and \
            (col >= 0) and \
            (col < m) and \
            (vis[row][col] == False) and \
            (mat[row][col] != '#')


def reconstruct_path():
    row, col = goal
    path = []
    while (row, col) != start:
        move = last_move[row][col]
        path.append(move[2])
        row -= move[0]
        col -= move[1]
    path.reverse()
    print("YES")
    print(len(path))
    print(''.join(path))


q = deque([ start ])
vis[start[0]][start[1]] = True

while len(q) > 0:
    pos = q.popleft() # pos es un par de 2 elementos

    if pos == goal:
        reconstruct_path()
        exit(0)

    for move in moves:
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if valid(new_pos):
            new_row, new_col = new_pos
            vis[new_row][new_col] = True
            last_move[new_row][new_col] = move
            q.append(new_pos)

print("NO")
