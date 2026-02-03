# Recursive function to find sum of digits until a single digit
def single_digit_sum(num):
    if num < 10:
        return num
    else:
        return single_digit_sum(sum_of_digits(num))

# Helper recursive function to calculate sum of digits once
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits(num // 10)


# Main program
number = int(input("Enter a number: "))
result = single_digit_sum(number)

print("Single digit sum:", result)
