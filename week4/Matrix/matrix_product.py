def mat_product(mat1, mat2):
    res_mat = [[0 for _ in range(len(mat1))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            sum = 0
            for k in range(len(mat1)):
                sum += mat1[i][k] * mat2[k][j]
            res_mat[i][j] = sum
    return res_mat


a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[3,4,5],
     [6,7,8],
     [9,10,11]]

a = mat_product(a, b)
for row in a:
    print(row)

