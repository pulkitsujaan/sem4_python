def get_primes(lst):
    return list(filter(
        lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)),
        lst
    ))


# Example usage
numbers = [2, 3, 4, 5, 10, 13, 17, 20]
prime_numbers = get_primes(numbers)

print(prime_numbers)

# Output: [2, 3, 5, 13, 17]