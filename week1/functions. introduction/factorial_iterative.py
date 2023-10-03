def factorial(num):
    fact = 1
    if num == 0:
        fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

print(factorial(4))
