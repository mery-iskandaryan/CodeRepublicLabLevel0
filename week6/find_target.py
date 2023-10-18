def find_target(target, file):
    with open(file, 'r') as file:
        text = file.read()
        lst = []
        if target in text:
            tsp = text.splitlines()
            for i in range(len(tsp)):
                if target in tsp[i]:
                    lst.append(i)
        return lst






# return ls if len(ls) > 0 else "The target word is not present in the text."


'''        for line in range(len(lst)):
            for i in range(len(lst[line])):
                print(lst[line][i:len(target)])'''
print(find_target('or', 'target_word.txt'))
