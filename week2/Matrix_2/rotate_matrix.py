def rotate_matrix(mat):
    for i in range(len(mat)//2):
        mat[i], mat[-i-1][::-1] = mat[-i-1][::-1], mat[i]
    return mat


mat = [[i + j for i in range(1,5)] for j in range(0,13,4)]
mat1 = [[i + j for i in range(5)] for j in range(0,26,5)]
for row in mat:
    print(row)

print('\n')

rotate_matrix(mat)
for row in mat:
    print(row)
