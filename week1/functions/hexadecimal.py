def hexadecimal(num):
    hex = ''
    while num > 0:
        digit = str(num % 16)
        dic = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
        for key in dic:
            if digit == key:
                digit = dic[key]
        hex += digit
        num = num // 16
    return hex[::-1]

print(hexadecimal(8284))
