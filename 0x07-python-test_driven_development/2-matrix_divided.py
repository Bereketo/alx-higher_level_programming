#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ divides each element of the matrix by a number
        matrix is a list of list of integers or floats
        div is a float or an integer
       return:
          a new_matrix on which every element of it is divided by div
          and rounded to 2 decimal places.
    """
    new_matrix = []
    if not isinstance(matrix, list): # or not isinstance(row, list) for row in matrix:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    for row in matrix:
        for column in row:
            if not isinstance(column, int) or not isinstance(column, float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) or not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        for column in [row]:
            new_matrix.append(round(column/div, 2))
    return new_matrix
