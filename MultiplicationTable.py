number = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table of {number}")
for i in range(1, 13):  # prints from 1 to 12
    print(f"{number} x {i} = {number * i}")