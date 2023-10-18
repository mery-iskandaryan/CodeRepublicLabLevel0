def binary_number(n):
    binary = ''
    while n > 0:
        binary += str(n % 2)
        n //= 2
    return binary[::-1]


print(binary_number(8))


