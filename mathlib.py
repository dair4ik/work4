import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = 15
radian = degree_to_radian(degree)
print("Input degree:", degree)
print("Output radian:", round(radian, 6))
#-----------------------------------------
def trapezoid_area(height, base1, base2):
    return ((base1 + base2) / 2) * height

height = 5
base1 = 5
base2 = 6
area = trapezoid_area(height, base1, base2)
print("Expected Output:", area)

#-----------------------------------------
import math

def regular_polygon_area(n, side_length):
    return (n * (side_length ** 2)) / (4 * math.tan(math.pi / n))

num_sides = 4
side_length = 25
area = regular_polygon_area(num_sides, side_length)
print("The area of the polygon is:", round(area, 2))

#-----------------------------------------
def parallelogram_area(base, height):
    return base * height

base = 5
height = 6
area = parallelogram_area(base, height)
print("Expected Output:", area)

#-----------------------------------------