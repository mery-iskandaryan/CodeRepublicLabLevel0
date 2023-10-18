def magic_matrix(mat):
    sum_row = [sum(row) for row in mat]
    sum_col = [sum([row[i] for i in range(len(mat))]) for row in mat]
    diag_sum = sum([mat[i][i] for i in range(len(mat))])
    second_diag_sum = sum([a[i][-i - 1] for i in range(len(a))])
    tmp = sum_row[0]
    for i in range(len(sum_row)):
        if sum_row[i] != tmp or sum_col[i] != tmp or diag_sum != tmp or second_diag_sum != tmp:
            return "Not Magic"
    return "Magic"


a = [[2, 7, 6],  # [0][-1]   [1][-2]   [2][-3]
     [9, 5, 1],
     [4, 3, 8]]

b = [[2, 7, 6],
     [9, 5, 1],
     [7, 3, 8]]

c = [[4, 9, 2],  # [0][-1]   [1][-2]   [2][-3]
     [3, 5, 7],
     [8, 1, 6]]

print(magic_matrix(a))
print(magic_matrix(b))
print(magic_matrix(c))
