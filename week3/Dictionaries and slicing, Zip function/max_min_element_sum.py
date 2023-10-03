mat = [[i+j for i in range(1,6)] for j in range(0,25,5)]

for row in mat:
    print(row)
print("\n")
col1 = [row[0] for row in mat]
col2 = [row[3] for row in mat]


# print(min(col1) + min(col2) + max(col2) + max(col1))


mat1 = mat[:4:3]

for i in mat1:
    print(i)

for i in mat1:
    print(min(i) + max(i))

