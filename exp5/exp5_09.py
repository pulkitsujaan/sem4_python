import string

s = input("Enter string: ").lower()
alphabet_set = set(string.ascii_lowercase)

print("Contains all alphabets:", alphabet_set <= set(s))