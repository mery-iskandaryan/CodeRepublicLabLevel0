def square_equations(a, b, c):
    if a == 0:
        return "a should be above 0."
    discriminant = b**2 - (4*a*c)
    if discriminant < 0:
        return "This equation has no roots"
    elif discriminant == 0:
        return (-b + discriminant**0.5) / (2*a)
    else:
        return (-b + discriminant**0.5) / (2*a), (-b - discriminant**0.5) / (2*a)


print(square_equations(2, 3, 1))
print(square_equations(0, 3, 1))
print(square_equations(1, 6, 9))
