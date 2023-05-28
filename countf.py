def countf(seq, value):  # Define a função countf
    """
        Função que conta a frequêcia de um valor na lista.
        seq: sequência qualquer (lista, tupla, string).
        value: valor qualquer.
        Retorna a frequêcia de um valor na lista.
    """
    total = 0  # Total de aparições
    for i in range(len(seq)):  # Percorre todas as posições de seq
       if seq[i] == value:  # Se o valor atual for igual ao valor determinado
           total += 1  # Soma 1 em total
    return total   # Retorna a frequência total

lista1 = [1, 2, 3, 4, 5, 1, 1]
print(countf(lista1, 1))

tupla1 = (1, 2, 3, 4, 5)
print(countf(tupla1, 4))

lista1 = [1, 2, 3, 4, 5]
print(countf(lista1, 6))

string = "dasdasdasda"
print(countf(string, "s"))