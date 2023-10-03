ls = ['hi', 'bye', 'hello', 'au revoir', 'bonsoir', 'hi', 'bye', 'bye']

ls_dict = dict()
for i in ls:
    ls_dict[i] = ls.count(i)

print(ls_dict)
