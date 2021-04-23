#!/usr/bin/python3.7
from random import randint
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

from collections import deque

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

def bfs(pos):
    q = deque([pos])
    vis[pos[0]][pos[1]] = True
    while len(q):
        row, col = q.popleft()
        for move in moves:
            new_pos = (row + move[0], col + move[1])
            if valid(new_pos):
                vis[new_pos[0]][new_pos[1]] = True
                q.append(new_pos)

cnt = 0
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if (cell != '#') and (vis[i][j] == False):
            bfs((i, j))
            cnt += 1

print(cnt)
