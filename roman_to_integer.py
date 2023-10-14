def romanToInt(st):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for s in range(len(st)):
        if s < len(st) - 1 and d[st[s]] < d[st[s+1]]:
            res -= d[st[s]]
        else:
            res += d[st[s]]
    return res


print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))
