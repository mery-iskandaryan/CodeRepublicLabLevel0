def max_value_array(mat):
    ls = []
    for i in range(len(mat)):
        max = mat[i][0]
        for j in range(len(mat[i])):
            if mat[i][j] > max:
                max = mat[i][j]
        ls.append(max)
    return ls


mat1 =[[4,5],[5,7],[9,8],[10,15]]
for row in mat1:
    print(row)
print('\n')

print(max_value_array(mat1))

