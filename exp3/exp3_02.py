# Function to calculate a raised to the power b
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result


# Main program
a = int(input("Enter base (a): "))
b = int(input("Enter power (b): "))

print(a, "raised to the power", b, "is", power(a, b))
