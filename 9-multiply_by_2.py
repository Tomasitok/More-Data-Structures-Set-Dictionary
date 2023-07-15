def multiply_by_2(a_dictionary):

    multiply_dict = {}

    for key, value in a_dictionary.items():
        multiply_dict[key] = value * 2
    return multiply_dict