s = input("Enter string: ")
sub = input("Enter substring: ")

index = -1
for i in range(len(s)-len(sub)+1):
    if s[i:i+len(sub)] == sub:
        index = i
        break

print("Index:", index)