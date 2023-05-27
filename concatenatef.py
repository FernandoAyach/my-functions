def concatenatef(seq1, seq2):  # Define a função concatenatef
    """
        Função que concatena uma sequência de mesmo tipo com outra.
        seq1: sequência qualquer (lista, tupla, string).
        seq2: sequência qualquer (lista, tupla, string), de mesmo tipo de seq1.
        Retorna uma lista com a concantenação de seq1 e seq2, nessa ordem.
    """
    n = len(seq1) + len(seq2)  # Número total de elementos resultante
    concatenated_seq = [None] * n  # Define uma lista de tamanho n

    for i in range(len(seq1)):  # Loop que percorre a primeira sequência
       concatenated_seq[i] = seq1[i]  # Atribui o elemento de seq1[i] em concatenated_seq[i]
    
    for i in range(len(seq1), n):  # Loop que percorre a segunda sequência
       # Atribui o elemento de seq2[i - len(seq1)] em appended_seq[i]
       concatenated_seq[i] = seq2[i - len(seq1)]  

    if str(type(seq1)) == "<class 'str'>":  # Se for uma string
       return "".join(concatenated_seq)  # Junta a lista em uma string e retorna
    
    if str(type(seq1)) == "<class 'tuple'>":  # Se for uma tupla
       return tuple(concatenated_seq)  # Converte a lista em tupla e retorna

    return concatenated_seq  # Retorna a lista nova

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8]
print(concatenatef(lista1, lista2))

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (6, 7, 8)
print(concatenatef(tupla1, tupla2))

string1 = "Fernando "
string2 = "Ayach"
print(concatenatef(string1, string2))