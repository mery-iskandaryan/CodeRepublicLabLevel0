def partition(array, start, end):
 
    pivot = array[end]

    i = start - 1
 
    for j in range(start, end):
        if array[j] <= pivot:
            i = i + 1

            array[i], array[j] = array[j], array[i]
    
    i += 1
    array[i], array[end] = array[end], array[i]
    return i

 
def quickSort(array, start, end):
    if start < end:

        pi = partition(array, start, end)
        quickSort(array, start, pi - 1)
        quickSort(array, pi + 1, end)
    return array
 
 
data = [5,4,7,2,9,3,56,45,12]
 
size = len(data)
 
print(quickSort(data, 0, size - 1))
