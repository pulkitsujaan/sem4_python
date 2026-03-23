def longest_word(words):
    return max(words, key=len) if words else ""