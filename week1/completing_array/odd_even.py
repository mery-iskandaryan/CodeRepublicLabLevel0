ls = [1,25,6,7,19,8,9,45,100,9,88]

size = len(ls)
for i in range(int(size/2)):
    if ls[i] % 2 != 0:
        temp = ls[i] #25
        if ls[size-1-i] % 2 == 0:
            ls[i] = ls[size-1-i]
            ls[size-1-i] = temp
        else:
            ls.append(ls[i])
            size += 1
            ls.remove(ls[i])



print(ls)
