#!/usr/bin/python3.7

import math
tc = int(input())

def sq_dist(p, q): # Distancia entre dos puntos
    return ((q[0]-p[0])**2 + (q[1]-p[1])**2)

for _ in range(tc): # Para cada caso de prueba
    # Lectura de input
    P, K = map(int, input().split())
    red, blue = [], []
    for _ in range(P):
        x, y, c = input().split()
        x, y = int(x), int(y)
        c = int(c == 'azul')
        if c == 0: red.append((x, y))
        else: blue.append((x, y))

    inf = 10**18
    blue_free = [True] * len(blue)

    def solve(cur, cnt, mx) -> int:
        if cur == len(red): 
            return mx if cnt >= K else inf

        #opcion 1: no matchear este con nadie
        ret = solve(cur+1, cnt, mx)

        #opcion 2: tratar de matchear con cualquiera libre
        for i, is_free in enumerate(blue_free):
            if is_free:
                blue_free[i] = False
                ret = min(ret, solve(cur+1, cnt+1, max(mx, sq_dist(red[cur], blue[i]))))
                blue_free[i] = True
        return ret
    
    ans = solve(0, 0, 0)
    if ans >= inf: print('Imposible')
    else: print(math.ceil(math.sqrt(ans)))
