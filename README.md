# Sparse Matrix Program

## Overview

This program implements a Sparse Matrix data structure and operations in Python. It's designed to efficiently handle large matrices with many zero elements by only storing non-zero values. The program supports reading matrices from files, performing basic matrix operations (addition, subtraction, multiplication), and outputting the results.

## Features

- Efficient storage of sparse matrices
- File I/O for matrix input
- Matrix addition, subtraction, and multiplication
- User-friendly command-line interface

## Sparse Matrix Class

The `SparseMatrix` class is the core of this program. It uses a dictionary to store only non-zero elements, with the key being a tuple of (row, column, value) and the value being the non-zero element.

### Key Methods

- `getElement(self, curr_row, curr_col)`: Returns the value at the specified position.
- `setElement(self, curr_row, curr_col, value)`: Sets the value at the specified position.
- `_load_from_file(self, file_path)`: Private method to load a matrix from a file.

### Magic Methods

The class implements several magic methods to enable intuitive matrix operations:

- `__add__(self, other)`: Implements matrix addition (A + B).
- `__sub__(self, other)`: Implements matrix subtraction (A - B).
- `__mul__(self, other)`: Implements matrix multiplication (A \* B).
- `__str__(self)`: Provides a string representation of the matrix.

## How to Run

1. Ensure you have Python 3.x installed on your system.

2. Run the program from the command line:

   ```
   python sparse-matrix.py
   ```

3. Follow the prompts to:

   - Choose an operation (addition, subtraction, or multiplication)
   - Select input files from the list of available files in the ./sample_inputs directory

4. The program will display the result of the operation.

## Example Usage

## Error Handling

The program includes error handling for:

- Invalid input file formats
- Incompatible matrix dimensions for operations
- File I/O errors

If an error occurs, an appropriate error message will be displayed.
