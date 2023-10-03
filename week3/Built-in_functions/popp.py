def popp(lst, index=-1):
    res = lst[index]
    lst.remove(res)
    return res


lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)
a = popp(lst,2)
print(a)
