def lengthOfLongestSubstring(s):
    char_index = {}
    start = 0
    max_length = 0

    for i in range(len(s)):
        if s[i] in char_index and char_index[s[i]] >= start:
            start = char_index[s[i]] + 1
        char_index[s[i]] = i
        max_length = max(max_length, i - start + 1)
    return max_length


s = "dvdf"
print(lengthOfLongestSubstring(s))

