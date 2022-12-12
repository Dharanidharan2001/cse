"""def rotate_img(matrix):
    n=len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]"""


def rotate_img(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate_img(mat))