# dodawanie
# odenjmownie
# równość
# mniejsze niż
# mnożenie (przez skalar)
# porównywanie po długości

class Vector():

    def __init__(self,x,y):
        self.pos_x = x
        self.pos_y = y

    def __add__(self, other):
        return Vector(self.pos_x + other.pos_x, self.pos_y + other.pos_y )

    def __sub__(self, other):
        return Vector(self.pos_x - other.pos_x, self.pos_y - other.pos_y )

    def __eq__(self, other):
        return Vector(self.pos_x == other.pos_x, self.pos_y == other.pos_y )

    def lenght(self):
        return (self.pos_x**2 + self.pos_y**2)**0.5

    def __lt__(self, other):
        return self.lenght() < other.lenght()

    def __mult__(self, other):
        return self.pos_x* other, self.pos_y* other


def test_vector_add():
    v1 = Vector(2,10)
    v2 = Vector(3,4)
    result =  v1 + v2
    assert result.pos_x == 5
    assert result.pos_y == 14

def test_vector_substr():
    v1 = Vector(5,10)
    v2 = Vector(3,4)
    result =  v1 - v2
    assert result.pos_x == 2
    assert result.pos_y == 6

def test_vector_equal():
    v1= Vector(1,3)
    v2= Vector(1,3)
    v3= Vector(4,7)
    assert v1 == v2
    assert not (v1==v3)

def test_vector_lenght():
    vector = Vector(2,2)
    assert vector.lenght() == 8**0.5 # czegos brakuje w nawiasie

def test_vector_lower_than():
    v1 = Vector(1, 3)
    v2 = Vector(1, 2)
    assert not (v1<v2)
    assert v2<v1

def test_vector_myultiplication_with_scalar():
    vector =Vector (2,4)
    result = vector + 2
    assert result.pos_x == 4
    assert result.pos_y == 4

