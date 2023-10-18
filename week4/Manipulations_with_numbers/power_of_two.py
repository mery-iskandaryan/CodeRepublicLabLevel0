def power_of_two(n):
    if n & n - 1 == 0:
        return 'YES'
    return 'NO'


print(power_of_two(78))


