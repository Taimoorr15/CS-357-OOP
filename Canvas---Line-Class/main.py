from point import Point
from line import Line

# Create points
p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(-1, -1)
p4 = Point(5, 5)

# Create lines
line1 = Line(p1, p2)  # Expected length: 5.00
line2 = Line(p3, p4)  # Expected length: sqrt(36 + 36) = 8.49
line3 = Line(p1, p1)  # Expected length: 0.00

# Print results
print(line1)  # "The length of the line is 5.00"
print(line2)  # "The length of the line is 8.49"
print(line3)  # "The length of the line is 0.00"

# Direct method calls
print(line1.length())  # 5.0
print(line2.length())  # ~8.485
print(line3.length())  # 0.0
