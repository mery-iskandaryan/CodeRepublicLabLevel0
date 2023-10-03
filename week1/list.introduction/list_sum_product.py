ls = [7,8,9,5,4,10,23,1]
sum = 0
product = 1

for i in ls:
    sum += i
    product *= i

print("The sum of the elements of list is {}.\nThe product of the elements of the list is {}.".format(sum, product))
