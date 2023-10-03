from prime_or_not import *

def prime_sum(num):
    for i in range(2, num//2):
        if (is_prime(i) & is_prime(num-i)):
            return i, num-i
    return 0

print(prime_sum(27))



