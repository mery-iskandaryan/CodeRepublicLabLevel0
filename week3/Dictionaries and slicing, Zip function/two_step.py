def reverse_slice(lst):
    ls = lst[::-1]
    return ls[1::2]


lst = [9,8,7,6,5,4,3,2,1]
print(reverse_slice(lst))
