words = ["apple", "bat", "ant", "bear", "cat"]
grouped = {}
for word in words:
    grouped.setdefault(word[0], []).append(word)