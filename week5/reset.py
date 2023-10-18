def resett(n, i):
    if (n >> i) % 2 == 0:
        return n
    return n - 2**i


def reset(n, i):
    changed = ~(1 << i)
    result = n & changed
    return result

# print(resett(18, 1))
print(resett(18, 3))
# print(resett(16, 3))
# print(resett(15, 3))

print(reset(18, 3))
