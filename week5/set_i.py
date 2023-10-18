def set_i(n, i):
    return n ^ 2 ** i


def set(n, i):
    changed = 1 << i
    return n | changed


print(set(9, 1))
print(set_i(9, 1))


