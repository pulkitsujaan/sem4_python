def power(a, n):
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return a * power(a, n - 1)


# Example usage
print(power(2, 3))   # Output: 8
print(power(5, 0))   # Output: 1
print(power(3, 4))   # Output: 81
