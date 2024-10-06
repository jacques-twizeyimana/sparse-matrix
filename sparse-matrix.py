class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=0, num_cols=0):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = {}
        
        if matrix_file_path:
            self._load_from_file(matrix_file_path)
    
    def _load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Parse rows and columns
            self.num_rows = int(lines[0].split('=')[1])
            self.num_cols = int(lines[1].split('=')[1])
            
            # Parse matrix entries
            for line in lines[2:]:
                line = line.strip()
                if not line:
                    continue
                if not (line.startswith('(') and line.endswith(')')):
                    raise ValueError("Input file has wrong format")
                
                values = line[1:-1].split(',')
                if len(values) != 3:
                    raise ValueError("Input file has wrong format")
                
                row, col, value = map(int, values)
                self.setElement(row, col, value)
    
    def getElement(self, curr_row, curr_col):
        return self.matrix.get((curr_row, curr_col), 0)
    
    def setElement(self, curr_row, curr_col, value):
        if value != 0:
            self.matrix[(curr_row, curr_col)] = value
        elif (curr_row, curr_col) in self.matrix:
            del self.matrix[(curr_row, curr_col)]
    
    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for addition")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        
        for (row, col), value in self.matrix.items():
            result.setElement(row, col, value + other.getElement(row, col))
        
        for (row, col), value in other.matrix.items():
            if (row, col) not in self.matrix:
                result.setElement(row, col, value)
        
        return result
    
    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for subtraction")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        
        for (row, col), value in self.matrix.items():
            result.setElement(row, col, value - other.getElement(row, col))
        
        for (row, col), value in other.matrix.items():
            if (row, col) not in self.matrix:
                result.setElement(row, col, -value)
        
        return result
    
    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        
        for (i, k), value_a in self.matrix.items():
            for (k2, j), value_b in other.matrix.items():
                if k == k2:
                    result.setElement(i, j, result.getElement(i, j) + value_a * value_b)
        
        return result
    
    def __str__(self):
        output = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (row, col), value in sorted(self.matrix.items()):
            output += f"({row}, {col}, {value})\n"
        return output

def load_matrix(file_path):
    return SparseMatrix(file_path)

def main():
    print("Sparse Matrix Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Enter your choice (1/2/3): ")
    
    file_path1 = input("Enter the file path for the first matrix: ")
    file_path2 = input("Enter the file path for the second matrix: ")
    
    matrix1 = load_matrix(file_path1)
    matrix2 = load_matrix(file_path2)
    
    if choice == '1':
        result = matrix1 + matrix2
        operation = "Addition"
    elif choice == '2':
        result = matrix1 - matrix2
        operation = "Subtraction"
    elif choice == '3':
        result = matrix1 * matrix2
        operation = "Multiplication"
    else:
        print("Invalid choice")
        return
    
    print(f"\nResult of {operation}:")
    print(result)

if __name__ == "__main__":
    main()