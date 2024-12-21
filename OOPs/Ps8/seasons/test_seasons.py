from .seasons import get_elpased_minutes, is_valid 
from datetime import date

def test_is_valid(): 
    assert is_valid('2023-24-12') == False
    assert is_valid('5645-10-3') == True
    assert is_valid('209-4-29') == False 
    assert is_valid('2019-13-2') == False 
    assert is_valid('1998-09-21') == True 
    assert is_valid('2007-10-32') == False 
    assert is_valid('2009-09-21') == True 
    assert is_valid('wiur-ij-dk') == False 
    assert is_valid('') == False 
    assert is_valid('1467-08-04') == True  
    assert is_valid('2023-09-12') == True 
    assert is_valid(' 1989-23-09') == False


def test_get_elapsed_minutes(): 
    assert get_elpased_minutes('2023-12-12', date(2024, 12, 12) ) == 527040
    assert get_elpased_minutes('2024-12-11', date(2024, 12, 12)) == 1440
    assert get_elpased_minutes('2022-9-12', date(2023, 12, 7)) == (date(2023, 12, 7)-date(2022, 9, 12)).days * 24 * 60