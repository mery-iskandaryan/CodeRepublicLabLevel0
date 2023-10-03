def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)


print(factorial(4   ))

# fac(5) = 5 * fac(4) //120
# fac(4) = 4 * fac(3) //24
# fac(3) = 3 * fac(2) //6
# fac(2) = 2 * fac(1) //2
# fac(1) = 1 * fac(0) //1
