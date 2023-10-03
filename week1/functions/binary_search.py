def binary_search(ls, target):
    start = 0
    end = len(ls)-1
    mid = (start + end)//2

    while start <= end:
        mid = (start + end)//2
        if ls[mid] == target:
            return mid
        elif target > ls[mid]:
            start = mid + 1
        elif target < ls[mid]:
            end = mid - 1
    return -1

print(binary_search([1,2,3,4,5,6,7],6))


