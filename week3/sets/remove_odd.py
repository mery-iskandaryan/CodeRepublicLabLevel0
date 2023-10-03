set1 = {1, 2, 3, 4}


for i in set1.copy():
    if i % 2 != 0:
        set1.remove(i)
        set1.add(i*16)

print(set1)
#help(set)

