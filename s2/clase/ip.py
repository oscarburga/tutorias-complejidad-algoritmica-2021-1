'''
Problema: 
    * Oscar está llevando su curso de Redes y Protocolo de Comunicaciones.
    * A Oscar le han gustado mucho las direcciones IPv4.
    * El formato de una dirección IPv4 es el siguiente: xxx.xxx.xxx.xxx

    Oscar tiene una cadena de N dígitos y quiere saber:
    ¿De cuantas formas puede Oscar separar su cadena en 4 partes no-vacías 
    para poder escribirla como si fuera una dirección IPv4? Imprímelas.
    
    En palabras simples: Genera todas las formas distintas de insertar 3 puntos en
    en una cadena, tal que no haya 2 puntos juntos, y junto a cada punto hayan digitos
    a sus dos costados.

    Diseñe un algoritmo de fuerza bruta cualquiera que solucione este problema.
    Diseñe un algoritmo con backtracking que solucione este problema.

'''


# 1234 [1] 5 [2] 6 [3] 7

# [ 1, 2, 3, 4, . , 5, . , 6, . , 7 ]

def fuerzabruta(s) -> list:
    n = len(s)
    if n < 4: return []
    ans = []
    # Asumimos que si ponemos un punto en la posición 'i'
    # en verdad lo estamos colocando entre las posiciones 'i' e 'i+1'
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                # s[L:R] retorna el segmento en S de la posición L hasta R-1 
                t = '.'.join( [ \
                    s[0 : i+1], \
                    s[i+1 : j+1], \
                    s[j+1 : k+1], \
                    s[k+1 : n] \
                    ] )
                # t = ""
                # t += s[0 : i+1] + '.'
                # t += s[i+1 : j+1] + '.'
                # t += s[j+1 : k+1] + '.'
                # t += s[k+1: n]
                ans.append(t)
    return ans


def backtracking(s) -> list: # esto es solo para meter todo y que este ordenado
    n = len(s)
    s = list(s)
    ans = []
    cur = []

    # otra opcion menos eficiente:
    # no usar la lista 'cur', sino llevar la cadena construida actual
    # como parámetro en el backtracking

    # def bt(i, cnt, cadena_actual):
    # bt(i+1, cnt, cadena_actual + s[i])
    # bt(i+1, cnt+1, cadena_actual + s[i] + '.' )

    def bt(i, cnt): # <- esta va a ser mi funcion recursiva de verdad

        cur.append(s[i]) # s[i] es el i-ésimo dígito de la cadena

        if i == n - 1: # estoy en el final de la cadena
            # si he puesto 3 puntos, agrego esta cadena a mi respuesta
            if cnt == 3: ans.append( ''.join(cur) )     
            # si no he puesto 3 puntos, no tengo que hacer nada
            # porque no tengo una cadena valida
            cur.pop(-1)
            return

        # que opciones tengo?
        # opcion 1: avanzar a la siguiente pos. sin poner punto
        bt(i+1, cnt)

        # opcion 2: poner punto y avanzar a la siguiente pos
        if cnt < 3: # O(N^3)
            #si no pongo este if, es O(2^(N-1))
            cur.append('.') # agrego un punto luego del i-ésimo dígito
            bt(i+1, cnt+1)
            cur.pop(-1)

        # ya termine ocn todo: debo quitar mi digito tambien
        cur.pop(-1)

    bt(0, 0)
    return ans


ans1 = backtracking("1234567")
ans2 = fuerzabruta("1234567")

print("BACKTRACKING: ")
for x in ans1:
    print(x)

print("FUERZA BRUTA: ")
for x in ans2:
    print(x)
