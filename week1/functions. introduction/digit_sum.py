def digit_sum(num):
    sum = 0
    while num:
        sum += num % 10
        num = int(num // 10)

    return sum

print(digit_sum(82))



