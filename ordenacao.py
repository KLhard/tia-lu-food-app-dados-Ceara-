def insertion_sort(lista, chave):
    """
    Ordena uma lista de dicionários usando o algoritmo Insertion Sort,
    ordenando de acordo com a chave especificada.
    """
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        # Move elementos maiores que 'atual' para a direita
        while j >= 0 and lista[j][chave] > atual[chave]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = atual

    return lista
