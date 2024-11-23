import random

class Hat: 
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class variable (static variable)

    @classmethod
    def sort(cls, name):
        house  = random.choice(cls.houses)
        print(name, "is in", house) 


Hat.sort("Harry")