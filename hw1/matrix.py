from typing import List
from pathlib import Path


class Matrix2D:
    def __init__(self, data: List):
        self._shape = (len(data), 1 if type(data[0]) is not list else len(data[0]))
        for i in range(len(data)):
            if type(data[0]) is not list:
                data[i] = [data[i]]
            if len(data[i]) != self._shape[1]:
                raise ValueError("Error in matrix shape")
        self._matrix = data


    

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
                    # do something
                else:
                    pass
                    # do something
                elems = []
            else:
                data_str = line.split('(')[1].split(')')[0]
                input_data = data_str.split(';')
                for i in range(len(input_data)):
                    input_data[i] = input_data[i].split()
                    input_data[i] = list(map(int, input_data[i]))
                elems.append(input_data)