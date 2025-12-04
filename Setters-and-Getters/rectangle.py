class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width} cm"
    
    @property
    def height(self):   
        return f"{self._height} cm"
    
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print(f"Width cannot be less than 0")
        
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print(f"Height cannot be less than 0")
        
rectangle = Rectangle(4,5)

rectangle.width = 6
rectangle.height = 2

print(rectangle.width)
print(rectangle.height)