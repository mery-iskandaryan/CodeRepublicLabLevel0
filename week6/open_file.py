def replace_a_b(text, a, b):
    with open(text, 'r') as file, open('replaced.txt', 'w') as new_file:
        t = file.read()
        for line in t:
            new_line = line.replace(a, b)
            new_file.write(new_line)


replace_a_b('a.txt', 'l', 'm')

