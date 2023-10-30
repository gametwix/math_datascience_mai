import pytest


@pytest.fixture
def matrix1_3x3():
    return [[2, 5, 7], [6, 3, 4], [5, -2, -3]]


@pytest.fixture
def matrix2_3x3():
    return [[2, 3, -1], [1, -2, 1], [1, 0, 2]]


@pytest.fixture
def matrix_3x3_zero():
    return [[0, 3, -1], [1, -2, 1], [1, 0, 2]]


@pytest.fixture
def matrix_2x2():
    return [[2, -1], [1, -2]]


@pytest.fixture
def matrix_1x3():
    return [[1, 2, 3]]


@pytest.fixture
def matrix_3x1():
    return [[1], [2], [3]]


@pytest.fixture
def matrix_3x2():
    return [[2, -1], [1, -2], [1, 2]]


@pytest.fixture
def matrix_3x4():
    return [[1, 0, 2, 3], [0, 0, 0, 0], [4, 5, 6, 7]]


@pytest.fixture
def matrix_4x4():
    return [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


@pytest.fixture
def matrix_5x3():
    return [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 0, 0]]


@pytest.fixture
def vec_mat1():
    return [[1], [2], [3]]

@pytest.fixture
def vec_mat2():
    return [[3], [-1], [4]]

@pytest.fixture
def vec_mat_3x3_zero():
    return [[2], [0], [1]]

@pytest.fixture
def vec_mat_2x2():
    return [[2], [1]]

@pytest.fixture
def vec_mat_1x3():
    return [[4]]

@pytest.fixture
def vec_mat_3x1():
    return [[1], [-2],[3]]

@pytest.fixture
def vec_mat_3x2():
    return [[1], [2], [-1]]

@pytest.fixture
def vec_mat_3x4():
    return [[0], [0], [0]]

@pytest.fixture
def vec_mat_4x4():
    return [[2], [3], [4], [5]]

@pytest.fixture
def vec_mat_5x3():
    return [[0], [1], [0], [1], [0]]