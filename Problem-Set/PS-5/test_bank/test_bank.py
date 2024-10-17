from bank import value 

class TestValue(): 
    def test_value_hello(self): 
        assert value("Hello") == 0
        assert value("Hello, Sir") == 0
        assert value("    HELLO, regular customer") == 0

    def test_value_start_h(self): 
        assert value("How are doing?") == 20 
        assert value("   how are you?") == 20
        assert value("HOW's it going?") == 20
        assert value("hey") == 20 


    def test_value_else(self): 
        assert value("What's up?") == 100
        assert value("what's happening?   ") == 100
        assert value("whats' going on?") == 100 
        assert value("") == 100 