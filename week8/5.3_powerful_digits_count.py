num = 1
count = 0
i = 1

while True:
    for num in range(1, 10):
        if len(str(num**i)) == i:
            count += 1
    i += 1
    if i == 25:
        break

print(count)

