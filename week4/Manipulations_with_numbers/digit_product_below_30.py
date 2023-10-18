n = int(input("Enter a positive integer: "))

product = 1
while True:
    if n == 0:
        break
    product *= n % 10
    n //= 10


if product < 30:
    print("YES")
else:
    print("NO")
