size = int(input("Please enter an integer number: "))
ls = []

for i in range(size):
    el = int(input("Enter an element of the list: "))
    if isinstance(el, int):
        ls.append(el)

print(ls)
