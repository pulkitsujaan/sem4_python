def sum_first_n_even(n, current=1):
    # Base case
    if n == 0:
        return 0
    
    # Check if current number is even using bitwise operator
    if (current & 1) == 0:   # Even number check
        return current + sum_first_n_even(n - 1, current + 1)
    else:
        return sum_first_n_even(n, current + 1)


# Example usage
print(sum_first_n_even(1))   # 2
print(sum_first_n_even(3))   # 2 + 4 + 6 = 12
print(sum_first_n_even(5))   # 2 + 4 + 6 + 8 + 10 = 30
