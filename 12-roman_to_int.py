def roman_to_int(roman_string):

    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    temp = 0
    
    for char in reversed(roman_string):
        valor = numerals.get(char, 0)
        if valor >= temp:
            resultado += valor
        else:
            resultado -= valor
        temp = valor
    
    return resultado