# -*- coding: utf-8 -*-

def lowerf(string):  # Define a função lowerf
    
    """
        Função que retorna uma string somente com caracteres minúsculos.
        seq: string qualquer.
        Retorna uma string somente com caracteres minúsculos.
    """

    lower_string = ""  # Define uma string para armazenar os caracters minúsculos
    for i in range(len(string)):  # Percorre a string
        code = ord(string[i])  # Obtem o código do caracter
       
        # Verifica se está, respectivamente, em A-Z ou ÀÁÂÃ ou ÉÊ ou ÍÎ ou ÓÔÕ ou ÚÛ
        if code >= 65 and code <= 90 or \
            code >= 192  and code <= 195 or \
            code >= 199 and code <= 202 or \
            code >= 205 and code <= 206 or \
            code >= 211 and code <= 213 or \
            code >= 218 and code <= 219:
            code += 32  # Transforma em minúsculo
        lower_string += chr(code)  # Concatena o caracter minúsculo em lower_string
        
    return lower_string  # Retorna lower_string

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇÀÁÂÃÉÊÍÎÓÔÕÚÛ"
print(string)
print(lowerf(string))