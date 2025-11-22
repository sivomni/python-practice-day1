# This is a Comment Python ignores anything after #
# basics.py {File Name}

# ✔ Print your name
# print() is a function that displays text on the screen. It outputs whatever is inside the parentheses.
print("My name is: Sivomnii")

# ✔ Create variables of different types
my_int = 10 #Creates a variable named my_int and assigns it the integer value 10
my_float = 3.14 #Creates a variable named my_float and assigns it the floating-point (decimal) value 3.14
my_string = "Hello, World!" #Creates a variable named my_string and assigns it the string (text) value "Hello, World!"
my_bool = True #Creates a variable named my_bool and assigns it the boolean (true/false) value True.

# These are f-strings (formatted string). The f before the quotes allows you to insert variables inside {}
print(f"Integer: {my_int}") # will output: Integer: 10
print(f"Float: {my_float}") # will output: Float: 3.14
print(f"String: {my_string}") # will output: String: Hello, World!
print(f"Boolean: {my_bool}") # will output: Boolean: True

# ✔ Practice Problems

# 1. Add two numbers
num1 = 5 # Creates variable num1 with value 5.
num2 = 3 # Creates variable num2 with value 3.
sum_result = num1 + num2 # Adds num1 + num2 and stores the result (8) in a new variable sum_result.
print(f"\n1. {num1} + {num2} = {sum_result}") #\n creates a new line. Outputs: 1. 5 + 3 = 8

# 2. Convert Celsius to Fahrenheit
celsius = 25 # Creates variable celsius with value 25.
fahrenheit = (celsius * 9/5) + 32 # Uses the formula to convert Celsius to Fahrenheit:
print(f"2. {celsius}°C = {fahrenheit}°F") # Outputs: 2. 25°C = 77.0°F

# 3. String concatenation
first_name = "John" # Creates string variable first_name with value "John".
last_name = "Doe" # Creates string variable last_name with value "Doe".
full_name = first_name + " " + last_name # Concatenates/Merges two strings. Result: "John Doe" stored in full_name 
print(f"3. Full name: {full_name}") # 3. Full name: John Doe

# 4. Boolean test (5 > 3)
is_greater = 5 > 3 # Compares if 5 is greater than 3 (which is True) and stores the result in is_greater.
print(f"4. Is 5 greater than 3? {is_greater}") # Outputs: 4. Is 5 greater than 3? True

# 5. Calculate area of a circle
import math # Imports the math module, which gives you access to mathematical functions and constants like pi.
radius = 7 # Creates variable radius with value 7.
area = math.pi * radius ** 2 # Calculates circle area using formula π × r²:
print(f"5. Area of circle with radius {radius}: {area:.2f}") # :.2f formats the number to 2 decimal places. Outputs: 5. Area of circle with radius 7: 153.94