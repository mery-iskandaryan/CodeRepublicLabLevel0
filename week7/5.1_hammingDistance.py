def hammingDistance(x, y):
    count = 0

    while max(x, y):
        if x % 2 != y % 2:
            count += 1
        x //= 2
        y //= 2

    return count

