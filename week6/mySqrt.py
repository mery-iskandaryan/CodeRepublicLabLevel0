def mySqrt(x: int) -> int:
    i = 0
    while i*i <= x:
        i +=1
    return i-1


print(mySqrt(0))
print(mySqrt(10))
print(mySqrt(19))
