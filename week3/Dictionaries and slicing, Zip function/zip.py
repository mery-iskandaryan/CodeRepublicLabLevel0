def zipp(*iterables):
    min_len = min([len(i) for i in iterables])
    ls_tuples = []
    for el in range(min_len):
        ls_tuples.append(tuple(lst[el] for lst in iterables))
    return ls_tuples


def zip_(*iterables):
    min_len = min([len(i) for i in iterables])
    ls_tuples = [tuple(lst[el] for lst in iterables)for el in range(min_len)]
    return ls_tuples


a = zip_([1,2,3], ['a', 'b', 'c'])
#print(a)


