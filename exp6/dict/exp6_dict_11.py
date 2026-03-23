d1, d2 = {'a': 2, 'b': 3}, {'a': 1, 'b': 4}
combined = dict(d1)
for k, v in d2.items():
    combined[k] = combined.get(k, 0) + v