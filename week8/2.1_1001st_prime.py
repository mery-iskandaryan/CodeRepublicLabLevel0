def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


count = 0
num = 2
while count < 10001:
    if is_prime(num):
        count +=1
    num += 1

print(num-1)
