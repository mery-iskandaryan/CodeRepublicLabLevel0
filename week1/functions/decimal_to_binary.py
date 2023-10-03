def binary(num):
    bin = ''
    while num > 0:
        digit = str(num % 2)
        bin += digit
        num = num // 2
    return bin[::-1]

print(binary(98))

