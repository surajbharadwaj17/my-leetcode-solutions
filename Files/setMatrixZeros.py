"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
"""

def setZeroes(matrix):
    m,n = len(matrix), len(matrix[0])

    rc_pairs = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rc_pairs.append((i,j))

    for pair in rc_pairs:
        r,c = pair[0],pair[1]

        for p in range(n):
            matrix[r][p] = 0

        for q in range(m):
            matrix[q][c] = 0

    print(matrix)


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

setZeroes(matrix)
