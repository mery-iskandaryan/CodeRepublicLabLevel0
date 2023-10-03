mat = [[i + j for i in range(1, 6)] for j in range(0, 25, 5)]

for row in mat:
    print(row)

print("\n")

print([i[:3:2] for i in mat])

# col1 = [row[0] for row in mat]
# col2 = [row[2] for row in mat]
# print(col1, col2)
#print([i[:3:2] for i in mat])
