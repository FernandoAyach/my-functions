def isupperf(char):  # Define a função isupperf
    """
        Função que verifica se um caracter (lingua portuguesa) é maiúsculo.
        seq: caracter de uma string (lingua portuguesa).
        Retorna True se for maiúsculo e False caso contrário.
    """

    code = ord(char)  # Obtem o código do caracter
       
    # Verifica se está, respectivamente, em A-Z ou ÀÁÂÃ ou ÉÊ ou ÍÎ ou ÓÔÕ ou ÚÛ
    if code >= 65 and code <= 90 or \
        code >= 192  and code <= 195 or \
        code >= 199 and code <= 202 or \
        code >= 205 and code <= 206 or \
        code >= 211 and code <= 213 or \
        code >= 218 and code <= 219:
        return True  # É maiúsculo
    return False  # É minúsculo

if isupperf("%"):
    print("É maiúsculo")
else:
   print("É minúsculo")