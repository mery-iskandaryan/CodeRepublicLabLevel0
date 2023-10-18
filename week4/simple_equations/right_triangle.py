def is_right_triangle(a,b,c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    return False


print(is_right_triangle(4, 5, 8))
print(is_right_triangle(3, 5, 4))
print(is_right_triangle(10, 8, 6))

