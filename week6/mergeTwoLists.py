def mergeTwoLists(list1, list2):
    ls = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                ls.append(list1[i], list2[j])



list1 = [1,2,4]
list2 = [1,3,4]
