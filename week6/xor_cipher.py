def xor_cipher(file):
    with open(file, 'r') as file, open('encoded_xor.txt', 'w') as new_file:
        text = file.read()
        key = 'code_to_encode'
        res = ''
        for i in range(len(text)):
            res += chr(ord(text[i]) ^ ord(key[i % len(key)]))
        new_file.write(res)


xor_cipher('encode_file.txt')
