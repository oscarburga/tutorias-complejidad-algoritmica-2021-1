#!/usr/bin/python3.7
from random import randint
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

from collections import deque

n, m = map(int, input().split())
mat = [input() for _ in range(n)]
moves = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]

vis = [[False for _ in range(m)] for _ in range(n)]
last_move = [[None for _ in range(m)] for _ in range(n)]

def valid(pos):
    row, col = pos
    return (row >= 0) and \
            (row < n) and \
            (col >= 0) and \
            (col < m) and \
            (mat[row][col] != '#') and \
            (vis[row][col] == False)


start, goal = (-1, -1), (-1, -1)

for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == 'A': start = (i, j)
        if cell == 'B': goal = (i, j)

q = deque([start])
vis[start[0]][start[1]] = True

def reconstruct_path():
    row, col = goal
    ans = []
    while (row, col) != start:
        mv = last_move[row][col]
        ans.append(mv[2])
        row -= mv[0]
        col -= mv[1]
    ans.reverse()
    print("YES")
    print(len(ans))
    print(''.join(ans))



while len(q):
    row, col = q.popleft()
    if (row, col) == goal:
        reconstruct_path()
        exit(0)
    for i, move in enumerate(moves):
        new_pos = (row + move[0], col + move[1])
        new_row, new_col = new_pos
        if valid(new_pos):
            vis[new_row][new_col] = True
            last_move[new_row][new_col] = move
            q.append(new_pos)

print("NO")
