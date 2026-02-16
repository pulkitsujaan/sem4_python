def is_divisible_by_3(n):
    n = abs(n)  # Handle negative numbers
    
    # Base cases
    if n == 0:
        return True
    if n < 3:
        return False
    
    return reduce_number(n)


def reduce_number(n):
    # Sum of digits
    digit_sum = sum(int(d) for d in str(n))
    
    # Indirect recursive call
    return is_divisible_by_3(digit_sum)


# Example usage
print(is_divisible_by_3(9))     # True
print(is_divisible_by_3(14))    # False
print(is_divisible_by_3(123))   # True
