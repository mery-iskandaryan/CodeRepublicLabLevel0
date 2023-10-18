def isSubstring(st, substr):
    for i in range(len(st)):
        if st[i] == substr[0]:
            if st[i:i+len(substr)] == substr:
                return i


st = 'hello'
print(isSubstring(st, 'llo'))
