def print_digit(string):
    ls = []
    for word in string:
        if word.isdigit():
            ls.append(word)
    return ls



print(print_digit('hello 854b'))
