def maxf(seq):  # Define a função maxf
    """
        Função que retorna o maior elemento de uma sequência.
        seq: sequência qualquer (string, tupla ou lista).
        Retorna o maior elemento.
    """

    bigger = seq[0]  # Define um maior de referência

    for i in range(1, len(seq)):  # Loop que percorre o intervalo [1, len(seq))
        if seq[i] > bigger:  # Se o elemento atual for maior que o maior
            bigger = seq[i]  # Este será o maior
    
    return bigger  # Retorna o maior

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
string = "Agora deu caralho memo"

print(maxf(lista))
print(maxf(tupla))
print(maxf(string))