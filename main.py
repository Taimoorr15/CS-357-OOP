from point import Point

# Test script for Point class

# Create points
p1 = Point(3, 4)
p2 = Point(0, 0)
p3 = Point(-2, 5)
p4 = Point(3, 4)  # Same as p1

print("=== Basic __str__() check ===")
print(p1)  # Expect: Point(3, 4)
print(p2)  # Expect: Point(0, 0)

print("\n=== Distance test ===")
print(p1.distance(p2))  # Expect 5.0 (classic 3-4-5 triangle)
print(p2.distance(p3))  # Expect sqrt((0+2)^2 + (0-5)^2) = sqrt(4 + 25) = sqrt(29)
print(p1.distance(p4))  # Expect 0.0 (same point)

print("\n=== Addition test ===")
p5 = p1 + p3
print(p5)  # Expect Point(1, 9)

print("\n=== Subtraction test ===")
p6 = p1 - p3
print(p6)  # Expect Point(5, -1)

print("\n=== Getter & Setter test ===")
print("Before:", p1.x, p1.y)
p1.x = 10
p1.y = 20
print("After:", p1.x, p1.y)

# Testing setting to same value
p1.x = 10  # Shouldn't change internally
p1.y = 20
print("After same value set:", p1.x, p1.y)

print("\n=== Chained operations ===")
p7 = (p1 + p2) - p3
print(p7)  # Expect Point(12, 15)

print("\n=== Type safety check (optional) ===")
try:
    print(p1.distance(42))  # Should error
except AttributeError as e:
    print("Error caught:", e)
