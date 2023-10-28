def sum_of_squares(n):
    sum_of_sq = 0
    for i in range(n+1):
        sum_of_sq += i**2
    return sum_of_sq


def square_of_sum(n):
    square_of_sum = 0
    for i in range(n+1):
        square_of_sum += i
    square_of_sum = square_of_sum **2
    return square_of_sum


print(square_of_sum(100) - sum_of_squares(100))
