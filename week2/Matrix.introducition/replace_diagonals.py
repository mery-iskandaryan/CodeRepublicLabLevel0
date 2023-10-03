"""def replace_diagonals(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j:
                temp = mat[i][j]
                mat[i][j] = mat[i][-j-1]
                mat[i][-j-1] = temp
    return mat """

mat = [[i + j for i in range(3)] for j in range(0, 9, 3)]
for row in mat:
    print(row)

print("\n")

# mat1 = replace_diagonals(mat)
# for row in mat:
#    print(row)


def replace_diagonals(mat):
    for i in range(len(mat)):
        temp = mat[i][i]
        mat[i][i] = mat[i][-i-1]
        mat[i][-i-1] = temp
    return mat


res = replace_diagonals(mat)
for row in res:
    print(row)
