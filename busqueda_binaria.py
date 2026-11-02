def buscar_binario(datos, valor):
    inicio = 0
    fin = len(datos) - 1

    while inicio <= fin:

        centro = inicio + (fin - inicio) // 2
        elemento = datos[centro]

        if elemento == valor:
            return centro

        if valor < elemento:
            fin = centro - 1
        else:
            inicio = centro + 1

    return -1

lista = [1, 3, 4, 6, 12, 15, 35, 44]
numero_buscado = 12

indice = buscar_binario(lista, numero_buscado)

print("BÚSQUEDA BINARIA")
print("Lista:", lista)
print("Número buscado:", numero_buscado)

if indice >= 0:
    print("Elemento encontrado en la posición:", indice + 1)
    print("Índice del elemento:", indice)
else:
    print("El elemento no existe en la lista.")