set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {6, 7, 8, 9, 10, 11, 12}

set_union = set1.union(set2)
set_union = set1 | set1
set_intersection = set1.intersection(set2)
set_intersection = (set1 & set2)
symmetric_difference = set_union - set_intersection
set1.symmetric_difference(set2)
sym_dif = set1 ^ set2
print(set_union)
print(set_intersection)
print(symmetric_difference)
print(sym_dif)
