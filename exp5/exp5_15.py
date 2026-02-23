def split_groups(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

print(split_groups("abcdefgh",3))