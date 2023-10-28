def digit_sum(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n%10
        n //= 10
    return digit_sum




max_sum = 0
for i in range(100):
    for j in range(100):
        if digit_sum(i**j) > max_sum:
            max_sum = digit_sum(i**j)


print(max_sum)
