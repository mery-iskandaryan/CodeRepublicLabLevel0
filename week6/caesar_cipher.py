def caesar_cipher(file):
    with open(file, 'r') as f, open('encoded.txt', 'w') as new_file:
        text = f.read()
        res = ''
        shift = 4
        for char in text:
            if char.isalpha():
                if char.isupper():
                    res += chr(((ord(char) + shift - 65) % 26) + 65)
                else:
                    res += chr(((ord(char) + shift - 97) % 26) + 97)
            else:
                res += char
        new_file.write(res)


caesar_cipher('encode_file.txt')
