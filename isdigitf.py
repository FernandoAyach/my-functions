def isdigitf(string):  # Define a função isdigitf
    """
        Função que verifica se todos os caracteres de um string são dígitos.
        string: string qualquer.
        Retorna True se forem todos digitos e False se pelo menos um não for.
    """

    for i in range(len(string)):  # Percorre toda a string
        code = ord(string[i])  # Obtem o código do caracter
        
        if not (code >= 48 and code <= 57):  # Verifica se não é um dígito
            return False  # Não há somente digitos
    return True  # Só tem digitos
       

if isdigitf("12345"):
    print("Só dígitos")
else:
    print("Tem outras coisas ai...")