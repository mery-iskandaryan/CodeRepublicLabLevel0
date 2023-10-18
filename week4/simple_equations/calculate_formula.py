def formula(n, x):
    summ = 0
    for i in range(1, n+1):
        summ += (((-1)**i) * (x**(i+1)/(factorial(3*i) + 2**(i+1))))
    return summ


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(formula(3, 4))
