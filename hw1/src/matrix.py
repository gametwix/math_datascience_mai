from typing import List
from pathlib import Path
import copy


class Matrix2D:
    def __init__(self, data: List):
        if len(data) == 0:
            raise ValueError("Error in matrix shape")
        self._shape = (len(data), 1 if type(data[0]) is not list else len(data[0]))
        for i in range(len(data)):
            if type(data[i]) is not list:
                data[i] = [data[i]]
            if len(data[i]) != self._shape[1]:
                raise ValueError("Error in matrix shape")
        self._matrix = data

    def __repr__(self):
        return (
            f"Matrix2D(shape=({self._shape[0]}, {self._shape[1]}), data={self._matrix})"
        )

    def __getitem__(self, key):
        return self._matrix[key]

    def row_echelon_form(self):
        row_echelon_matrix = copy.deepcopy(self._matrix)
        permutations = []
        for i in range(min(self._shape)):
            if row_echelon_matrix[i][i] == 0:
                for j in range(i + 1, self._shape[0]):
                    if row_echelon_matrix[j][i] != 0:
                        permutations.append((i, j))
                        row_echelon_matrix[i], row_echelon_matrix[j] = (
                            row_echelon_matrix[j],
                            row_echelon_matrix[i],
                        )
                        break
                else:
                    continue
            for down_row in row_echelon_matrix[i + 1 :]:
                coef = down_row[i] / row_echelon_matrix[i][i]
                for j, _ in enumerate(down_row):
                    down_row[j] -= row_echelon_matrix[i][j] * coef
        return (Matrix2D(row_echelon_matrix), permutations)

    def triangular_form(self):
        if self._shape[0] != self._shape[1]:
            raise ValueError("It's not a square matrix")
        return self.row_echelon_form()

    def determinant(self):
        triangular_matrix = self.triangular_form()
        result = 1
        for i, row in enumerate(triangular_matrix[0]):
            result *= row[i]
        return result * (-1) ** len(triangular_matrix[1])

    def gaus_method(self, right):
        new_matrix = copy.deepcopy(self._matrix)
        for row_mat, row_right in zip(new_matrix, right):
            row_mat.extend(row_right)

        
        new_matrix = Matrix2D(new_matrix)
        
        echelon_matrix, permutation = new_matrix.row_echelon_form()
        
        for i in reversed(range(echelon_matrix._shape[0])):
            for j in range(self._shape[1]):
                if echelon_matrix[i][j] != 0:
                    div_elem = echelon_matrix[i][j]
                    for k in range(echelon_matrix._shape[1]):
                        echelon_matrix._matrix[i][k] /= div_elem
                    for k in reversed(range(i)):
                        echelon_matrix._matrix[k] = [
                            echelon_matrix[k][l]
                            - echelon_matrix[i][l]
                            * echelon_matrix[k][j]
                            for l in range(new_matrix._shape[1])
                        ]
                    
                    break
        return (echelon_matrix, permutation)

    def inverse_matrix(self):
        if self.determinant == 0:
            return None
        gaus_res, _ = self.gaus_method(
            [[1 if i == j else 0 for j in range(self._shape[1])] for i in range(self._shape[0])]
        )

        inverse_matrix = [row[self._shape[0]:] for row in gaus_res]

        return Matrix2D(inverse_matrix)

    def rank(self):
        result = 0
        for row in self.row_echelon_form()[0]:
            for element in row:
                if element != 0:
                    result += 1
                    break
        return result

    def has_solution(self, vector):
        if len(vector) != self._shape[0]:
            raise ValueError("Different shape matrix and vector")
        wide_matrix = copy.deepcopy(self._matrix)
        for row, elem in zip(wide_matrix, vector):
            row.extend(elem)
        return self.rank() == Matrix2D(wide_matrix).rank()

    def solve_equations(self, vector):
        if not self.has_solution(vector):
            return None
        gaus_res, _ = self.gaus_method(vector)
        solve_matrix = [row[self._shape[0]:] for row in gaus_res]
        return Matrix2D(solve_matrix)