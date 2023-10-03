def sum_above_sec_diagonal(mat):
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat)-i-1):
            sum += mat[i][j]
    return sum


mat = [[i + j for i in range(3)] for j in range(0,9,3)]
mat2 = [[0,5,6,4],[7,0,9,3],[1,0,7,1],[1,1,8,7]]
for row in mat:
    print(row)

print(sum_above_sec_diagonal(mat))
