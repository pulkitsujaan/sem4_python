# Program to check even or odd using bitwise operator

num = int(input("Enter an integer: "))

if num & 1:
    print(num, "is Odd")
else:
    print(num, "is Even")
