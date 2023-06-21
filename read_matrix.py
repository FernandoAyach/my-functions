def read_matrix(m):  # Define a função read_matrix
    """
        Função que recebe as linhas de uma matriz
        e retorna uma matriz de strings.
        m: inteiro referente ao número de linhas.
        Retorna uma matriz de strings.
    """
    matrix = []  # Cria uma lista vazia
    for i in range(m):  # Percorre as linhas
        matrix.append(input().split() )  # Insere a linha na matriz

    return matrix  # Retorna a matriz