from  fuel import convert, guage

import pytest

class TestFuel:
# Tests for convert function
    def test_convert_good_input(self): 
        assert convert('1/2') == 50
        assert convert('3/7') == 43
        assert convert('3/4') == 75
        assert convert('4/9') == 44
    
    def test_convert_bad_input(self): 
        with pytest.raises(ValueError): 
            convert('5/2')

        with pytest.raises(ZeroDivisionError): 
            convert('4/0')
        
        with pytest.raises(ValueError): 
            convert('7/5')

# Tests for guage function 

    def test_guage_empty(self): 
        assert guage(1) == 'E'
        assert guage(0) == 'E'
    
    def test_guage_full(self): 
        assert guage(99) == 'F'
        assert guage(100) == 'F'
    
    def test_guage_inbetween(self): 
        assert guage(45) == '45%'
        assert guage(78) == '78%'