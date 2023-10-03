def binary_search(target, lst, start, end):
    if start <= end:
        mid = (start + end)//2
        if lst[mid] == target:
            return mid
        elif target > lst[mid]:
            return binary_search(target, lst, mid + 1, end)
        else:
            return binary_search(target, lst, start, mid - 1)
    else:
        return 'The element is not present in the list.'


lst = [1, 2, 3, 4, 5, 8, 16]

print(binary_search(16, lst, 0, len(lst)))


