# Program to count character frequency without using count()

string = input("Enter a string: ")
freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("\nCharacter Frequency:")
for ch, count in freq.items():
    print(f"'{ch}' : {count}")
