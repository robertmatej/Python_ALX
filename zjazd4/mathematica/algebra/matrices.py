#import numpy
#
# A = [[1,1,1],[2,2,2],[3,3,3]]
# B = [[1,1,1],[1,1,1],[2,2,2]]
# #C = [[0,0,0],[0,0,0],[0,0,0]]


def add_matrices(A, B):
    if len(A)!=len(B) or len(A[0])!= len(B[0]):
        raise ValueError("Różna ilość wymiarów")

    result = []
    for row_i in range(len(A)):
        new_row = []
        for col_i in range(len(A[row_i])):
            # C[row_i][col_i]= A[row_i][col_i]+B[row_i][col_i]    # moja weresja gdzie C wynikowe bylo zdefiniowane
            new_row.append(A[row_i][col_i] + B[row_i][col_i])

        result.append(new_row)
    print (result)
    return result

def sub_matrices(A, B):
    if len(A)!=len(B) or len(A[0])!= len(B[0]):
        raise ValueError("Różna ilość wymiarów")

    result = []
    for row_i in range(len(A)):
        new_row = []
        for col_i in range(len(A[row_i])):
            # C[row_i][col_i]= A[row_i][col_i]+B[row_i][col_i]    # moja weresja gdzie C wynikowe bylo zdefiniowane
            new_row.append(A[row_i][col_i] - B[row_i][col_i])

        result.append(new_row)
    print (result)
    return result


if __name__=='__main__':
    print (__name__)            #wywoujemy nazwę pliku
    A = [
        [1, 2, 3],
        [4, 5, 6],
        ]
    B = [
        [7, 8, 9],
        [10, 11, 12],
        ]

    add_matrices(A,B)

    sub_matrices(A,B)

