# Function to multiply two matrices from scratch
def matrix_multiplication(A, B):
    # Get the dimensions of the matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Iterate through rows of A
    for i in range(rows_A):
        # Iterate through columns of B
        for j in range(cols_B):
            # Calculate the dot product of row A and column B
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Define two matrices A and B (same as previous example)
A = [[1, 2, 3], [4, 5, 6]]  # 2x3 matrix
B = [[1, 2], [3, 4], [5, 6]]  # 3x2 matrix

# Perform matrix multiplication using the custom function
result_custom = matrix_multiplication(A, B)
print(result_custom)
