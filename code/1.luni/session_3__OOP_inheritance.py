import math


class Vector:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def __repr__(self):
        return f"Vector(length={self.length}, angle={self.angle})"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{self.__class__.__name__}{self.as_tuple()}"
        
    def __str__(self):
        return str(self.as_tuple())
    
    def as_tuple(self):
        return (self.x, self.y)

    def translate(self, x=0, y=0):
        self.x += x
        self.y += y

    @property
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        #return self.as_tuple() == other.as_tuple()
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

    def __gt__(self, other):
        return self.as_tuple() > other.as_tuple()

    def __mul__(self, num):
        return self.__class__(*[
            elem * num for elem in self.as_tuple()
        ])
    
    def __truediv__(self, num):
        return self.__class__(*[
            elem / num for elem in self.as_tuple()
        ])
    
    def __sub__(self, other):
        # "substraction" creates a new right triangle
        _y = other.y - self.y
        _x = other.x - self.x

        distance = math.sqrt(_y**2 + _x**2)

        angle = math.atan2(-_y, -_x)

        return Vector(length=distance, angle=math.degrees(angle))


# întrebare:
# folosind as_tuple(), cum facem __mul__ și __truediv__ generice?
#
# răspuns:
# 1) self.as_tuple() returnează o tuplă cu nr.-ul corect de elemente;
# 2) creem o listă cu fiecare element înmulțit cu `num`;
# 3) există argument unpacking


class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)

        self.z = z

    def as_tuple(self):
        return super().as_tuple() + (self.z, )
    
    def __eq__(self, other):
        return super().__eq__(other) and self.z == other.z
    
    def __sub__(self, other):
        raise NotImplementedError

ThreeDPoint(1, 2, 3) / 2