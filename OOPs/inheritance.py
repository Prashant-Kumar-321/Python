class A: 
    # class attribute 
    name = "class A"

    def __init__(self): 
        self.a = "instance variable of class A"
    
    @classmethod 
    def class_method(cls): 
        print("Class method is invoked")
        print(f"class attribute/property: {cls.name}")

class B(A): 
    name = "Class B"

    def __init__(self): 
        super().__init__()
        self.b = "instance varibale of class B"

def main(): 
    objA = A()
    # objA.extraAttr = "Extra Attribute"
    # print(A.name)
    # print(objA.a)
    # print(objA.name)
    # print(objA.extraAttr)
    
    objB = B()
    print(B.name)
    print(objB.name)
    B.class_method()


if __name__ == "__main__": 
    main() 