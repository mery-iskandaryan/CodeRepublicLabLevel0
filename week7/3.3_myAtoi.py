def myAtoi(s: str) -> int:
        s = s.lstrip()
        sign = 1
        i = 0
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res = max(min(res * sign, 2**31 - 1), -2**31)
        return res


s = "   -42"
s = "4193 with words"
print(myAtoi(s))
