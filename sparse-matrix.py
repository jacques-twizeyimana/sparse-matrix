import os

class SparseMatrix:
    """
    A class to represent a sparse matrix, which is a matrix primarily composed of zero-valued elements.
    """

    def __init__(self, matrix_file_path=None, num_rows=0, num_cols=0):
        """
        Initializes the sparse matrix. If a file path is provided, it loads the matrix from the file.

        Parameters:
        matrix_file_path (str, optional): Path to the file containing the matrix data.
        num_rows (int, optional): Number of rows in the matrix. Default is 0.
        num_cols (int, optional): Number of columns in the matrix. Default is 0.
        """
        self.num_rows = num_rows  # Number of rows in the matrix
        self.num_cols = num_cols  # Number of columns in the matrix
        self.matrix = {}  # Dictionary to store non-zero elements with keys as (row, col) tuples

        # create output folder if not exists
        if not os.path.exists('./output'):
            os.makedirs('./output')
        
        if matrix_file_path:
            self._load_from_file(matrix_file_path)
    
    def _load_from_file(self, file_path):
        """
        Loads the matrix data from a file.

        Parameters:
        file_path (str): Path to the file containing the matrix data.

        Raises:
        ValueError: If the input file format is incorrect.
        """
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
        """
        Retrieves the value at the specified position in the matrix.

        Parameters:
        curr_row (int): The row index of the element.
        curr_col (int): The column index of the element.

        Returns:
        int: The value at the specified position, or 0 if the position is not explicitly stored in the sparse matrix.
        """
        return self.matrix.get((curr_row, curr_col), 0)
    
    def setElement(self, curr_row, curr_col, value):
        """
        Sets the value at the specified position in the matrix.

        Parameters:
        curr_row (int): The row index of the element.
        curr_col (int): The column index of the element.
        value (int): The value to be set at the specified position.
        """

        if value != 0:
            self.matrix[(curr_row, curr_col)] = value
        elif (curr_row, curr_col) in self.matrix:
            del self.matrix[(curr_row, curr_col)]
    
    def __add__(self, other):
        """
        Magic method to add two sparse matrices.

        Parameters:
        other (SparseMatrix): The other sparse matrix to be added.

        Returns:
        SparseMatrix: The result of adding the two sparse matrices.
        """

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
        """
        Magic method to subtract one sparse matrix from another (this).

        Parameters:
        other (SparseMatrix): The other sparse matrix to be subtracted.

        Returns:
        SparseMatrix: The result of subtracting the second sparse matrix from the first.
        """

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
        """
        Magic method to multiply two sparse matrices.

        Parameters:
        other (SparseMatrix): The other sparse matrix to be multiplied.

        Returns:
        SparseMatrix: The result of multiplying the two sparse matrices.
        """

        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions are not compatible for multiplication")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        
        for (i, k), value_a in self.matrix.items():
            for (k2, j), value_b in other.matrix.items():
                if k == k2:
                    result.setElement(i, j, result.getElement(i, j) + value_a * value_b)
        
        return result
    
    def __str__(self):
        """
        Returns a string representation of the sparse matrix.

        Returns:
        str: (rows, cols, value) for each non-zero element in the matrix.
        """

        output = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (row, col), value in sorted(self.matrix.items()):
            output += f"({row}, {col}, {value})\n"
        return output

def get_sample_files(message):
    """
    Get the sample files from ./sample_input folder 
    and ask user to choose from any of them or to enter file path

    Parameters:
    message (str): Message to display to the user.

    Returns:
    str: File path of the selected file.
    """

    files = os.listdir('./sample_input')
    print(message)
    for i, file in enumerate(files):
        print(f"\t{i+1}. {file}")
    print("\t0. Enter my own file path")
    choice = input("\n\tEnter your choice: ")
    if choice == '0':
        file_path = input("\tEnter the file path: ")
    else:
        file_path = f"./sample_input/{files[int(choice)-1]}"
    return file_path

def main():
    """
    Main function to let the user choose the operation and 
    input files for sparse matrix operations.
    """

    print("\n************* Sparse Matrix Operations *************\n")
    print("\t\t1. Addition")
    print("\t\t2. Subtraction")
    print("\t\t3. Multiplication")
    choice = input("\n\tEnter your choice: ")

    #load files from ./sample_input and ask user to choose or enter file path
    file_path1 = get_sample_files("\n\t#### Choose the first matrix file:\n")
    file_path2 = get_sample_files("\n\t#### Choose the second matrix file:\n")

    matrix1 = SparseMatrix(file_path1)
    matrix2 = SparseMatrix(file_path2)
    
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

    # write result to file1_operation_file2.txt
    output_file = file_path1.split("/")[-1].split(".")[0] + "_" + operation + "_" + file_path2.split("/")[-1].split(".")[0] + ".txt"
    with open(f'./output/{output_file}', 'w') as file:
        file.write(str(result))

    print(result)

if __name__ == "__main__":
    main()