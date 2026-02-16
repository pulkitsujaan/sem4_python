def remove_vowels(text):
    # Base case
    if len(text) == 0:
        return ""
    
    first = text[0]
    
    if first.lower() in "aeiou":
        return remove_vowels(text[1:])
    else:
        return first + remove_vowels(text[1:])


# Example usage
print(remove_vowels("Hello World"))   # Output: Hll Wrld
print(remove_vowels("Python"))        # Output: Pythn
print(remove_vowels("AEIOUxyz"))      # Output: xyz
