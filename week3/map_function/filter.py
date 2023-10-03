def filterr(func, lst):
    return [i for i in lst if func(i)]


def even(num):
    return True if num % 2 == 0 else False


print(filterr(even, [1,2,3,4,5,6]))
