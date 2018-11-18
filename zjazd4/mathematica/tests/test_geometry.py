from mathematica.geometry.figures import square_area, triangle_area


def test_geometry():
    assert square_area(2,3) == 6
#    assert square_area(4) == 16 zabezpieczniue dla jednje wartosci
    assert square_area(-10,2) == None

def test_triangle_area():
    assert (4, 2) == 4
    assert (10,20) == 100