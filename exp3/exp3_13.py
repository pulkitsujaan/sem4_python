# Given list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Numbers divisible by both 3 and 5
divisible_by_3_and_5 = [x for x in numbers if x % 3 == 0 and x % 5 == 0]

# Squares of only even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]

print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)
print("Squares of even numbers:", even_squares)
