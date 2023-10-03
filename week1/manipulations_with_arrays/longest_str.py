ls = ['hi', 'bye', 'hello', 'au-revoir', 'bonsoir', 'hi', 'bye', 'bye']

longest_str = ls[0]
longest_str_index = 0
for i in range(len(ls)):
    if len(ls[i]) > len(ls[longest_str_index]):
        longest_str = ls[i]
        longest_str_index = i

print("{}: {}".format(longest_str_index, longest_str))
