class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    # Like this; Have to return a new object when using dunder methods
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y    
        )

    # Not like this; You cannot modify the self (object) through a dunder method
        # def __add__(self, other):
        #     self.x += other.x
        #     self.y += other.y

point1 = Point(5,6)
point2 = Point(2,9)

point12 = point1 + point2

print(point12.x, point12.y)