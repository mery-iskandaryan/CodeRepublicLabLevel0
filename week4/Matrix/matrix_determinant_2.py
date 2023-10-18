def determinant(mat):
    prod = 1
    sec_prod = 1
    for i in range(len(mat)):
        prod *= mat[i][i]
        for j in range(i, i+1):
            sec_prod *= mat[i][-j-1]
    return prod - sec_prod


mat = [[2,5],
       [9,8]]


print(determinant(mat))

