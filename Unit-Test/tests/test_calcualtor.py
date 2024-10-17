from calculator import square 

def test_square_positive():
    assert square(1) == 1 
    assert square(2) == 4 
    assert square(3) == 9
    assert square(7) == 49

def test_square_negative():
    assert square(-1) == 1 
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16

def test_square_zero():
    assert square(0) == 0
