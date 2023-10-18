n = int(input("Enter a positive integer: "))

sum = 0
while True:
    if n == 0:
        break
    sum += n % 10
    n //= 10

if sum > 20:
    print("YES")
else:
    print("NO")
