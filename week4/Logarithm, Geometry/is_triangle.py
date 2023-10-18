import herons_formula


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True, herons_formula.herons_formula(a, b, c)
    return False


print(is_triangle(23, 41, 46))
print(is_triangle(1, 1, 3))


