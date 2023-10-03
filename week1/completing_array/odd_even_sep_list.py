ls = [1,25,6,7,19,8,9,45,100,9,88]

odd_ls = []
even_ls = []

for i in ls:
    if i % 2 == 0:
        even_ls.append(i)

    else:
        odd_ls.append(i)

print(even_ls+odd_ls)
