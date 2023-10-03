def transpose(mat):
    result = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return result


mat = [[i+j for i in range(1, 6)] for j in range(0,15,4)]
for row in mat:
    print(row)

print("\n")

res = transpose(mat)

for row in res:
    print(row)
