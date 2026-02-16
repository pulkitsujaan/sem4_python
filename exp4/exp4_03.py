def reverse_strings(string_list):
    return list(map(lambda s: s[::-1], string_list))


# Example usage
words = ["hello", "python", "world", "code"]
reversed_words = reverse_strings(words)

print(reversed_words)

'''

OUTPUT:
['olleh', 'nohtyp', 'dlrow', 'edoc']

'''