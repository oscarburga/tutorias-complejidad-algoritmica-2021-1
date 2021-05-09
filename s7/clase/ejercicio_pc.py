#!/usr/bin/python3.7
import math

def distancia(p, q):
    return (q[0] - p[0])**2 + (q[1] - p[1])**2

# Leer input
tc = int(input()) # Cantidad de casos de prueba

for _ in range(tc):
    P, K = map(int, input().split())
    # P: Cantidad de puntos
    # K: Cantidad de vallas que debes construir
    red = []
    blue = []

    for _ in range(P):
        # Leer los P puntos
        x, y, color = input().split()
        x, y = int(x), int(y)
        if color == 'azul': blue.append((x, y))
        else: red.append((x, y))
    
    cant_azules = len(blue)
    azul_libre = [True] * cant_azules

    def solve(pos, cnt, max_dis):
        if pos == len(red):
            return max_dis if cnt >= K else float('inf')

        # Considerar las dos opciones: No crear valla, 
        # o probar creando vallas desde este punto

        # si no creo valla, no hago absolutamente nada, solo voy al sgte punto rojo
        ans = solve(pos+1, cnt, max_dis)
        
        # crear vallas -> tengo que marcar el punto azul como "no libre"
        for i in range(cant_azules):
            if azul_libre[i]: 
                azul_libre[i] = False
                temp = solve(pos+1, cnt+1, max(max_dis, distancia(red[pos], blue[i])))
                ans = min(ans, temp)
                azul_libre[i] = True

        return ans

    ans = solve(0, 0, 0)
    if ans == float('inf'): print('Imposible')
    # 5.3 -> 6
    # 5.0 -> 5
    # 5.00000000000000000000000001 -> 6
    else: print(math.ceil(math.sqrt(ans)))

        

