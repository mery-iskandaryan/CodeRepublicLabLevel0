def print_list_elements(ls):
    if len(ls) == 0:
        return
    else:
        print(ls[0])
        print_list_elements(ls[1:])

print_list_elements([1,2,3,4,5,6])


