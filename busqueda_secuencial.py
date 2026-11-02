def buscar_secuencial(datos, valor):
    posicion = 0

    while posicion < len(datos):
        
        if datos[posicion] == valor:
            return posicion
        posicion += 1

    return -1

lista = [1, 3, 4, 6, 12, 15, 35, 44]
numero_buscado = 12

indice = buscar_secuencial(lista, numero_buscado)

print("BÚSQUEDA SECUENCIAL")
print("Lista:", lista)
print("Número buscado:", numero_buscado)

if indice >= 0:
    print("Elemento encontrado en la posición:", indice + 1)
    print("Índice del elemento:", indice)
else:
    print("El elemento no existe en la lista.")