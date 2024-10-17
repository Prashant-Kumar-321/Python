from twttr import is_vowel, shorten

def test_is_vowel(): 
    assert is_vowel('A') == True 
    assert is_vowel('E') == True 
    assert is_vowel('V') == False 
    assert is_vowel('i') == True 
    assert is_vowel('y') == False
    assert is_vowel("@") == False

# test for the shorten 
def test_shorten(): 
    assert shorten("Prashant") == "Prshnt"
    assert shorten("") == ""
    assert shorten("Twitter") == "Twttr"
    assert shorten("aEi#oU") == "#"