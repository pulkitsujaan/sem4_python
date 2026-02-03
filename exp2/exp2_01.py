# experiment 2 - 2/02/26

import math

def is_prime(n):
    """
    Checks if a single number n is a prime number.
    """
    if n <= 1:
        return False
   
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False # Not a prime number
    return True # Prime number if no divisors found

def find_primes_in_range(start, end):
    """
    Finds all prime numbers within a specified range [start, end].
    """
    primes = []
    # Iterate through each number in the range
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage:
lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))
prime_numbers = find_primes_in_range(lower_bound, upper_bound)
print(f"Prime numbers between {lower_bound} and {upper_bound} are: {prime_numbers}")
