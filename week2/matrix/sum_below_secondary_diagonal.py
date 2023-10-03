def sum_below_secondary_diagonal(mat):
    sum = 0
    for i in range(len(mat)-1, 0, -1):
        for j in range(1, i+1):
            sum += mat[i][-j]
    return sum


mat = [[i + j for i in range(3)] for j in range(0, 9, 3)]
mat2 = [[4,5,6,4,1],[7,8,9,3,1],[9,8,7,1,1],[8,8,8,7,0],[0,0,0,0,0]]
for row in mat:
    print(row)
print("\n")

print(sum_below_secondary_diagonal(mat))


