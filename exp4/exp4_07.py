def count_vowels(text):
    # Base case
    if len(text) == 0:
        return 0
    
    # Check first character
    first = text[0].lower()
    if first in "aeiou":
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])


# Example usage
print(count_vowels("Hello World"))      # Output: 3
print(count_vowels("Python"))           # Output: 1
print(count_vowels("AEIOU"))            # Output: 5
