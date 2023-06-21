def show_matrix(matrix, m, n):  # Define a função show_matrix
    """
        Função que recebe uma matriz e suas dimensões
        e a mostra no formato visual de matriz na tela.
        matrix: matriz qualquer.
        m: inteiro referente ao número de linhas.
        n: inteiro referente ao número de colunas.
        Não há retorno.
    """

    for i in range(m):  # Percorre as linhas
        for j in range(n - 1):  # Percorre até a penúltima coluna
            print(matrix[i][j], end = " ")  # Imprime o elemento com espaço
        print(matrix[i][n - 1])  # Imprime o último elemento, pulando linha e sem espaço