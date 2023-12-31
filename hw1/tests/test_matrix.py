import pytest
from ..src.matrix import Matrix2D, Matrix2D
from .fixtures import *
import copy

def test_create_bad_shape():
    with pytest.raises(ValueError) as value:
        Matrix2D([[1, 2, 3], [1, 2], [1, 2, 3, 4]])
        assert value == "Error in matrix shape"
    with pytest.raises(ValueError) as value:
        Matrix2D([1, [1, 2]])
        assert value == "Error in matrix shape"
    with pytest.raises(ValueError) as value:
        Matrix2D([])
        assert value == "Error in matrix shape"
    with pytest.raises(ValueError) as value:
        Matrix2D([[1], []])
        assert value == "Error in matrix shape"


def test_create(
    matrix1_3x3, matrix2_3x3, matrix_1x3, matrix_2x2, matrix_3x1, matrix_3x2
):
    matrix = Matrix2D(matrix1_3x3)
    assert matrix._shape == (3, 3)
    assert matrix._matrix == matrix1_3x3
    matrix = Matrix2D(matrix2_3x3)
    assert matrix._shape == (3, 3)
    assert matrix._matrix == matrix2_3x3
    matrix = Matrix2D(matrix_1x3)
    assert matrix._shape == (1, 3)
    assert matrix._matrix == matrix_1x3
    matrix = Matrix2D(matrix_2x2)
    assert matrix._shape == (2, 2)
    assert matrix._matrix == matrix_2x2
    matrix = Matrix2D(matrix_3x2)
    assert matrix._shape == (3, 2)
    assert matrix._matrix == matrix_3x2
    matrix = Matrix2D(matrix_3x1)
    assert matrix._shape == (3, 1)
    assert matrix._matrix == matrix_3x1
    matrix = Matrix2D([1, 2, 3])
    assert matrix._shape == (3, 1)
    assert matrix._matrix == matrix_3x1


def test_triangular_form_raise(matrix_1x3, matrix_3x1, matrix_3x2):
    with pytest.raises(ValueError) as value:
        matrix = Matrix2D(matrix_1x3)
        matrix.triangular_form()
        assert value == "It's not a square matrix"
    with pytest.raises(ValueError) as value:
        matrix = Matrix2D(matrix_3x1)
        matrix.triangular_form()
        assert value == "It's not a square matrix"
    with pytest.raises(ValueError) as value:
        matrix = Matrix2D(matrix_3x2)
        matrix.triangular_form()
        assert value == "It's not a square matrix"


def test_triangular_form(matrix1_3x3, matrix2_3x3, matrix_2x2, matrix_3x3_zero):
    matrix = Matrix2D(matrix1_3x3)
    triangular = matrix.triangular_form()
    assert len(triangular[1]) == 0
    assert triangular[0]._shape == (3, 3)
    answer = [[2, 5, 7], [0, -12, -17], [0, 0, 0.0417]]
    for row1, row2 in zip(answer, triangular[0]._matrix):
        for elem1, elem2 in zip(row1, row2):
            assert round(elem1, 4) == round(elem2, 4)

    matrix = Matrix2D(matrix2_3x3)
    triangular = matrix.triangular_form()
    assert len(triangular[1]) == 0
    assert triangular[0]._shape == (3, 3)
    answer = [[2, 3, -1], [0, -3.5, 1.5], [0, 0, 1.8571]]
    for row1, row2 in zip(answer, triangular[0]._matrix):
        for elem1, elem2 in zip(row1, row2):
            assert round(elem1, 4) == round(elem2, 4)

    matrix = Matrix2D(matrix_2x2)
    triangular = matrix.triangular_form()
    assert len(triangular[1]) == 0
    assert triangular[0]._shape == (2, 2)
    answer = [[2, -1], [0, -1.5]]
    for row1, row2 in zip(answer, triangular[0]._matrix):
        for elem1, elem2 in zip(row1, row2):
            assert round(elem1, 4) == round(elem2, 4)

    matrix = Matrix2D(matrix_3x3_zero)
    triangular = matrix.triangular_form()
    assert len(triangular[1]) == 1
    assert triangular[0]._shape == (3, 3)
    answer = [[1, -2, 1], [0, 3, -1], [0, 0, 1.6667]]
    for row1, row2 in zip(answer, triangular[0]._matrix):
        for elem1, elem2 in zip(row1, row2):
            assert round(elem1, 4) == round(elem2, 4)


def test_determinant_raise(matrix_1x3, matrix_3x1, matrix_3x2):
    with pytest.raises(ValueError) as value:
        matrix = Matrix2D(matrix_1x3)
        matrix.determinant()
        assert value == "It's not a square matrix"
    with pytest.raises(ValueError) as value:
        matrix = Matrix2D(matrix_3x1)
        matrix.determinant()
        assert value == "It's not a square matrix"
    with pytest.raises(ValueError) as value:
        matrix = Matrix2D(matrix_3x2)
        matrix.determinant()
        assert value == "It's not a square matrix"


def test_determinant(matrix1_3x3, matrix2_3x3, matrix_2x2, matrix_3x3_zero):
    matrix = Matrix2D(matrix1_3x3)
    determinant = matrix.determinant()
    assert round(determinant, 4) == -1

    matrix = Matrix2D(matrix2_3x3)
    determinant = matrix.determinant()
    assert round(determinant, 4) == -13

    matrix = Matrix2D(matrix_2x2)
    determinant = matrix.determinant()
    assert round(determinant, 4) == -3

    matrix = Matrix2D(matrix_3x3_zero)
    determinant = matrix.determinant()
    assert round(determinant, 4) == -5


def test_rank(
    matrix1_3x3,
    matrix2_3x3,
    matrix_1x3,
    matrix_2x2,
    matrix_3x1,
    matrix_3x2,
    matrix_3x3_zero,
    matrix_3x4,
    matrix_4x4,
    matrix_5x3,
):
    matrix = Matrix2D(matrix1_3x3)
    assert matrix.rank() == 3

    matrix = Matrix2D(matrix2_3x3)
    assert matrix.rank() == 3

    matrix = Matrix2D(matrix_1x3)
    assert matrix.rank() ==  1

    matrix = Matrix2D(matrix_2x2)
    assert matrix.rank() == 2

    matrix = Matrix2D(matrix_3x1)
    assert matrix.rank() == 1

    matrix = Matrix2D(matrix_3x2)
    assert matrix.rank() == 2

    matrix = Matrix2D(matrix_3x3_zero)
    assert matrix.rank() == 3

    matrix = Matrix2D(matrix_3x4)
    assert matrix.rank() == 2

    matrix = Matrix2D(matrix_4x4)
    assert matrix.rank() == 2

    matrix = Matrix2D(matrix_5x3)
    assert matrix.rank() == 3

def test_rank(
    matrix1_3x3,
    matrix2_3x3,
    matrix_1x3,
    matrix_2x2,
    matrix_3x1,
    matrix_3x2,
    matrix_3x3_zero,
    matrix_3x4,
    matrix_4x4,
    matrix_5x3,
    vec_mat1,
    vec_mat2,
    vec_mat_3x3_zero,
    vec_mat_2x2,
    vec_mat_1x3,
    vec_mat_3x1,
    vec_mat_3x2,
    vec_mat_3x4,
    vec_mat_4x4,
    vec_mat_5x3
):
    matrix = Matrix2D(matrix1_3x3)
    vec = Matrix2D(vec_mat1)
    assert matrix.has_solution(vec_mat1) == True

    matrix = Matrix2D(matrix2_3x3)
    vec = Matrix2D(vec_mat2)
    assert matrix.has_solution(vec_mat2) == True
    
    matrix = Matrix2D(matrix_1x3)
    vec = Matrix2D(vec_mat_1x3)
    assert matrix.has_solution(vec_mat_1x3) == True

    matrix = Matrix2D(matrix_2x2)
    vec = Matrix2D(vec_mat_2x2)
    assert matrix.has_solution(vec_mat_2x2) == True

    matrix = Matrix2D(matrix_3x1)
    vec = Matrix2D(vec_mat_3x1)
    assert matrix.has_solution(vec_mat_3x1) == False

    matrix = Matrix2D(matrix_3x2)
    vec = Matrix2D(vec_mat_3x2)
    assert matrix.has_solution(vec_mat_3x2) == False

    matrix = Matrix2D(matrix_3x3_zero)
    vec = Matrix2D(vec_mat_3x3_zero)
    assert matrix.has_solution(vec_mat_3x3_zero) == True

    matrix = Matrix2D(matrix_3x4)
    vec = Matrix2D(vec_mat_3x4)
    assert matrix.has_solution(vec_mat_3x4) == True
    matrix = Matrix2D(matrix_4x4)
    vec = Matrix2D(vec_mat_4x4)
    assert matrix.has_solution(vec_mat_4x4) == True

    matrix = Matrix2D(matrix_5x3)
    vec = Matrix2D(vec_mat_5x3)
    assert matrix.has_solution(vec_mat_5x3) == False


def test_inverse(matrix1_3x3, matrix2_3x3, matrix_2x2, matrix_3x3_zero):
    matrix = Matrix2D(matrix1_3x3)
    inverse_matrix = matrix.inverse_matrix()
    identity_matrix = copy.deepcopy(matrix)
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            identity_matrix[i][j] = 0
            for k in range(matrix._shape[0]):
                identity_matrix[i][j] += matrix[i][k]*inverse_matrix[k][j]
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            if i == j:
                assert round(identity_matrix[i][j]) == 1
            else:
                 assert round(identity_matrix[i][j]) == 0

    matrix = Matrix2D(matrix2_3x3)
    inverse_matrix = matrix.inverse_matrix()
    identity_matrix = copy.deepcopy(matrix)
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            identity_matrix[i][j] = 0
            for k in range(matrix._shape[0]):
                identity_matrix[i][j] += matrix[i][k]*inverse_matrix[k][j]
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            if i == j:
                assert round(identity_matrix[i][j]) == 1
            else:
                 assert round(identity_matrix[i][j]) == 0

    matrix = Matrix2D(matrix_2x2)
    inverse_matrix = matrix.inverse_matrix()
    identity_matrix = copy.deepcopy(matrix)
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            identity_matrix[i][j] = 0
            for k in range(matrix._shape[0]):
                identity_matrix[i][j] += matrix[i][k]*inverse_matrix[k][j]
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            if i == j:
                assert round(identity_matrix[i][j]) == 1
            else:
                 assert round(identity_matrix[i][j]) == 0

    matrix = Matrix2D(matrix_3x3_zero)
    inverse_matrix = matrix.inverse_matrix()
    identity_matrix = copy.deepcopy(matrix)
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            identity_matrix[i][j] = 0
            for k in range(matrix._shape[0]):
                identity_matrix[i][j] += matrix[i][k]*inverse_matrix[k][j]
    for i in range(matrix._shape[0]):
        for j in range(matrix._shape[1]):
            if i == j:
                assert round(identity_matrix[i][j]) == 1
            else:
                 assert round(identity_matrix[i][j]) == 0

def test_solve(matrix1_3x3, matrix2_3x3, matrix_2x2, matrix_3x3_zero):
    matrix = Matrix2D(matrix1_3x3)
    answer = matrix.solve_equations([[6], [3], [3]])
    assert [round(elem[0], 4) for elem in answer._matrix] == [6, -207, 147]

    matrix = Matrix2D(matrix2_3x3)
    answer = matrix.solve_equations([[6], [3], [3]])
    assert [round(elem[0], 4) for elem in answer._matrix] == [3, 0, 0]

    matrix = Matrix2D(matrix_2x2)
    answer = matrix.solve_equations([[-1], [1]])
    assert [round(elem[0], 4) for elem in answer._matrix] == [-1, -1]

    matrix = Matrix2D(matrix_3x3_zero)
    answer = matrix.solve_equations([[1], [2], [1]])
    assert [round(elem[0], 4) for elem in answer._matrix] == [3, 0, -1]