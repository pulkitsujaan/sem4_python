def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

lst = [2, 3, 4, 5, 6, 7]
s = set(lst)
s = {x for x in s if not is_prime(x)}