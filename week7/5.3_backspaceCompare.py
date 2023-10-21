def backspaceCompare(s, t):
    def backspace(l):
        res = []
        for i in range(len(l)):
            if l[i] != '#':
                res.append(l[i])
            else:
                if len(res) != 0:
                    res.pop()
        return res

    return backspace(s) == backspace(t)


