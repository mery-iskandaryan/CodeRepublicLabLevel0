def main_diag_sum(square_mat):
    sum = 0
    for i in range(len(square_mat)):
        sum += square_mat[i][i]
    return sum


mat = [[i + j for i in range(3)] for j in range(0,9,3)]
mat2 = [[4,5,6,7],[7,8,9,4],[0,0,2,0],[9,8,7,6]]
for row in mat:
    print(row)

print(main_diag_sum(mat))
