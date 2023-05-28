def intercalatef(seq1, seq2):  # Define a função intercalatef
    """
        Função que intercala em uma nova sequência os valores intercalados de seq1 e seq2.
        seq1: sequência qualquer (lista, tupla, string).
        seq2: sequência qualquer (lista, tupla, string), de mesmo tipo de seq1.
        Retorna uma nova sequência com valores intercalados por seq1 e seq.
    """
    n = len(seq1) + len(seq2)  # Número total de elementos resultante
    intercalated_seq = [None] * n  # Define uma lista de tamanho n

    seq1_turn = True  # Vez da sequencia 1

    j = 0  # Iterador de seq1 e seq1
    for i in range(n):  # Percorre n
        
        # Se for a vez do seq1 e for possivel pegar um elemento
        if seq1_turn and j < len(seq1):  
            intercalated_seq[i] = seq1[j]  # Insere o elemento de seq1 em intercalated_seq

            if j < len(seq2):  # Se for possivel pegar um elemento de seq2
                seq1_turn = False  # É a vez do seq2
            else:  # Senão
                j += 1  # Incrementa no iterador
        else:  # Senão
            intercalated_seq[i] = seq2[j]  # Insere o elemento de seq2 em intercalated_seq
            seq1_turn = True  # É a vez do seq1
            j += 1  # Incrementa no iterador
       
    if str(type(seq1)) == "<class 'str'>":  # Se for uma string
       return "".join(intercalated_seq)  # Junta a lista em uma string e retorna
    
    if str(type(seq1)) == "<class 'tuple'>":  # Se for uma tupla
       return tuple(intercalated_seq)  # Converte a lista em tupla e retorna

    return intercalated_seq  # Retorna a lista nova

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
print(intercalatef(lista1, lista2))

tupla1 = (0, 1, 0, 1, 0)
tupla2 = (1, 0, 1)
print(intercalatef(tupla1, tupla2))

string1 = "Fernando"
string2 = "Ayach"
print(intercalatef(string1, string2))