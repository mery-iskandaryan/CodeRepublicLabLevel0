def biggest_power_two(n):
    if n & n-1 == 0:
        return n
    return biggest_power_two(n-1)


def power_two(n):
    for i in range(n, 1, -1):
        if i & i-1 == 0:
            return i


print(biggest_power_two(49))
#print(power_two(33))
