# a << b  <=>  a * 2**b
# a >> b  <=>  a // 2**b

def count_ones(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

#print(count_ones(5))



