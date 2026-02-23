s = input("Enter string: ")
result = ""
prev_space = False

for ch in s:
    if ch == " ":
        if not prev_space:
            result += ch
        prev_space = True
    else:
        result += ch
        prev_space = False

print(result)