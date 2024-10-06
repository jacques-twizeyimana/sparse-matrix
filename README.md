# Sparse Matrix Program

## Overview

This program implements a Sparse Matrix data structure and operations in Python. The program supports reading matrices from files, performing basic matrix operations (addition, subtraction, multiplication), and outputting the results.

<img width="568" alt="image" src="https://github.com/user-attachments/assets/20be5e08-663a-4dd5-b601-652054ea1eb0">

## Features

- Efficient storage of sparse matrices
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

Choose Operation you want
<img width="568" alt="image" src="https://github.com/user-attachments/assets/20be5e08-663a-4dd5-b601-652054ea1eb0">

Select input files or type file path
<img width="513" alt="image" src="https://github.com/user-attachments/assets/354f0f77-1f25-42e9-b579-e1a243499fa2">

Result of operation will be printed on screen and written in a file
<img width="513" alt="image" src="https://github.com/user-attachments/assets/d44df9f0-9791-4ea7-9d53-de3eeac34815">



## Error Handling

The program includes error handling for:

- Invalid input file formats
- Incompatible matrix dimensions for operations
- File I/O errors

If an error occurs, an appropriate error message will be displayed.
