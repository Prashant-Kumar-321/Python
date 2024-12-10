class Jar: 
    def __init__(self, capacity=12): 
        if not isinstance(capacity, int) or capacity < 0: 
            raise ValueError('capcity must be non-zero integer value')
        
        self._capacity = capacity
        self._available_cookies = 0

    def __str__(self):
        cookie = '🍪'
        cookies = ''
        for _ in range(self._available_cookies): 
            cookies += cookie
        return cookies  
     
    def remaining_space(self): 
        return self._capacity - self._available_cookies
    
    def deposite(self, n:int):
        if n < 0: 
            raise ValueError(f'{n} must be positive')
        
        if n > self.remaining_space(): 
            raise ValueError(f'{n} cookies can not fit in the jar with capacity:{self.capacity}')
        
        self._available_cookies += n

    def withdraw(self, n:int): 
        if n < 0: 
            raise ValueError(f'{n} must be a positive number')
        
        if n > self.size: 
            raise ValueError(f'jar does not have {n} cookies')
        
        self._available_cookies -= n

    @property
    def capacity(self): 
        return self._capacity
    
    @property 
    def size(self): 
        return self._available_cookies
        

def main(): 
    jar = Jar(10) 
    jar.deposite(7)
    jar.withdraw(2)

    print(jar.capacity)
    print(jar.size)
    print(jar.remaining_space())
    print(jar)


if __name__ == '__main__': 
    main() 