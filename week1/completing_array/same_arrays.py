ls1 = [1,2,3,4,5,6,7,8,9]
ls2 = [1,2,3,4,5,6,7,8,9]
counter = 0

if len(ls1) == len(ls2):
    for i in range(len(ls1)):
        if ls1[i] == ls2[i]:
            counter += 1
    print(counter == len(ls1))
else:
    print("The arrays have different lengths.")

