import math

def calculate_area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

# Example usage:
radius = float(input("Enter the radius of the circle: "))
area = calculate_area_of_circle(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
