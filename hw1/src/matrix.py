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

    def triangular_form(self):
        if self._shape[0] != self._shape[1]:
            raise ValueError("It's not a square matrix")

        triangular_matrix = copy.deepcopy(self._matrix)
        count_permutations = 0
        for i, _ in enumerate(triangular_matrix):
            if triangular_matrix[i][i] == 0:
                for j in range(i + 1, self._shape[1]):
                    if triangular_matrix[j][i] != 0:
                        count_permutations += 1
                        triangular_matrix[i], triangular_matrix[j] = (
                            triangular_matrix[j],
                            triangular_matrix[i],
                        )
                        break
                else:
                    continue
            for down_row in triangular_matrix[i + 1 :]:
                coef = down_row[i] / triangular_matrix[i][i]
                for j, _ in enumerate(down_row):
                    down_row[j] -= triangular_matrix[i][j] * coef
        return (Matrix2D(triangular_matrix), count_permutations)


class Vector(Matrix2D):
    def __init__(self, data: List):
        super().__init__(data)
        if self._shape[0] != 1 and self._shape[1] != 1:
            raise ValueError("This matrix can't to be vector")


if __name__ == "__main__":
    filepath = Path(input("Enter filepath: "))
    if not filepath.is_file():
        print(f"File path '{filepath.resolve()}' does not exist")
        exit()
    with open(filepath) as f:
        elems = []
        for line in f:
            if line.strip() == "%":
                matrix = Matrix2D(elems[0])
                if len(elems) == 2:
                    vector = Vector(elems[1])
                    print(matrix.triangular_form())
                else:
                    print(matrix.triangular_form())
                elems = []
            else:
                data_str = line.split("(")[1].split(")")[0]
                input_data = data_str.split(";")
                for i in range(len(input_data)):
                    input_data[i] = input_data[i].split()
                    input_data[i] = list(map(int, input_data[i]))
                elems.append(input_data)
