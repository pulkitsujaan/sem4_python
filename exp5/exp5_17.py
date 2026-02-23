s = input("Enter snake_case string: ")
words = s.split("_")
result = "".join(word.capitalize() for word in words)
print(result)