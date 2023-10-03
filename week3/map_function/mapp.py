def mapp(func, data):
    return [triple(i) for i in data]


def triple(num):
    return num * 3


print(mapp([1, 2, 3, 4]))
