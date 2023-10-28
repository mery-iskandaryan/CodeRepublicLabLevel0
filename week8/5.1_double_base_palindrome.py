def decimal_to_binary(n):
    binary = ''
    while n > 0:
        binary += str(n % 2)
        n //= 2
    return binary


def is_palindorme(s):
    return str(s) == str(s)[::-1]


ls = []
for i in range(1000000):
    if is_palindorme(i) and is_palindorme(decimal_to_binary(i)):
        ls.append(i)

print(sum(ls))
