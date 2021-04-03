'''
Problema: 
    * Oscar está llevando su curso de Redes y Protocolo de Comunicaciones.
    * A Oscar le han gustado mucho las direcciones IPv4.
    * El formato de una dirección IPv4 es el siguiente: xxx.xxx.xxx.xxx

    Oscar tiene una cadena de N dígitos y quiere saber:
    ¿De cuantas formas puede Oscar separar su cadena en 4 partes no-vacías 
    para poder escribirla como si fuera una dirección IP? Imprímelas.
    
    En palabras simples: Genera todas las formas distintas de insertar 3 puntos en
    en una cadena, tal que no haya 2 puntos juntos, y junto a cada punto hayan digitos
    a sus dos costados.

    Diseñe un algoritmo de fuerza bruta cualquiera que solucione este problema.
    Diseñe un algoritmo con backtracking que solucione este problema.

'''

def fuerza_bruta(s) -> list:
    n = len(s)
    #Caso especial
    if n < 4: return []
    # Probar todas las tripletas posibles.
    # Nota: Estoy asumiendo que coloco el punto entre las posiciones i y i+1
    ans = []
    for i in range(0, n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                # Unir los cuatro rangos divididos por los puntos
                # Nota: s[L:R] considera el intervalo [L, R), abierto en R, por eso +1 en R
                t = '.'.join([ \
                            s[0:i+1], \
                            s[i+1:j+1], \
                            s[j+1:k+1], \
                            s[k+1:n] \
                        ])
                ans.append(t)
    return ans

def backtracking(s) -> list:
    s = list(s) # Convierto a lista para trabajarlo más fácil
    cur = [] # Cadena que estoy construyendo
    ans = [] # Respuesta
    n = len(s)
    def bt(pos, cnt): # Voy a forzar que máximo ponga 3 puntos para que mi complejidad no vuele

        cur.append(s[pos]) # Agrego la letra actual

        if pos == n-1:
            if cnt == 3: ans.append(''.join(cur)) # Agrego a la respuesta
            cur.pop(-1)
            return

        # Opción 1: No poner un punto y pasar a la siguiente posicion
        bt(pos+1, cnt) 

        # Opción 2: Intentar poner un punto aquí
        if cnt < 3: 
            cur.append('.')
            bt(pos+1, cnt+1)
            cur.pop(-1) # pop(-1) elimina el ultimo elemento

        cur.pop(-1) # Revertir la inserción de la letra actual
    bt(0, 0)
    return ans	


# Probar la solución
from random import randint
def probar_solucion():
    # Dato curioso: para n = 100, existen aprox. 156mil combinaciones :)
    n = randint(4, 10)
    s = ''.join([str(randint(0, 9)) for i in range(n)])

    ans = fuerza_bruta(s)
    print("CADENA ORIGINAL:", s)
    print("FUERZA BRUTA:", len(ans))
    for x in ans:
            print(x)
    ans = backtracking(s)
    print("\nBACKTRACKING:", len(ans))
    for x in ans:
            print(x)
    print("")

if __name__ == '__main__':
    probar_solucion()
