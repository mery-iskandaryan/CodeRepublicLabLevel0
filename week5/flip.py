def flip(n, i):
    if (n >> i) % 2 == 0:
        return n + 2**i
    return n - 2**i


print(flip(22, 4))
print(flip(22, 0))
print(flip(22, 1))
