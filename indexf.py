def indexf(seq, value):  # Define a função indexf
    """
        Função que retorna o indice na lista do valor determinado.
        seq: sequência qualquer (lista, tupla, string).
        value: valor qualquer.
        Retorna o índice do primeiro valor correspondente ao valor determinado.
    """

    for i in range(len(seq)):  # Percorre todas as posições de seq
       if seq[i] == value:  # Se o valor atual for igual ao valor determinado
           return i   # Retorna a posição do valor

lista1 = [1, 2, 3, 4, 5, 1]
print(indexf(lista1, 1))

tupla1 = (1, 2, 3, 4, 5)
print(indexf(tupla1, 4))

lista1 = [1, 2, 3, 4, 5]
print(indexf(lista1, 6))

string = "dasdasdasda"
print(indexf(string, "s"))