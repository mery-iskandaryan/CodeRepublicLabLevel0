def is_prime(n):
    return all(n % i != 0 for i in range(2, n))

def rotation(n):
    s = set()
    for i in range(len(str(n))):
        m = int(str(n)[i:] + str(n)[:i])
        s.add(m)
    return s

count = 0
for i in range(2,1000000):
    if is_prime(i) and all(is_prime(num) for num in rotation(i)):
        count += 1

print(count)
