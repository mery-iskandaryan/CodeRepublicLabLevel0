def symbol_reverse(ls):
    for i in range(len(ls)//2):
        temp = ls[i]
        ls[i] = ls[len(ls)-1-i]
        ls[len(ls)-1-i] = temp
    return (ls)


ls = ['a','b','c','d','e','f']
print(symbol_reverse(ls))


#print(ls[::-1])
