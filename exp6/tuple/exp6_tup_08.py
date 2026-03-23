tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
merged = tuple(dict.fromkeys(tup1 + tup2)) # dictionary preserves order better than set