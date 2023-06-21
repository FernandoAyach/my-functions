def read_float_matrix(m, n):  # Define a função read_float_matrix
    """
        Função que recebe as linhas e colunas de uma matriz
        e retorna uma matriz m x n de números reais.
        m: inteiro referente ao número de linhas.
        n: inteiro referente ao número de colunas.
        Retorna uma matriz de m x n de números reais.
    """
    matrix = []  # Cria uma lista vazia
    for i in range(m):  # Percorre as linhas
        line = [0] * n  # Cria uma lista de inteiros
        # Le os valores da linha, separados por espaços
        line_in = input().split()  
        for j in range(n):  # Percorre as colunas
            line[j] = float(line_in[j])  # Atribui o valor real em line
        matrix.append(line)  # Insere a linha na matriz
    
    return matrix  # Retorna a matriz