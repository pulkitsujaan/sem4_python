# Program to print pairs (i, j) using nested loops

n = int(input("Enter value of n: "))

print("\nValid pairs (i, j):")

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i * j) % 2 == 0 and (i + j) % 3 == 0:
            print(f"({i}, {j})")
