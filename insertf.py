def insertf(seq, position, value):  # Define a função insertf
    """
        Função que insere um valor em seq, na posição determinada.
        seq: sequência qualquer (lista, tupla, string).
        position: inteiro referente a posição a ser inserido o valor.
        value: valor em questão.
        Retorna uma lista com o valor inserido na posição.
    """
    inserted_seq = [None] * (len(seq) + 1)  # Define uma lista de tamanho len(seq) + 1

    j = 0  # Indice da lista nova
    for i in range(position):  # Percorre até a posição
       inserted_seq[j] = seq[i]  # Copia os valores de seq em inserted_seq
       j += 1  # Incrementa o iterador da lista nova

    inserted_seq[position] = value  # Adiciona o valor na posição

    for i in range(position, len(seq)):  # Percorre do indice da posição até o final de seq
       j += 1  # Incrementa o iterador da lista nova
       inserted_seq[j] = seq[i]  # Copia o restante

    if str(type(seq)) == "<class 'str'>":  # Se for uma string
       return "".join(inserted_seq)  # Junta a lista em uma string e retorna
    
    if str(type(seq)) == "<class 'tuple'>":  # Se for uma tupla
       return tuple(inserted_seq)  # Converte a lista em tupla e retorna

    return inserted_seq  # Retorna a lista nova

lista1 = [1, 2, 3, 4, 5]
print(insertf(lista1, 0, 0))

tupla1 = (1, 2, 3, 4, 5)
print(insertf(tupla1, 4, 7))

string1 = "Fernando"
print(insertf(string1, 8, " Ayach"))