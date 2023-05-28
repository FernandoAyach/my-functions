def islowerf(char):  # Define a função islowerf
    """
        Função que verifica se um caracter (lingua portuguesa) é minúsculo.
        seq: caracter de uma string (lingua portuguesa).
        Retorna True se for minúsculo e False caso contrário.
    """

    code = ord(char)  # Obtem o código do caracter
       
    # Verifica se está, respectivamente, em a-z ou à,á,ã ou éê ou íî ou óôõ ou úû
    if code >= 97 and code <= 122 or \
        code >= 224  and code <= 227 or \
        code >= 231 and code <= 234 or \
        code >= 237 and code <= 238 or \
        code >= 243 and code <= 245 or \
        code >= 250 and code <= 251:
        return True  # É minúsculo
    return False  # É maiúsculo

if islowerf("A"):
    print("É minúsculo")
else:
    print("É maiúsculo")