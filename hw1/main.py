from src.matrix import Matrix2D, Vector

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