sentence = "this is a test this is only a test"
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1