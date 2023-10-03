def primes_to_n(n):
    primes = [i for i in range(2, n+1) if all(i % j for j in range(2, int(i**0.5)+1))]
    return primes


print(primes_to_n(15))


