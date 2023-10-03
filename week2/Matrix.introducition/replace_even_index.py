def replace_to_zero(sq_mat):
    ls = []
    for i in range(len((sq_mat))):
        for j in range(len(sq_mat)):
            if i % 2 == 0:
                sq_mat[i][j] = 0
    return sq_mat


mat2 = [[4,5,6,4],[7,8,9,3],[9,8,7,1],[8,8,8,7]]
for row in mat2:
    print(row)

print('\n')
mat = replace_to_zero(mat2)
for row in mat:
    print(row)

