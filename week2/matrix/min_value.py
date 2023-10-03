def min_value(mat):
    min = mat[0][0]
    for i in mat:
        for j in i:
            if j < min:
                min = j
    return min


mat = [[i+j for i in range(4)] for j in range(0, 5, 4)]
for row in mat:
    print(row)


print(min_value(mat))
