def joinn(seq, sep):
    new_str = seq[0]
    for i in seq[1:]:
        new_str += sep + i
    return new_str


a = 'hello'
b = ['h', 'e', 'l', 'l', 'o']
print(joinn(a, '#'))

