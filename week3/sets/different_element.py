arr1 = [1,2,3,4,5,6,9,0]
arr2 = [1,2,3,9,4,5,6]
'''
if len(arr1) > len(arr2):
    print(set(arr1) - set(arr2))
else:
    print(set(arr2) - set(arr1))
'''

print(set(arr1) - set(arr2) if len(arr1) > len(arr2) else set(arr2) - set(arr1))
