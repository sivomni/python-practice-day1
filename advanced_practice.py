# advanced_practice.py

# Check if a number is even or odd
def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# Reverse a string
def reverse_string(text):
    return text[::-1]

# Find the largest of three numbers
def find_largest(a, b, c):
    return max(a, b, c)

# Simple password checker
def check_password(password):
    return len(password) >= 8 and any(char.isdigit() for char in password)

# Calculate factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Test the functions
print(f"1. 15 is {check_even_odd(15)}")
print(f"2. 'hello' reversed is '{reverse_string('hello')}'")
print(f"3. Largest of (4, 7, 2) is {find_largest(4, 7, 2)}")
print(f"4. Password 'abc123' is valid: {check_password('abc123')}")
print(f"5. Factorial of 5 is {factorial(5)}")