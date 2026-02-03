# Program to convert decimal to binary using bitwise operators

num = int(input("Enter a decimal number: "))

if num == 0:
    print("Binary: 0")
else:
    binary = ""

    while num > 0:
        bit = num & 1          # get last bit
        binary = str(bit) + binary
        num = num >> 1         # right shift

    print("Binary:", binary)
