ls = [1,5,-87,5,58,99,87,0,4,6,10]
max_index = 0
for i in range(len(ls)):
    if ls[i]>ls[max_index]:
        max_index = i

print(max_index)
