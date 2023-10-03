mat = [[i+j for i in range(1, 5)] for j in range(0,15,4)]
for row in mat:
    print(row)

print([sum(row) for row in mat])

ls = []
for row in mat:
    sum = 0
    for el in row:
        sum += el
    ls.append(sum)

# print(ls)
