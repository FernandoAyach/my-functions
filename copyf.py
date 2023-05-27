def copyf(seq):  # Define a função copyf
    """
        Função que retorna a cópia de uma sequência.
        seq: lista qualquer.
        Retorna a cópia da sequência.
    """

    copy = [None] * len(seq)  # Define uma lista de mesmo tamanho de seq

    for i in range(len(seq)):  # Loop que percorre o intervalo [0, len(seq))
       copy[i] = seq[i]  # Atribui o elemento de seq[i] em copy[i]
    
    return copy  # Retorna a cópia

lista = [1, 2, 3, 4, 5]
print(lista)

copy = copyf(lista)
lista[0] = 0

print(lista)
print(copy)

    