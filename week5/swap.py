def swap_bits(number, i, j):
    swapped_i = (number >> i) & 1
    swapped_j = (number >> j) & 1
    if swapped_i != swapped_j:
        number ^= (1 << i)
        number ^= (1 << j)
    return number


print(swap_bits(9, 0, 1))
