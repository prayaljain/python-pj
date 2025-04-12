print("Wellcome To Prayal's Python\n")
import math

# Function to calculate hypotenuse using Pythagoras Theorem
def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Take input from the user
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))

# Calculate hypotenuse
hypotenuse = calculate_hypotenuse(a, b)

# Display result
print(f"The length of the hypotenuse is: {hypotenuse}")
