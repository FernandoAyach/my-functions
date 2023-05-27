def minf(seq):  # Define a função minf
    """
        Função que retorna o menor elemento de uma sequência.
        seq: sequência qualquer (string, tupla ou lista).
        Retorna o menor elemento.
    """

    smaller = seq[0]  # Define um menor de referência

    for i in range(1, len(seq)):  # Loop que percorre o intervalo [1, len(seq))
        if seq[i] < smaller:  # Se o elemento atual for menor que o menor
            smaller = seq[i]  # Este será o menor
    
    return smaller  # Retorna o menor

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
string = "Agora deu caralho memo"

print(minf(lista))
print(minf(tupla))
print(minf(string))