import string

s = input("Enter string: ")
special = string.punctuation

found = False
for ch in s:
    if ch in special:
        found = True
        break

print("Contains special character:", found)