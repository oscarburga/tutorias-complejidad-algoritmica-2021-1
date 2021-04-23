#!/usr/bin/python3.7
from random import randint
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
mat = [input() for _ in range(n)]
vis = [[False for _ in range(m)] for _ in range(n)]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def valid(pos):
    row, col = pos
    return (row >= 0) and \
            (row < n) and \
            (col >= 0) and \
            (col < m) and \
            (mat[row][col] != '#') and \
            (vis[row][col] == False)

def dfs(pos):
    row, col = pos
    vis[row][col] = True
    for move in moves:
        new_pos = (row + move[0], col + move[1])
        if valid(new_pos):
            dfs(new_pos)

cnt = 0
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if (cell != '#') and (vis[i][j] == False):
            dfs((i, j))
            cnt += 1

print(cnt)
