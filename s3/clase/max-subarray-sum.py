
# a = [-5, -5, -5, -5, -5]
# subarreglo vacio [] con suma 0
# nosotros no vamos a considerar el subarreglo vacío



inf = 10**18

def merge(a, l, mid, r): # mezclar respuestas
    # calcular b1 (bloque de la izquierda que termina en el medio)
    b1 = -inf # inicializar en -infinito para no considerar subarreglos vacíos
    suma = 0
    for i in range(mid, l-1, -1):
        suma += a[i]
        b1 = max(b1, suma)
    
    b2 = -inf 
    suma = 0
    for i in range(mid+1, r+1):
        suma += a[i]
        b2 = max(b2, suma)

    return b1 + b2


def conquer(a, l, r): # resolver recursivamente y mezclar respuestas
    # l: left
    # r: right
    if l == r: return a[l]
    mid = (l+r) // 2
    max_L = conquer(a, l, mid)
    max_R = conquer(a, mid+1, r)
    return max(max_L, max_R, merge(a, l, mid, r))


a = [-2,1,-3,4,-1,2,1,-5,4] # la respuesta es 6, [4, -1, 2, 1]
n = len(a)

print(conquer(a, 0, len(a)-1))

