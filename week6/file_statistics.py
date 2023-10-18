def file_stat(file):
    with open(file, 'r') as text:
        t = text.read()
    lines_count = len(t.splitlines())
    lst = t.split('\n')
    print(lst)
    word_count = 0
    for i in lst:
        word_count += len(i.split(' '))

    chars_count = sum([1 for i in t if i != '\n'])
    res = f'There are {lines_count} lines, {word_count-1} words and {chars_count} characters.'
    return res


print(file_stat('stats.txt'))
