# Function to find LCM of two numbers
def lcm(a, b):
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


# Main program
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("LCM of", x, "and", y, "is:", lcm(x, y))
