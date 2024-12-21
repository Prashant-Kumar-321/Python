class Person: 
    def __init__(self, fname, lname): 
        # print("Person class __init__ invoked")
        self.firstname = fname
        self.lastname = lname
    
    def printname(self): 
        print(self.firstname, self.lastname)

class Student(Person): 
    def __init__(self, fname, lname, graduate_year): 
        # print("Student class __init__ invoked")
        # Person.__init__(self, fname, lname)
        super(Student, self).__init__(fname, lname)
        self.graduate_year = graduate_year

    def print_graduate_year(self): 
        print(self.graduate_year)



def main(): 
    # person = Person("Prashant", "Kumar Gupta")
    # person.printname()

    student = Student("Shivan", "Kumar", 2025)
    student.printname()
    student.print_graduate_year()
    


if __name__ == "__main__": 
    main()
