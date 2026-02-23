s = input("Enter string: ")
result = ""

for ch in s:
    if ch == ",":
        result += "."
    elif ch == ".":
        result += ","
    else:
        result += ch

print(result)