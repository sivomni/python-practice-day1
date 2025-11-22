# advanced_practice.py

# Check if a number is even or odd
def check_even_odd(number): #Defines function that takes a number parameter
    return "Even" if number % 2 == 0 else "Odd" #Uses ternary operator - if number divided by 2 has remainder 0, return "Even", else "Odd"

# Reverse a string
def reverse_string(text): # Function takes a text string parameter
    return text[::-1] # String slicing - [::-1] means "start to end, but step backwards by 1"

# Find the largest of three numbers
def find_largest(a, b, c): # Takes three number parameters
    return max(a, b, c) # Uses built-in max() function to find largest value

# Simple password checker
def check_password(password): # Takes a password string
    return len(password) >= 8 and any(char.isdigit() for char in password) 
# len(password) >= 8 - length at least 8 characters
# any(char.isdigit() for char in password) - checks if ANY character is a digit
# and - both must be True

# Calculate factorial
def factorial(n): # Takes integer n
    if n == 0:
        return 1 # Base case - 0! = 1 by definition
    return n * factorial(n-1) #  Recursion - n! = n × (n-1)! (function calls itself)

# Count vowels in a string
def count_vowels(text): # Takes a text string
    vowels = "aeiouAEIOU" # Defines what characters count as vowels (both cases)
    return sum(1 for char in text if char in vowels) # counts 1 for each character that's a vowel, then sums them

# Simple interest calculator
def simple_interest(principal, rate, time): # Takes three parameters: initial amount, interest rate, time period
    return principal * rate * time / 100 # Applies simple interest formula: (P × R × T) ÷ 100

# Check if a number is prime
def is_prime(number): # Takes a number to check
    if number < 2: 
        return False # Numbers less than 2 are not prime
    for i in range(2, int(number**0.5) + 1): # only check divisors up to √number
        if number % i == 0: 
            return False # If any divisor found, not prime
    return True # If no divisors found, it's prime

# Convert seconds to hours, minutes, seconds
def convert_seconds(total_seconds): # Takes total seconds
    hours = total_seconds // 3600 # Integer division - calculates whole hours
    minutes = (total_seconds % 3600) // 60 # Gets remaining seconds after hours, then calculates minutes
    seconds = total_seconds % 60 # Gets remaining seconds after minutes
    return hours, minutes, seconds # Returns three values as a tuple

# Find common elements between two lists
def find_common_elements(list1, list2): # Takes two lists
    return list(set(list1) & set(list2))
# set(list1) - converts list to set (removes duplicates)
# & - set intersection (finds common elements)
# list() - converts back to list

# Test the functions
print(f"1. 15 is {check_even_odd(15)}")
print(f"2. 'hello' reversed is '{reverse_string('hello')}'")
print(f"3. Largest of (4, 7, 2) is {find_largest(4, 7, 2)}")
print(f"4. Password 'abc123' is valid: {check_password('abc123')}")
print(f"5. Factorial of 5 is {factorial(5)}")
# Add to your existing test section:
print(f"6. Vowels in 'hello world': {count_vowels('hello world')}")
print(f"7. Simple interest: ${simple_interest(1000, 5, 2):.2f}")
print(f"8. Is 17 prime? {is_prime(17)}")
hours, minutes, seconds = convert_seconds(3665)
print(f"9. 3665 seconds = {hours}h {minutes}m {seconds}s")
print(f"10. Common elements: {find_common_elements([1,2,3,4], [3,4,5,6])}")