def log_a(n, a):
    x = 0.0001

    if 0 < n < 1:
        x = -0.0001
        while True:
            if n - a ** x > 0.0000001:
                return x
            x -= 0.000001
    while True:
        if n - a ** x < 0.0000001:
            return x
        x += 0.000001


print(f"Logarithm 1/16 with base 4 is {log_a(1/16, 4)}")
print(f"Logarithm 1/16 with base 4 is {log_a(8, 2)}")















