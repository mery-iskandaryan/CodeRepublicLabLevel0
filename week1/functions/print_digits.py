def print_digits(num):
    ls = []
    while num > 0:
       ls.append(str(num%10))
       num = num // 10
    return ls[::-1]



print(print_digits(456))

