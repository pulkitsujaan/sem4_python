# Function to count digits
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

# Function to calculate sum of digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Function to reverse digits
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
    return rev


# Main program
number = int(input("Enter a number: "))

digits = count_digits(number)
digit_sum = sum_of_digits(number)
reversed_num = reverse_number(number)

print("\n--- Result ---")
print("Count of digits:", digits)
print("Sum of digits:", digit_sum)
print("Reverse of number:", reversed_num)
