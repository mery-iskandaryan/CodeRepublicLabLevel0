def polyndrome(num):
    if num == num[::-1]:
        return 0
    else:
        sum = int(num) + (int(num[::-1]))
        sum = str(sum)
        counter = 1
        while sum != sum[::-1]:
            num = str(sum)
            sum = int(num) + int(num[::-1])
            sum = str(sum)
            counter += 1

        return counter


num = input("Enter a number: ")
print(polyndrome(num))
