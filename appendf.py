def appendf(seq, value):  # Define a função appendf
    """
        Função que adiciona um valor ao final de uma lista.
        seq: lista qualquer.
        value: valor a ser adicionado.
        Retorna a lista com o valor adicionado no final.
    """
    
    appended_seq = [None] * (len(seq) + 1)  # Define uma lista do tamanho de seq + 1

    for i in range(len(seq)):  # Loop que percorre o intervalo [0, len(seq))
       appended_seq[i] = seq[i]  # Atribui o elemento de seq[i] em appended_seq[i]

    appended_seq[len(seq)] = value  # Adiciona o valor na última posição

    return appended_seq  # Retorna a lista nova

lista = [1, 2, 3, 4, 5]
print(lista)

appended = appendf(lista, 6)
print(appended)

appended = appendf(appended, 7)
print(appended)