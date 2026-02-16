def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Indirect recursive call
    return n * fact_helper(n - 1)


def fact_helper(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Calls the first function again
    return n * factorial(n - 1)


# Example usage
print(factorial(5))   # 120
print(factorial(0))   # 1
