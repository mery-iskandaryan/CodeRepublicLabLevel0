def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return all(s.count(let) == t.count(let) for let in t)


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
