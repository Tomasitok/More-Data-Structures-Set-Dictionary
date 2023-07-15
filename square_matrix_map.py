def square_matrix_map(matrix=[]):

    new_list = list(map(lambda fila: list(map(lambda x: x ** 2, fila)), matrix))

    return new_list