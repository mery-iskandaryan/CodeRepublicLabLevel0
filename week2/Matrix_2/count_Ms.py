def count_Ms(sq_mat):
    for i in range(len(mat)):
        for j in range(len(mat)):   #0,2  coun = 1, 2
            if mat[i][j] == 0:
                if i != 0:
                    if mat[i-1][j] == 'M':
                        mat[i][j] += 1
                    if j != 0 and mat[i-1][j-1] == 'M':
                        mat[i][j] += 1
                    if j != len(mat) - 1 and mat[i-1][j+1] == 'M':
                        mat[i][j] += 1
                if i != len(mat) - 1:
                    if mat[i+1][j] == 'M':
                        mat[i][j] += 1
                    if j != 0 and mat[i+1][j-1] == 'M':
                        mat[i][j] += 1
                    if j != len(mat) - 1 and mat[i+1][j+1] == 'M':
                        mat[i][j] += 1
                if j != 0:
                    if mat[i][j-1] == 'M':
                        mat[i][j] += 1
                if j != len(mat) - 1:
                    if mat[i][j+1] == 'M':
                        mat[i][j] += 1
    return sq_mat


mat = [[0, 'M', 0, 'M', 0],
       [0,  0, 'M', 0,  0],
       [0,  0,  0,  0,  0],
       ['M','M',0,  0,  0],
       [0,   0, 0, 'M', 0]]
for row in mat:
    print(row)

print('\n')

count_Ms(mat)
for row in mat:
    print(row)
