# Function to check Armstrong number
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    return total == num


# Main program
n = int(input("Enter a number to check: "))

if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")


# Armstrong numbers between two limits
lower = int(input("\nEnter lower limit: "))
upper = int(input("Enter upper limit: "))

print("\nArmstrong numbers between", lower, "and", upper, ":")
for num in range(lower, upper + 1):
    if is_armstrong(num):
        print(num, end=" ")
