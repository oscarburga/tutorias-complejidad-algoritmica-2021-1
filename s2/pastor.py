# Estados: (Lado, cabra, lobo, lechuga) (todos booleanos)
# El backtracking podría ser cíclico y no terminar nunca, por lo que necesitamos mantener
# algo que nos diga si ya hemos visitado un estado antes.
# Lo óptimo sería usar mascaras de bits para representar los estados pero eso 
# escapa de los temas del curso. Para esta ocasión, usaremos un 
# 'arreglo de sets de tuplas' para hacer dicha verificación de manera sencilla.

# Los objetos representan lo siguiente segun su valor:
# False -> el objeto está a la izquierda del río
# True -> el objeto está a la derecha del río

def backtracking():
    # vis[lado] contiene todas las configuraciones de objetos visitadas actualmente
    # que ocurrieron cuando el pastor estaba del lado 'lado'
    vis = [ set([]), set([]) ] ## Arreglo de sets
    path = []

    # Funcion que me dice si puedo ir a un estado
    def can(lado, obj): 
        invalid = False # invalid será True si el estado es invalido
        invalid = invalid or (obj[0] == obj[1] and lado != obj[0]) # Se queda solo cabra y lobo
        invalid = invalid or (obj[0] == obj[2] and lado != obj[0]) # Se queda solo cabra y lechuga
        invalid = invalid or (tuple(obj) in vis[lado]) # Ya estuve en ese estado
        return not invalid # Lo invierto para que retorne True si el estado es valido
                    

    def bt(lado = False, obj = [False, False, False]):

        vis[lado].add(tuple(obj)) # Marcar como visitado

        ### Si todos están a la derecha, agregar al camino y retornar verdadero
        if lado and (False not in obj): 
            path.append([lado, tuple(obj)])
            return True 

        ### Opción 1: Cruzar sin llevar ningún objeto
        if can(not lado, obj):
            if bt(not lado, obj): ### Si encontré camino, añado el estado a la respuesta
                path.append([lado, tuple(obj)])
                return True

        ### Opción 2: Cruzar llevando algún objeto
        for i in range(3):
            if obj[i] == lado: # Si el objeto esta del lado del pastor, intento llevarmelo
                obj[i] = not obj[i]
                if can(not lado, obj): 
                    # Si encontré camino, añado el estado a la respuesta
                    if bt(not lado, obj):  
                        obj[i] = not obj[i] # Primero revierto el movimiento!
                        path.append([lado, tuple(obj)])
                        return True
                obj[i] = not obj[i] # Revertir el movimiento

        vis[lado].remove(tuple(obj)) # Marco como no visitado
        return False ### No encontré camino, retorno False
    return bt(), path

ans, path = backtracking()
print(ans)
path.reverse()

for x in path: ### Imprimo la ruta
	print(x)
