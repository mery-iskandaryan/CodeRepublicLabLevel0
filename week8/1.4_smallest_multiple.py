def smallest_multiple(n):
    for num in range(2520, 500000000):
        if all(num % i == 0 for i in range(1, n+1)):
            return num


print(smallest_multiple(20))
