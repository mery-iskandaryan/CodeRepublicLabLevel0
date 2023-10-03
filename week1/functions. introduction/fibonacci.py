def fibonacci(num):
    res = 0
    temp1 = 0
    temp2 = 1
    if num in (1,2):
        return num - 1

    for i in range(2,num):
        res = temp1 + temp2
        temp1 = temp2
        temp2 = res
    return res


print(fibonacci(5))
