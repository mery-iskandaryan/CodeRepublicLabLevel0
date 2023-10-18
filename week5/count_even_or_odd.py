import count_ones


def count_even_or_odd(n):
    if count_ones.count_ones(n) % 2 == 0:
        return "Even"
    return "Odd"


print(count_even_or_odd(7))
