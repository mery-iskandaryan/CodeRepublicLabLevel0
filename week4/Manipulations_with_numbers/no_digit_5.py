n = int(input("Enter a a positive integer: "))
while True:
    if n % 10 == 5:
        print("NO")
        break
    elif n == 0:
        print("YES")
        break
    n = n // 10



