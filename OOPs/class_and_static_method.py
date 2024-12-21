class Person: 
    @classmethod
    def get_person(cls): 
        print(f"Class name: {cls.__name__}")
        print(f"An object is created of {cls.__name__} class.")
    
    @staticmethod
    def has_vote_right(age:int):
        if age >= 18: 
            print("Person has vote right")
        else: 
            print("Person does not have vote right") 

class MyClass:
    _count = 0

    @classmethod 
    def count(cls): 
        return cls._count
    
    @classmethod 
    def increment_count(cls):
        cls._count += 1
    
    @staticmethod
    def add(x, y): 
        if not (isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float)): 
            raise TypeError("x and y must be of either int or float type")

        return x + y


def main(): 
    person = Person()

    # Invoking class method on class and instance of class
    person.get_person()
    Person.get_person()

    # Invoking static method on class and instance of class
    Person.has_vote_right(18)
    person.has_vote_right(25)

def main2(): 
    print(MyClass.count())
    MyClass.increment_count()
    MyClass.increment_count()
    print(MyClass.count())
    print(MyClass.add(45, 55))


if __name__ == "__main__": 
    # main()
    main2()