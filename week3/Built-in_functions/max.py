def maxx(iterable):
    maxx = 0
    for i in iterable:
        if i > maxx:
            maxx = i
    return maxx


b = [1, 2, 58, 9, 5, 55, 554, 0]
print(maxx(b))
