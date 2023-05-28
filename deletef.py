def deletef(seq, start, end):  # Define a função deletef
    """
        Função que retorna uma sequência sem os valores dos indices [start, end].
        seq: sequência qualquer (lista, tupla, string).
        start: inteiro referente a posição de início da remoção.
        end: inteiro referente a posição final da remoção (inclusive).
        Retorna uma sequência sem os valores dos indices [start, end].
    """
    n = len(seq) - (end - start + 1)
    deleted_seq = [None] * (n)  # Define uma lista de tamanho n

    j = 0  # Indice da lista nova
    for i in range(start):  # Percorre até a posição start - 1
        deleted_seq[j] = seq[i]  # Copia seq em deleted_seq
        j += 1  # Incrementa o iterador da lista nova
    
    for i in range(end + 1, len(seq)):  # Percorre de end até len(seq) - 1
       deleted_seq[j] = seq[i]  # Copia seq em deleted_seq
       j += 1  # Incrementa o iterador da lista nova

    if str(type(seq)) == "<class 'str'>":  # Se for uma string
       return "".join(deleted_seq)  # Junta a lista em uma string e retorna
    
    if str(type(seq)) == "<class 'tuple'>":  # Se for uma tupla
       return tuple(deleted_seq)  # Converte a lista em tupla e retorna

    return deleted_seq  # Retorna a lista nova

lista1 = [1, 2, 3, 4, 5]
print(deletef(lista1, 0, 0))

tupla1 = (1, 2, 3, 4, 5)
print(deletef(tupla1, 2, 4))

string1 = "Fernando"
print(deletef(string1, 3, 5))