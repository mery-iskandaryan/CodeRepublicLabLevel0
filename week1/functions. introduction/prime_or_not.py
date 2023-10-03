def is_prime(num):
    counter = 0
    if num <= 1:
        return "Enter a number above 1 please."
    else:
        for i in range(2, num+1):
            if num % i == 0:
                counter += 1
        if counter > 1:
            return False
        else:
            return True

print(is_prime(2))
