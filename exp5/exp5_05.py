def words_greater_than_k(sentence, k):
    words = sentence.split()
    return [w for w in words if len(w) > k]

print(words_greater_than_k("Python is very powerful language", 4))