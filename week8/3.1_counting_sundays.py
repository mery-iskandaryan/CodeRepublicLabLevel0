months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 30]
# 07 01 1990 Sunday
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

weekcode = 1
count = 0

for cur_year in range(1900, 2001):
    if leap_year(cur_year):
        months[1] = 29
    for y in months:
        weekcode = (weekcode + y) % 7

        if weekcode == 0 and cur_year > 1900:
            count += 1


print(count)


