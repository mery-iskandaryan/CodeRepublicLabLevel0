def check_col_min(j, mat):
    return min(x[j] for x in mat)


def check_row_max(i, mat):
    return max(mat[i])


def tambayin_ket(mat):
    d = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == check_row_max(i, mat) == check_col_min(j, mat):
                d[mat[i][j]] = (i, j)
    return d


mat = [[4, 5, 6],
       [15, 14, 13],
       [25, 26, 27]]

print(tambayin_ket(mat))

