def symmetric(sq_mat):
    for i in range(len(sq_mat)):
        for j in range(i, len(sq_mat)):
            sq_mat[i][j], sq_mat[j][i] = sq_mat[j][i], sq_mat[i][j]
    return sq_mat


mat = [[i + j for i in range(1, 4)] for j in range(0, 9, 3)]
mat2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for row in mat:
    print(row)
print('\n')


res = symmetric(mat)
for row in res:
    print(row)

