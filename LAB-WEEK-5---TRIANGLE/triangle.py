import math

class Triangle:
    _object_count = 0

    def __init__(self, *args):
        if len(args) == 0:
            self._sideA = self._sideB = self.sideC = 1.0
        elif len(args) == 1:
            if isinstance(args[0], Triangle):
                other = args[0]
                self._sideA = other._sideA
                self._sideB = other._sideB
                self._sideC = other._sideC
            else:
                self._sideA = self._sideB = self._sideC = float(args[0])
        elif len(args) == 2:
            self._sideA = self._sideB = float(args[0])
            self._sideC = float(args[1])
        elif len(args) == 3:
            self._sideA = float(args[0])
            self._sideB = float(args[1])
            self._sideC = float(args[2])
        else:
            print(f"Invalid number of sides entered")
        Triangle._object_count += 1
    
    @property 
    def sideA(self):
        return self._sideA
    
    @sideA.setter
    def sideA(self,value):
        if value>0:
            self._sideA = float(value)
        else:
            print("SideA must be positive")

    @property
    def sideB(self):
        return self._sideB
    
    @sideB.setter
    def sideB(self,value):
        if value>0:
            self._sideB = float(value)
        else:
            print("sideB must be positive")

    @property
    def sideC(self):
        return self._sideC
    
    @sideC.setter
    def sideC(self,value):
        if value>0:
            self._sideC = float(value)  
        else:
            print("sideC must be positive")

    @staticmethod
    def objectCount():
        return Triangle._object_count

    def perimeter(self):
        return self._sideA + self._sideB + self._sideC

    def isRightAngled(self):
        sides = sorted([self._sideA, self._sideB, self._sideC])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)

    def __str__(self):
        return f"Triangle with sides: A={self._sideA}, B={self._sideB}, C={self._sideC}"

