def perfect_number(num):
    if sum([i for i in range(1, num) if num % i == 0]) == num:
        return True
    return False


print(perfect_number(21))

