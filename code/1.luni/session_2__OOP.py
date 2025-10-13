# în Python totul este obiect!


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Excercițiu:
# faceți Point în context string să arate ca o tuplă.
# exemplu:
# >>> "un punct la coordonatele {}".format(Point(5, 10))
# 'un punct la coordonatele (5, 10)'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str(self.as_tuple())
    
    def as_tuple(self):
        return (self.x, self.y)


# Excercițiu:
# adaugați o metodă `translate()` ce mută punctul
# cu delta x, respectiv y

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str(self.as_tuple())
    
    def as_tuple(self):
        return (self.x, self.y)

    def translate(self, x=0, y=0):
        self.x += x
        self.y += y


# Excercițiu:
# adaugați o metodă `get_distance_from_origin()`

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str(self.as_tuple())
    
    def as_tuple(self):
        return (self.x, self.y)

    def translate(self, x=0, y=0):
        self.x += x
        self.y += y

    def get_distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    

p = Point(5, 10)


# Excercițiu:
# implementați suport pentru operatorii de comparație
# (metodele __eq__, __lt__, __gt__)
# (fără __ne__, __le__, __ge__)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str(self.as_tuple())
    
    def as_tuple(self):
        return (self.x, self.y)

    def translate(self, x=0, y=0):
        self.x += x
        self.y += y

    def get_distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()
    

# Exercițiu:
# transformați `get_distance_from_origin()` din metodă
# într-un atribut numit `distance_from_origin`

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
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
        return self.as_tuple() == other.as_tuple()
    


# Exercițiu:
# implementați înmulțire și împărțire.
# (metodele `__mul__` și `__truediv__`)

class Point(Point):
    # !! extindem clasa de mai sus
    # !! pentru că dezvoltare incrementală
    # !! și nu vrem să dăm copy-paste repetat

    def __mul__(self, num):
        return Point(self.x * num, self.y * num)
    
    def __truediv__(self, num):
        return Point(self.x / num, self.y / num)
    

# Exercițiu:
# implementați scăderea dintre două puncte.
# (metoda __sub__)
#
# aceasta va returna un obiect nou de tip `Vector`,
# cu semnătura `Vector(length, angle)`
#
# unghiul se calculează cu
# math.atan(cateta_opusa / cateta_alaturata)

class Vector:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def __repr__(self):
        return f"Vector(length={self.length}, angle={self.angle})"


class Point(Point):
    def __sub__(self, other):
        # "substraction" creates a new right triangle
        _y = other.y - self.y
        _x = other.x - self.x

        distance = math.sqrt(_y**2 + _x**2)

        angle = math.atan2(-_y, -_x)

        return Vector(length=distance, angle=math.degrees(angle))

