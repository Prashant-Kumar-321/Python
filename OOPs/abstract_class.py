from abc import ABC, abstractmethod

# Abastract Base Class
class Shape(ABC): 
    @abstractmethod 
    def area(self): pass # Sub class must implement this method 

    @abstractmethod
    def perimeter(self): pass  # Sub Class must implement this method

class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
    
    def __str__(self): 
        return f"Circle: <radius = {self.radius}>"

    def area(self): 
        return 22/7 * self.radius * self.radius 
     
    def perimeter(self): 
         return 2 * 22/7 * self.radius 

class Rectangle(Shape): 
    def __init__(self, length, width): 
        self.length = length 
        self.width = width 

    def __str__(self): 
        return f"Rectangle <length = {self.length}, width = {self.width}>"

    def area(self): 
        return self.length * self.width 

    def perimeter(self): 
        return 2 * (self.length + self.width) 

def main(): 
    circle = Circle(7)
    # print(circle) 
    # print(circle.area())
    # print(circle.perimeter())

    rect = Rectangle(10, 15)
    # print(rect)
    # print(rect.area())
    # print(rect.perimeter())

    for shape in (circle, rect): 
        print(shape) 
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}") 
        print() 


if __name__ == "__main__": 
    main()

