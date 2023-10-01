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
