def mat_sum(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]


def summ(mat1, mat2):
    ls = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        ls.append(row)
    return ls


a = [[1,2],
    [3,4]]
b = [[4,5],
    [6,7]]
print(mat_sum(a, b))
