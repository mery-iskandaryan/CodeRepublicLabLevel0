def insertion_sort(lst):
    for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
            print(lst)
    return lst


ls = [15, 2, 4, 6, 9, 1, 5, 3, 11, 10, 8, 7]
# print(insertion_sort(ls))

ls = [2,8,5,3,9,1]
print(insertion_sort(ls))
