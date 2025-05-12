def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even ✅")
    else:
        print(f"{num} is Odd ❌")

# Example usage
number = int(input("Enter a number to check if it's even or odd: "))
check_even_odd(number)

