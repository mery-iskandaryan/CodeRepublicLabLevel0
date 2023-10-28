def is_palindrome(n):
    return str(n) == str(n)[::-1]


max_palindrome = 1
for num in range(999, 99, -1):
    for n in range(999,99, -1):
        if is_palindrome(num * n) and n * num > max_palindrome:
            max_palindrome = n * num

print(max_palindrome)

