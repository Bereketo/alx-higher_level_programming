#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    inlen = len(matrix[0])
    leng = len(matrix)
    for i in range(leng):
        for j in range(inlen):
            print("{:d}".format(matrix[i][j]), end=" ")
        print()
