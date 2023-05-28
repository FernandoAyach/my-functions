def inf(seq, value):  # Define a função inf
    """
        Função que verifica se um valor está dentro de uma sequência.
        seq: sequência qualquer (lista, tupla, string).
        value: valor qualquer.
        Retorna True se estiver contido e False caso contrário.
    """
    len_seq = len(seq)  # Obtem o tamanho da sequência inteira
    
    if str(type(seq)) == "<class 'str'>":  # Se for uma string
        len_value = len(value)  # Obtem o tamanho do valor

        # Percorre de [0, len_string - len_value] para i + j não ultrapassar a string
        for i in range(len_seq - len_value + 1):  

            j = 0  # Iterador do valor
            # Loop que, ao achar um valor igual, percorre os valores subsquentes da string
            # até dar o número de letras exato
            while j < len_value:  # Percorre os indices do valor
                # Se o caracter da string não é igual ao do valor
                if seq[i + j] != value[j]:  
                    break  # Para o loop e passa pro proximo caracter da string
                j += 1  # Pega o próximo indice do valor 
                if j == len_value:  # Se bateu o número de letras
                    return True  # Encontrou
        return False  # Não encontrou
    
    for i in range(len_seq):  # Percorre toda a sequência
        if value == seq[i]:  # Se há um valor igual ao value
            return True  # Encontrou
    return False  # Não encontrou

lista = [1, 2, 3, 4]
tupla = (0, 1, -1)
string = "With or without you"

value = 1
if inf(lista, value):
    print(value, "está dentro de", lista)
else:
    print(value, "não está dentro de", lista)

value = 3
if inf(tupla, value):
    print(value, "está dentro de", tupla)
else:
    print(value, "não está dentro de", tupla)

value = "With"
if inf(string, value):
    print(value, "está dentro de", string)
else:
    print(value, "não está dentro de", string)


