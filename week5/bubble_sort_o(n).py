def bubble_sort(lst):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = True
        print(lst)
    return lst


lst = [1,2,0,4,3,5,6,7,8]
print(bubble_sort(lst))
