num = 600851475143


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


max_prime = 1
ls = []
for n in range(2, 30000):
    if is_prime(n) and num % n == 0 and n > max_prime:
        print(n)

