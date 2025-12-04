from point import Point
from line import Line
from tkpanel import TkPanel

# Create some points
p1 = Point(2, 3)
p2 = Point(5, 7)

# Create a line
l1 = Line(p1, p2)

# Create a tkpanel instance
panel = TkPanel(height=500, width=800, length=1000, lines=[])

# Test: addline method
result_add = panel.addline(p1, p2)
print("Add Line Result:", result_add)

# Test: delete method
result_delete = panel.delete()
print("Delete Result:", result_delete)

# Test: draw method
result_draw = panel.draw()
print("Draw Result:", result_draw)

# Bonus: Check attributes
print("Panel height:", panel._height)
print("Panel width:", panel._width)
print("Panel length:", panel._length)
