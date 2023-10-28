num1 = 1
num2 = 2
res = 0
even_sum = 2


while res <= 4000000:
    res = num1+num2
    if res % 2 == 0:
        even_sum += res
    num1, num2 = num2, res

print(even_sum)
