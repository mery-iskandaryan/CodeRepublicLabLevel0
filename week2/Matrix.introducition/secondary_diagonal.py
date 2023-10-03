def secondary_diag(sq_mat):
    diag_sum = 0
    for i, row in enumerate(sq_mat):
        diag_sum += row[-i-1]
    return diag_sum


sq_mat = [[i + j for i in range(4)] for j in range(0, 13, 4)]
mat = [[i + j for i in range(3)] for j in range(0,9,3)]
for row in sq_mat:
    print(row)


def secondary_dia(sq_mat):
    diag_sum = 0
    for i in range(len(sq_mat)):
        for j in range(i, i+1):
            diag_sum += sq_mat[i][-j-1]
    return diag_sum

print(secondary_dia(sq_mat))
