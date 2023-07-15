def square_matrix_simple(matrix=[]):

    result = list(map(lambda fila: list(map(lambda x: x ** 2, fila)), matrix))
    
    return result