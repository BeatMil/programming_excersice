matrix = [[1,2,3],[4,5,6],[7,8,9]]

def rotate_matrix():
    for i in matrix:
        print(i)
    print('rotated')
    box = matrix[2][0] #7
    matrix[2][0] = matrix[0][0] #1
    matrix[0][0] = box
    for i in matrix:
        print(i)

def is_matrix(matrix):
    count = 0 # matrix has 3 list inside
    if len(matrix) == 3:
        for i in matrix:
            if type(i) == list:
                count += 1
    else:
        print('This is not the matrix')
    if count == 3:
        print('This is the matrix')

is_matrix(matrix)