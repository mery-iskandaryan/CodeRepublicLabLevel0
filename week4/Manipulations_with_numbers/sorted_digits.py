n = int(input("Enter a number: "))
ls = []
while True:
    if n == 0:
        break
    ls.append(n % 10)
    n //= 10

ls = ls[::-1]
for i in range(len(ls) - 1):
    if ls[i] > ls[i+1]:
        print("NO")
        break
else:
    print("YES")


def sorted_digits(number):
    # Convert the number to a string to easily access its digits
    num_str = str(number)

    # Iterate through the digits and check if they are in ascending order
    for i in range(1, len(num_str)):
        if num_str[i] < num_str[i - 1]:
            return False

    # If we didn't find any out-of-order digits, return True
    return True
