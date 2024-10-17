import pytest

from calculator import square

class TestSquare():
    def test_square_positive(self): 
        assert square(2) == 4
        assert square(3) == 9 

    def test_square_negative(self): 
        assert square(-2) == 4 
        assert square(-3) == 9 

    def test_square_zero(self): 
        assert square(0) == 0

    def test_square_str(self): 
        with pytest.raises(TypeError): 
            square("cat") 
    