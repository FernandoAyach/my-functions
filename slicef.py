def slicef(seq, start, end, step = 1):  # Define a função concatenatef
    """
        Função que realiza o fatiamento de uma sequência.
        seq: sequência qualquer (lista, tupla, string).
        start: indice inteiro de começo do fatiamento.
        end: indice inteiro final do fatiamento.
        step: passo inteiro do fatiamento
        Retorna uma sequência somente com os valores dos indices [start, end), com passo step.
    """
    sliced_seq = []  # Define uma lista vazia
    
    for i in range(start, end, step):  # Percorre o intervalo [start, end), com passo step
      sliced_seq += [seq[i]]  # Adiciona os valores do intervalo em sliced_seq

    if str(type(seq)) == "<class 'str'>":  # Se for uma string
       return "".join(sliced_seq)  # Junta a lista em uma string e retorna
    
    if str(type(seq)) == "<class 'tuple'>":  # Se for uma tupla
       return tuple(sliced_seq)  # Converte a lista em tupla e retorna

    return sliced_seq  # Retorna a lista nova

lista1 = [1, 2, 3, 4, 5]

print(lista1[:3:])
print(slicef(lista1, 0, 3))

tupla1 = (1, 2, 3, 4, 5)
print(tupla1[0:4:2])
print(slicef(tupla1, 0, 4, 2))

string1 = "Fernando"
print(string1[7:3:-2])
print(slicef(string1, 7, 3, -2))