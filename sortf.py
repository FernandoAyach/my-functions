def sortf(seq, crescent = True):  # Define a função sortf
    """
        Função que retorna uma sequência ordenada, crescente ou decrescente.
        seq: sequência qualquer (lista, tupla, string).
        crescent: booleano que indica se é ordenada (True) ou descrescente (False).
        Retorna a sequência ordenada.
    """
    sorted_seq = list(seq)  # Define uma lista para ser ordenada, com base em seq

    for i in range(len(sorted_seq) - 1):  # Percorre de [i, len(sorted_seq) - 2]
        smaller = i  # Define i como posição menor
        for j in range(i + 1, len(sorted_seq)):  # Percorre de i + 1 em diante
            # Se o valor da posição for menor que o valor atual do menor
            if sorted_seq[j] < sorted_seq[smaller]:  
                smaller = j  # Armazena a posição do número
        aux = sorted_seq[i]  # Armazena o valor em i
        sorted_seq[i] = sorted_seq[smaller]  # Insere o valor do menor em i
        sorted_seq[smaller] = aux  # Insere o valor de onde era smaller

    if not crescent:  # Se a sequência deve ser decrescente
        reversed_seq = [None] * len(sorted_seq)  # Define uma lista de mesmo tamanho
        j = 0  # Inicia iterador da lista nova
        for i in range(len(sorted_seq) - 1, -1, -1):  # Percorre a lista ao contrário
            # Insere o valor da ultima posição de sorted_seq no começo da reversed
            reversed_seq[j] = sorted_seq[i]  
            j += 1  # Incrementa o iterado da lista nova

        sorted_seq = reversed_seq  # Insere reversed_seq em sorted

    if str(type(seq)) == "<class 'str'>":  # Se for uma string
       return "".join(sorted_seq)  # Junta a lista em uma string e retorna
    
    if str(type(seq)) == "<class 'tuple'>":  # Se for uma tupla
       return tuple(sorted_seq)  # Converte a lista em tupla e retorna

    return sorted_seq  # Retorna a lista nova  

lista1 = [5, 4, 3, 2, 1]
print(sortf(lista1))

tupla1 = (1, 2, 3, 4, 5)
print(sortf(tupla1, False))

string1 = "abcdefghijklmnopqrstuvwxyz"
print(sortf(string1, False))