n = int(input("Enter a number: "))
temp = n
size = len(str(n))

summ = 0
while True:
    if temp ==0:
        break
    summ += (temp % 10) ** size
    temp //= 10

if summ == n:
    print("YES")
else:
    print("NO")
