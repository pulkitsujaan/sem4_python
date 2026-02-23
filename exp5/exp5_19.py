def word_pattern(pattern, s):
    words = s.split()
    return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))

print(word_pattern("abba", "dog cat cat dog"))