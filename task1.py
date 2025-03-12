def transpose_matrix(matrix):
    """function to transponse a given matrix."""
    rows = len(matrix) #Number of rows
    cols = len(matrix[0]) if rows > 0 else 0 #Number of columns
    