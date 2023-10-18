def isValid(s: str):
    st = []
    for char in s:
        if char == '[' or char == '{' or char == '(':
            st.append(char)
        else:
            if not st or (st[-1] == '(' and char != ')') or (st[-1] == '{' and char != '}') or (st[-1] == '[' and char != ']'):
                return False
            st.pop()
    return not st


print(isValid("()[]{}"))
print(isValid("(]"))


