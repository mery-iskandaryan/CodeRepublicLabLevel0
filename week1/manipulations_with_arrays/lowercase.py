ls = ['HI', 'BYE', 'heLLo', 'AU-revoir', 'bonSOIR', 'HI', 'Bye', 'BYE']

for i in range(len(ls)):
    ls[i] = ls[i].lower()


for i in ls:
    print(i[::-1])

