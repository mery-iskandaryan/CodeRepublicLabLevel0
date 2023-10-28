def digit_pow_five_sum(num):
    sum = 0
    num_copy = num
    while num > 0:
        sum += (num%10)**5
        num //= 10
    return sum == num_copy


digit_pow_five = 0
for num in range(2, 1000000):
    if digit_pow_five_sum(num):
        digit_pow_five += num


print(digit_pow_five)
