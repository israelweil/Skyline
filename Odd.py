# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
num = 42
result = check_even_odd(num)
print(f"The number {num} is {result}.")
