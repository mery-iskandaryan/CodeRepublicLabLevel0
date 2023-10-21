def plusOne(lst):
    res = ''
    for num in lst:
        res += str(num)
    plus_one = str(int(res) + 1)
    return [int(num) for num in plus_one]


print(plusOne([1, 2, 9]))
