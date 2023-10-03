def contain(str, substr):
    sub_len = len(substr)
    for i in range(len(str)):
        if str[i:i+sub_len] == substr:
            return True
    return False


print(contain('Hello', 'l'))
print(contain('Hello', 'llo'))
print(contain('Hello', 'hem'))
