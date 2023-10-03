def fibonacci(n):
    if n in [1, 2]:
        return n - 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))


# fib(5) = fib(4)//2 + fib(3)//1
# fib(4) = fib(3)//1 + fib(2)//1
# fib(3) = fib(2) + fib(1)   1 + 0 = 1

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
