def splitt(string, delimiter=' '):
    ls = []
    temp_str = ''
    for i in range(len(string)):
        if string[i] != delimiter:
            temp_str += string[i]
            if i == len(string) - 1:
                ls.append(temp_str)
        else:
            ls.append(temp_str)
            temp_str = ''
    if not ls:
        return [string]
    return ls



ls = 'hello, my name is Mary, nice to meet you.'
lst = splitt(ls,',')
print(lst)
