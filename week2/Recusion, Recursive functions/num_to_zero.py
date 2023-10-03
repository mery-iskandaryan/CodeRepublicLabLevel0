def num_to_zero(num):
    if num < 0:
        return
    print(num)
    num_to_zero(num-1)


num_to_zero(5)
