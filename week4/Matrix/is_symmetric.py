def is_symmetric(mat):
    tr = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat))]
    return mat == tr


mat1 = [[i+j for i in range(1,4)] for j in range(0,9,3) ]
mat = [[1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]]
for row in mat1:
    print (row)
print("\n")
print(is_symmetric(mat))
