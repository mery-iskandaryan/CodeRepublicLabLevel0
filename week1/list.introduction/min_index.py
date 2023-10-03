ls = [1,5,-87,5,58,99,87,0,4,6,10]
min_index = 0
for i in range(len(ls)):
    if ls[i]<ls[min_index]:
        min_index = i

print(min_index)
