size = int(input("Please enter the size of the array: "))
ls = []
for i in range(size):
    ls.append(input("Enter a number: "))

max_index = 0
min_index = 0
for i in range(len(ls)):
    if ls[i] > ls[max_index]:
        max_index = i
    if ls[i] < ls[min_index]:
        min_index = i

print(max_index-min_index)

