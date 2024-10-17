from plate import is_valid

class TestIsValid(): 
    def test_leading_digits(self): 
        assert is_valid("8AADE6") == False
        assert is_valid("243235") == False
        assert is_valid("AA8723") == True
    
    def test_length(self): 
        assert is_valid("") == False 
        assert is_valid("RT") == True 
        assert is_valid("BTUS8776") == False 
    
    def test_middle_number(self): 
        assert is_valid("EPR76T") == False
    
    def test_first_zero(self): 
        assert is_valid("TYUT03") == False
    
    def test_start_two_letters(self): 
        assert is_valid("UE78") == True 
        assert is_valid("Y56") == False 