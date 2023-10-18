def insertionSort(arr, n):
    if n <= 1:
        return
    insertionSort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1
    # print(last)
    arr[j + 1] = last
    print(arr)

    return arr


ls = [4, 7, 9, 1, 2, 0]
print(insertionSort(ls, len(ls)))
