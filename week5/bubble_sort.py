def bubble_sort(ls):
    for i in range(len(ls)):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls


ls = [15, 2, 4, 6, 9, 1, 5, 3, 11, 10, 8, 7]
lst = [1, 2, 3, 4, 5]
print(bubble_sort(ls))
print(bubble_sort(lst))
