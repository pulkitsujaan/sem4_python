# Program to find inverse of a 2x2 matrix without using numpy

print("Enter elements of 2x2 matrix:")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

# Determinant
det = a * d - b * c

if det == 0:
    print("Inverse does not exist (Determinant is zero).")
else:
    print("\nInverse of the matrix:")
    print(f"{d/det:.2f}  {-b/det:.2f}")
    print(f"{-c/det:.2f}  {a/det:.2f}")
