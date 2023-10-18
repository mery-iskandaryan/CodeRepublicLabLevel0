def log_base_two(n):
    x = 0.0001
    if 0 < n < 1:
        x = -0.0001
        while True:
            if n - 2 ** x > 0.0000001:
                return x
            x -= 0.000001
    while True:
        if n - 2 ** x < 0.0000001:
            return x
        x += 0.000001


print(f"Logarithm with 2 base {1/8} is {log_base_two(1/8)}")
print(f"Logarithm with 2 base {8} is {log_base_two(8)}")
print(f"Logarithm with 2 base {3} is {log_base_two(3)}")

def log_2(n):
    x = 0
    while True:
        if 2 ** x - n > 0.001:
            return x
        x += 0.001

print(log_2(3))
