#!/usr/bin/python3.7
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)


# https://cses.fi/problemset/task/1638

n = int(input())
mat = [input() for _ in range(n)]

mod = 10**9 + 7

# n = 1000
# mat = ['.'*n for _ in range(n)]

respuesta = [[None]*n for _ in range(n)]

def BT(r, c): #row, col
    if r >= n or c >= n: return 0 #me sali de la matriz
    if mat[r][c] == '*': return 0 #estoy en una trampa
    if (r, c) == (n-1, n-1): return 1 #llegué a la meta

    #Programacion dinamica
    if respuesta[r][c] != None: 
        return respuesta[r][c]

    ans = BT(r+1, c) + BT(r, c+1)
    ans %= mod
    respuesta[r][c] = ans
    return ans

print(BT(0, 0))
