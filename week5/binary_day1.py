def count_ones(number):
    count = 0

    while number > 0:
        count += number & 1
        number >>= 1
    return count

def is_even_ones(number):
    count = 0
    while number > 0:
        count += number & 1 
        number >>= 1 
    return count % 2 == 0

def set_bit_1(n, i):
    change_bit = 1 << i

    result = n | change_bit
    return result

def set_bit_0(n, i):
   change_bit = ~(1 << i)
   result = n & change_bit
   return result

def flip_bit(n, i):
    changed = 1 << i
    result = n ^ changed
    return result


print(f"Result of problem1 with n=5 is: {count_ones(5)}")
print(f"Result of problem2 with n=5 is: {is_even_ones(5)}")
print(f"Result of problem3 with n=5 and i=1 is: {set_bit_1(5, 1)}")
print(f"Result of problem4 with n=5 and i=1 is: {set_bit_0(8, 3)}")
print(f"Result of problem5 with n=5 and i=1 is: {flip_bit(6, 1)}")