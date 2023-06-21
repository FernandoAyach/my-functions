def create_default_matrix(m, n):  # Define a função create_default_matrix
    """
        Função que recebe as linhas e colunas de uma matriz
        e retorna uma matriz m x n formada por 0's.
        m: inteiro referente ao número de linhas.
        n: inteiro referente ao número de colunas.
        Retorna uma matriz m x n formada por 0's.
    """
    matrix = []  # Cria uma lista vazia
    for i in range(m):  # Percorre as linhas
        line = [0] * n  # Cria uma linha de n zeros
        matrix.append(line)  # Insere a linha na matriz

    return matrix  # Retorna a matriz
