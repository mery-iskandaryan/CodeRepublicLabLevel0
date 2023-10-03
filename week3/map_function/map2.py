def map2(func, data1, data2):
    return [func(data1[i], data2[i]) for i in range(len(data1))]


def sum(a,b):
    return a+b


def exp(base, exp):
    return base ** exp


print(map2(exp, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
