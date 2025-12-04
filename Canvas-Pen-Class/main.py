from pen import Pen

# Create a pen at the default position
pen = Pen()

# Move pen to (5, 5)
pen.moveTo(5, 5)
print(pen.getPosition())  # Expected: (5, 5)

# Draw line to (10, 10)
pen.lineTo(10, 10)
print(pen.getPosition())  # Expected: (10, 10)

# Move to a different spot without drawing
pen.moveTo(2, 3)
print(pen.getPosition())  # Expected: (2, 3)

# Draw another line
pen.lineTo(8, 8)
print(pen.getPosition())  # Expected: (8, 8)

