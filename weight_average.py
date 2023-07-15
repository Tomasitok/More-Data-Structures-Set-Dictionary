def weight_average(my_list=[]):

    if not my_list:
        return 0

    peso_total = 0
    suma_ponderada = 0

    for item in my_list:
        valor, peso = item
        peso_total += peso
        suma_ponderada += valor * peso

    return suma_ponderada / peso_total