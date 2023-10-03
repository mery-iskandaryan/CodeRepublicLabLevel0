def zero_to_n(num):
    if num < 0:
        return
    zero_to_n(num-1)
    print(num)


zero_to_n(5)
