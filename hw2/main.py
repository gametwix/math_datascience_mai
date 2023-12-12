import sys

sys.path.append('../')

from hw1.src.matrix import Matrix2D
from pathlib import Path
import argparse
import math

def matrix_calc_write(file, matrix, vector=None, kernel_type="norm"):
    matrix = Matrix2D(matrix)

    if vector is not None:
        vector = [[elem] for elem in vector[0]]
        try:
            has_solution = matrix.has_solution(vector)
            if has_solution:
                solution = matrix.solve_equations(vector)
                file.write('equation solution = ')
                if solution._shape[1] == 1:
                    file.write(f'{solution}\n')
                else:
                    static = [x[-1] for x in solution] + [0]*(solution._shape[1]-1)
                    file.write(f'{Matrix2D(static)}')
                    for i in range(solution._shape[1]-1):
                        dynamic =  [-x[i] for x in solution] + [0]*i + [1] + [0]*(solution._shape[1]-2)
                        file.write(f'+{Matrix2D(dynamic)}*x{matrix._shape[0]+1+i}')
                    file.write('\n')
                    
            else:
                raise ValueError
        except ValueError:
            file.write('Equation does not have solution\n')
    else:
        vector = [[0] for i in range(matrix._shape[0])]
        try:
            has_solution = matrix.has_solution(vector)
            if has_solution:
                solution = matrix.solve_equations(vector)
                file.write('Ker = ')
                if solution._shape[1] == 1:
                    file.write(f'{solution}\n')
                else:
                    for i in range(solution._shape[1]-1):
                        numbers = [-x[i] for x in solution]
                        if kernel_type == "int":
                            max_float_point = max([str(round(x,3))[::-1].find('.') for x in numbers])
                            dynamic =  [-round(x[i],3)*10**max_float_point for x in solution] + [0]*i + [1*10**max_float_point] + [0]*(solution._shape[1]-2)
                            file.write(f'{"+" if i == 0 else ""}{Matrix2D(dynamic)}*x{matrix._shape[0]+1+i}')
                        else:
                            normal = math.sqrt(sum([x**2 for x in numbers])+1)
                            dynamic =  [-round(x[i],3)/normal for x in solution] + [0]*i + [1/normal] + [0]*(solution._shape[1]-2)
                            file.write(f'{"+" if i == 0 else ""}{Matrix2D(dynamic)}*x{matrix._shape[0]+1+i}')
                    file.write('\n')
                    
            else:
                raise ValueError
        except ValueError:
            file.write('Equation does not have solution\n')
    file.write("%\n")

def parse_write_file(input_file, output_file, kernel='norm'):
    elems = []
    for line in input_file:
        if line.strip() == "%":
            matrix_calc_write(output_file, *elems, kernel_type=kernel)
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
    kernel = input("Write 'int' if you want integer kernel vectors and 'norm' if normal: ")
    with open(filepath) as rf:
        with open("output.txt", "w") as wf:
            parse_write_file(rf, wf, kernel)