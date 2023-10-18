n = int(input("Enter a number: "))
ls = []
while True:
    if n == 0:
        break
    ls.append(n % 10)
    n //= 10

ls = ls[::-1]


for i in range(len(ls)-1):
    if ls[i] < ls[i+1]:
        print("YES")
        break
else:
    print("NO")

