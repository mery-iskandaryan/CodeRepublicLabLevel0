def max_value(mat):
    max = mat[0][0]
    for i in mat:
        for j in i:
            if j > max:
                max = j
    return max


mat = [[i+j for i in range(4)] for j in range(0, 5, 4)]
for row in mat:
    print(row)


print(max_value(mat))
