def swap_bits(number, i, j):
    swapped_i = (number >> i) & 1
    swapped_j = (number >> j) & 1

    if swapped_i != swapped_j:
        number ^= (1 << i)
        number ^= (1 << j)

    return number

def number_binary(number):
    if number == 0:
        return '0'
    
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    
    return binary

def reverse_bits(number):
    return number_binary(number)[::-1]

def pow_of_2(number):
    return number & (number - 1) == 0 and number != 0

def find_single_element(nums):
    result = 0
    for num in nums:
        result ^= num

    return result

print(f"Swapped bits: {swap_bits(8, 0, 3)}")
print(f"Number binary:  {number_binary(10)}")
print(f"Pow og two: {pow_of_2(16)}")
print(f"Reverse bits: {reverse_bits(10)}")
print(f"Find Single Element: {find_single_element([1, 3, 3, 2, 5, 2, 1])}")



