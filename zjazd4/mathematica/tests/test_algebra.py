from mathematica.algebra.matrices import add_matrices, sub_matrices
import pytest

def test_add_matrices():
    A = [
        [1,2,3],
        [4,5,6],
        ]
    B = [
        [7, 8, 9],
        [10, 11, 12],
        ]
    result = add_matrices(A,B)
    assert result == [[8, 10, 12],[14, 16, 18]]


def test_add_matrices_with_different_count_of_rows ():
    A = [
        [1, 2],
        [3, 4],
        [3, 4],
    ]

    B = [
        [7, 8],
        [10, 11],
        ]

    with pytest.raises(ValueError) :            # test sprawdza czy błąd zostanie rzuciony, zaimpoortowqaliśmy do tego pytest
        result = add_matrices(A,B)

def test_sub_matrices():
    A = [
        [1,2,3],
        [4,5,6],
        ]
    B = [
        [7, 8, 9],
        [10, 11, 12],
        ]
    result = add_matrices(A,B)
    assert result == [[-6, -6, -6],[-6, -6, -6]]


def test_sub_matrices_with_different_count_of_rows ():
    A = [
        [1, 2],
        [3, 4],
        [3, 4],
    ]

    B = [
        [7, 8],
        [10, 11],
        ]

    with pytest.raises(ValueError) :            # test sprawdza czy błąd zostanie rzuciony, zaimpoortowqaliśmy do tego pytest
        result = sub_matrices(A,B)



# poszukaj co nie działa