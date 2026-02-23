s = input("Enter string: ")
freq = {}

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        freq[sub] = freq.get(sub,0)+1

max_sub = max(freq, key=freq.get)
print("Max occurring substring:", max_sub)