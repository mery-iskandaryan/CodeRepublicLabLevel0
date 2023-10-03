def sum_above_diag(sq_mat):
    sum = 0
    for i in range(len(sq_mat)):
        for j in range(i, len(sq_mat)):
            sum += sq_mat[i][j]
    return sum


mat = [[i + j for i in range(4)] for j in range(0,13,4)]
for row in mat:
    print(row)


def sum_above_dia(sq_mat):
    sum = 0
    for i in range(len(sq_mat)):
        for j in range(1, len(mat) - i):
            sum += mat[i][-j]
    return sum


print(sum_above_diag(mat))


