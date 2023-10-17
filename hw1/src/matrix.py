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
        for i, _ in enumerate(row_echelon_matrix):
            if row_echelon_matrix[i][i] == 0:
                for j in range(i + 1, self._shape[1]):
                    if row_echelon_matrix[j][i] != 0:
                        permutations.append((i,j))
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
        return result*(-1)**len(triangular_matrix[1])
    

class Vector(Matrix2D):
    def __init__(self, data: List):
        super().__init__(data)
        if self._shape[0] != 1 and self._shape[1] != 1:
            raise ValueError("This matrix can't to be vector")

    def __getitem__(self, key):
        if self._shape[0] == 1:
            return self._matrix[0][key]
        else:
            return self._matrix[key][0]
    
    def __len__(self):
        if self._shape[0] == 1:
            return self._shape[1]
        else:
            return self._shape[0]

