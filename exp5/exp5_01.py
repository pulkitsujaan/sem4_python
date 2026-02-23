s = input("Enter string: ")

# Palindrome
is_palindrome = s == s[::-1]

# Symmetrical
mid = len(s)//2
if len(s) % 2 == 0:
    is_symmetrical = s[:mid] == s[mid:]
else:
    is_symmetrical = s[:mid] == s[mid+1:]

print("Palindrome:", is_palindrome)
print("Symmetrical:", is_symmetrical)