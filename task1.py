def transpose_matrix(matrix):
    """function to transponse a given matrix."""
    rows = len(matrix) #Number of rows
    cols = len(matrix[0]) if rows > 0 else 0 #Number of columns

    # Initialize the transposed matrix with empty lists
    transposed = [[0] * rows for _ in range(cols)]  # Creating cols x rows matrix
    