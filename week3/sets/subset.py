def subset(set1, set2):
    if len(set1) > len(set2):
        return True if set1.symmetric_difference(set2) == set1 - set2 else False
    else:
        return True if set1.symmetric_difference(set2) == set2 - set1 else False


set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4, 5, 6}

print(subset(set1, set2))
