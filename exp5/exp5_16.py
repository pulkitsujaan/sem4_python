s1 = input("First string: ")
s2 = input("Second string: ")

i = 0
for ch in s2:
    if i < len(s1) and ch == s1[i]:
        i += 1

print("Appears in order:", i == len(s1))