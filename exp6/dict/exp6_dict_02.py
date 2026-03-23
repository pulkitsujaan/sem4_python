s = "hello"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1