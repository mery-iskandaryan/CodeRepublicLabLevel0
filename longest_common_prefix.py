def longestCommonPrefix(strs):
    min_len = min([len(i) for i in strs])
    res = ''
    i = 0

    while i < min_len:
        prefix = strs[0][i]
        if all(word[i] == prefix for word in strs):
                i += 1
                res += prefix
        else:
            break
    return res



strs = ["flower","flow","flight"]
#longestCommonPrefix(strs)
#print(longestCommonPrefix(strs))

strs1 = ["dog","racecar","car"]
print(longestCommonPrefix(strs1))
