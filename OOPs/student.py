class Student:
    def __init__(self, name, house): 
        self.name = name
        self.house = house  # This will invoke the setter function // # We make the house variable constant

    def __str__(self): 
        return f"{self.name} from {self.house}" 

    @classmethod
    def get(cls): 
        name = input("Name: ")
        house = input("House: ")

        return cls(name, house) # Reference to the class

    # Getter 
    @property
    def house(self): 
        return self._house 

    # Settter 
    @house.setter
    def house(self, house): 
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']: 
            raise ValueError("Invalid house")
        
        self._house = house

    @property
    def name(self): 
        return self._name

    @name.setter
    def name(self, name): 
        if not name: 
            raise ValueError("Missing name ")
        
        self._name = name


def main(): 
    student = Student.get()
    print(student.get())
    print(student)


if __name__ == "__main__": 
    main()