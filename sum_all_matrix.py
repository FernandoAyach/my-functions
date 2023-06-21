def read_int_matrix(m, n):  # Define a função read_int_matrix
    """
        Função que recebe as linhas e colunas de uma matriz
        e retorna uma matriz m x n de inteiros.
        m: inteiro referente ao número de linhas.
        n: inteiro referente ao número de colunas.
        Retorna uma matriz de m x n de inteiros.
    """
    matrix = []  # Cria uma lista vazia
    for i in range(m):  # Percorre as linhas
        line = [0] * n  # Cria uma lista de inteiros
        # Le os valores da linha, separados por espaços
        line_in = input().split()  
        for j in range(n):  # Percorre as colunas
            line[j] = int(line_in[j])  # Atribui o valor inteiro em line
        matrix.append(line)  # Insere a linha na matriz
    
    return matrix  # Retorna a matriz

def sum_all_matrix(matrix, m, n):  # Define a função sum_all_matrix
    """
        Função que recebe uma matriz e suas dimensões
        e retorna uma lista com a soma de todas as linhas, colunas e diagonais.
        matrix: matriz de inteiros.
        m: inteiro referente ao número de linhas.
        n: inteiro referente ao número de colunas.
        Retorna uma lista com a soma de todas as linhas, colunas e diagonais.
    """

    line_s = [0] * n  # Soma das linhas
    col_s = [0] * n  # Soma das colunas
    md_s = 0  # Soma da diagonal principal
    sd_s = 0  # Soma da diagonal secundária

    for i in range(m):  # Percorre as linhas
        for j in range(n):  # Percorre as colunas
            line_s[i] += matrix[i][j]  # Soma o valor da linha
            col_s[j] += matrix[i][j]  # Soma o valor da coluna
        md_s += matrix[i][i]  # Soma o valor da diagonal principal
        sd_s += matrix[i][n - i - 1]  # Soma o valor da diagonal secundária
    
    return [line_s, col_s, md_s, sd_s]  # Retorna a lista de somas

matrix = read_int_matrix(3, 3)
print(sum_all_matrix(matrix, 3, 3))
