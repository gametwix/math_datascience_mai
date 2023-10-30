from src.matrix import Matrix2D
from pathlib import Path

def matrix_calc_write(file, matrix, vector=None):
    matrix = Matrix2D(matrix)
    rank = matrix.rank()
    file.write(f'rank = {rank}\n')
    try:
        determinant = matrix.determinant()
        file.write(f'determinant = {round(determinant, 3)}\n')
    except ValueError as error:
        file.write('Determinant does not exist\n')
    try:
        inverse = matrix.inverse_matrix()
        if inverse is None:
            raise ValueError
        file.write(f'inverse = {inverse}\n')
    except ValueError as error:
        file.write('Inverse matrix does not exist\n')

    if vector is not None:
        vector = [[elem] for elem in vector[0]]
        try:
            has_solution = matrix.has_solution(vector)
            if has_solution:
                solution = matrix.solve_equations(vector)
                file.write(f'equation solution = {solution}\n')
            else:
                raise ValueError
        except ValueError:
            file.write('Equation does not have solution\n')
    file.write("%\n")

def parse_write_file(input_file, output_file):
    elems = []
    for line in input_file:
        if line.strip() == "%":
            matrix_calc_write(output_file, *elems)
            elems = []
        else:
            data_str = line.split("(")[1].split(")")[0]
            input_data = data_str.split(";")
            for i in range(len(input_data)):
                input_data[i] = input_data[i].split()
                input_data[i] = list(map(int, input_data[i]))
            elems.append(input_data)

if __name__ == "__main__":
    filepath = Path(input("Enter filepath: "))
    if not filepath.is_file():
        print(f"File path '{filepath.resolve()}' does not exist")
        exit()
    with open(filepath) as rf:
        with open("output.txt", "w") as wf:
            parse_write_file(rf, wf)