# Function to calculate factorial of a digit
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function to check Strong Number
def is_strong(num):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == num


# Main program
number = int(input("Enter an integer: "))

if is_strong(number):
    print(number, "is a Strong Number")
else:
    print(number, "is not a Strong Number")
