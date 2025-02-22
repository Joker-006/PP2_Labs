import math

# Input values
n = int(input("Input number of sides: "))  # Number of sides
s = float(input("Input the length of a side: "))  # Length of a side

# Calculate the area of the regular polygon
area = (n * s**2) / (4 * math.tan(math.pi / n))

# Output the result
print(f"The area of the polygon is: {area}")