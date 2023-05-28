def isspacef(string):  # Define a função isspacef
    """
        Função que verifica se todos os caracteres de um string são espaços.
        string: string qualquer.
        Retorna True se forem todos espaços e False se pelo menos um não for.
    """
    if len(string) == 0:  # Se não tem nada
        return False  # Não há somente espaços

    for i in range(len(string)):  # Percorre toda a string
        code = ord(string[i])  # Obtem o código do caracter
        
        if not (code == 32):  # Verifica se não é um espaço
            return False  # Não há somente espaços
    return True  # Só tem espaços
       

if isspacef(""):
    print("Blank Space")
else:
    print("Tem outras coisas ai...")