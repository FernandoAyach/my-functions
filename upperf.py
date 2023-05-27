# -*- coding: utf-8 -*-

def upperf(string):  # Define a função upperf
    
    """
        Função que retorna uma string somente com caracteres maiusculos.
        seq: string qualquer.
        Retorna uma string somente com caracteres maiusculos.
    """

    upper_string = ""  # Define uma string para armazenar os caracters maiusculos
    for i in range(len(string)):  # Percorre a string
        code = ord(string[i])  # Obtem o código do caracter
       
        # Verifica se está, respectivamente, em a-z ou à,á,ã ou éê ou íî ou óôõ ou úû
        if code >= 97 and code <= 122 or \
            code >= 224  and code <= 227 or \
            code >= 231 and code <= 234 or \
            code >= 237 and code <= 238 or \
            code >= 243 and code <= 245 or \
            code >= 250 and code <= 251:
            code -= 32  # Transforma em maiusculo
        upper_string += chr(code)  # Concatena o caracter maiusculo em upper_string
        
    return upper_string  # Retorna upper_string

string = "abcdefghijklmnopqrstuvwxyzçàáâãéêíîóôõúû"
print(string)
print(upperf(string))
