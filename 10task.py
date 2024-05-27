class Matrix:
    def __init__(self, rows):
        """
        Initialize a Matrix instance.

        :param rows: A list of lists where each sublist represents a row in the matrix.
        """
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0]) if rows else 0

    def display(self):
        """Display the matrix."""
        for row in self.rows:
            print(row)

    def __add__(self, other):
        """
        Add two matrices.

        :param other: Another matrix instance to be added.
        :return: A new Matrix instance representing the sum of the two matrices.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions to be added")

        result = []
        for i in range(self.num_rows):
            result_row = []
            for j in range(self.num_cols):
                result_row.append(self.rows[i][j] + other.rows[i][j])
            result.append(result_row)

        return Matrix(result)

    def __mul__(self, other):
        """
        Multiply two matrices.

        :param other: Another matrix instance to be multiplied.
        :return: A new Matrix instance representing the product of the two matrices.
        """
        if self.num_cols != other.num_rows:
         raise ValueError("Matrices are not aligned for multiplication")

        result = []
        for i in range(self.num_rows):
            result_row = []
            for j in range(other.num_cols):
                sum_product = 0
                for k in range(self.num_cols):
                    sum_product += self.rows[i][k] * other.rows[k][j]
                result_row.append(sum_product)
            result.append(result_row)

        return Matrix(result)


# Define two matrices
matrix1 = Matrix([
    [1, 2],
    [3, 4]
])

matrix2 = Matrix([
    [5, 6],
    [7, 8]
])

# Perform addition
print("Matrix 1:")
matrix1.display()
print("\nMatrix 2:")
matrix2.display()

print("\nAddition of Matrix 1 and Matrix 2:")
matrix_sum = matrix1 + matrix2
matrix_sum.display()

# Perform multiplication
print("\nMultiplication of Matrix 1 and Matrix 2:")
matrix_product = matrix1 * matrix2
matrix_product.display()
