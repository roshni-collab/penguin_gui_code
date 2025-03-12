def print_matrix(matrix):
    """Helper Function to print a matrix in a readable format."""
    for row in matrix:
        print(row)
    print()




def transpose_matrix(matrix):
    """function to transponse a given matrix."""
    rows = len(matrix) #Number of rows
    cols = len(matrix[0]) if rows > 0 else 0 #Number of columns

    print ("Orginial Matrix:")
    print_matrix(matrix) # Display original Matrix

    # Initialize the transposed matrix with empty lists
    transposed = [[0] * rows for _ in range(cols)]  # Creating cols x rows matrix

    #Loop through rows
    for i in range(rows):
        pass # Placeholder for now.


    