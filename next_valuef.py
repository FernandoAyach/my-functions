def next_valuef(seq, index):  # Define a função next_valuef
    """
        Função que retorna o próximo valor da sequência.
        seq: sequência qualquer (lista, tupla, string).
        index: indice inteiro atual.
        Retorna o valor correspondente a index + 1.
    """
    next_index = (index + 1) % len(seq)  # Obtem o próximo indice

    return seq[next_index]  # Retorna o próximo valor da sequência

lista1 = [1, 2, 3, 4, 5]
print(next_valuef(lista1, 0))

tupla1 = (1, 2, 3, 4, 5)
print(next_valuef(tupla1, 4))

string1 = "Fernando"
print(next_valuef(string1, 3))