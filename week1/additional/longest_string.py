def longest_string(string):
    st_new = ''
    for letter in string:
        if letter not in '!()-[]{};:\,<>./?@#$%^&*_~':
            st_new += letter

    ls = st_new.split(' ')
    longest_word = ls[0]
    for word in ls:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(longest_string('HEllo looongest word;;;;*******'))

