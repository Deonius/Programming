class Point:
    count = 0
    def __init__(self,x,y):
        self.coord =  (x, y)
        Point.count =+ 1
        self.x = x
        self.y = y
        @classmethod
        def abc(cls,qwe):
            return qwe
    def __add__(self, point):
        point.x = self.x + point.x
        point.y = self.y + point.y
        return point
point1=Point(1,2)
point2=Point(2,3)
point3 = point1 + point2
print(point3.x)
print(point3.y)