class Integer: 
    def __init__(self, number):
        self.data = int(number)
    
    def __str__(self): 
        return str(self.data)
    
    def __add__(self, other): 
        return Integer(self.data + other.data) 

    def __sub__(self, other): 
        return Integer(self.data - other.data)  

    def __mul__(self, other): 
        return Integer(self.data * other.data)    

    def __truediv__(self, other):
        return self.data / other.data 
    
    def __floordiv__(self, other): 
        return Integer(self.data // other.data)
    
    def __mod__(self, other):
        return Integer(self.data % other.data)
    
    def __pow__(self, other): 
        if isinstance(other, int): 
            return Integer(self.data ** other)
        else: 
            return Integer(self.data ** other.data)
        
    def binary_rep(self): 
        num = self.data

        if num > 0:
            bin = []
            while num: 
                mod = num % 2 
                bin.append(str(mod))
                num //= 2 
            bin.reverse()
            bin = ''.join(bin)
            return bin
        elif num == 0: 
            bin = "0"
            return bin
        # else: 
        



def main(): 
    num1 = Integer(0)
    num2 = Integer(3)
    add = num1 + num2 
    sub = num1 - num2 
    mul = num1 * num2 
    truediv = num1 / num2
    floordiv = num1 // num2
    modulo = num1 % num2
    pow_int = num1 ** 2
    pow_integer = num1 ** num2 
    # print(num1.binary_rep())
    print([1, 2, 3] + [4, 5])
    
    
    


if __name__ == "__main__": 
    main()