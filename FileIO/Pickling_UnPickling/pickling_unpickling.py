import pickle
from pickle import Pickler, Unpickler




""" 
Pickling and Unpickling in python is the process of serializing and deserialization a python object structure. 

pickle: python object -----> byte stream
unpickle: byte stream -----> python object
"""
class Triangle: 
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b 
        self.c = c 
    
    def __str__(self): 
        return f"a:{self.a}, b:{self.b}, c:{self.c}"


def pickle_unpickle_userdefined_object(): 

    triangle = Triangle(1, 2, 3)

    with open("triangle.pkl", "wb") as file:
        Pickler(file).dump(triangle) 
    
    with open("triangle.pkl", "rb") as file: 
        unpickled_triangle = Unpickler(file).load()

    print("Triangle: ", triangle)
    print("Unpickled Triangle: ", unpickled_triangle)

def main(): 
    names = ("Prashant", "Nishant", "Ravi", "Amrita", "Taniya", "Sumati", "Suraj", "Aditya", "Muskan")

    triangle = Triangle(1, 2, 3)

    with open("names.pkl", "wb") as file:
        Pickler(file).dump(triangle) 
        # pickle.dump(names, file)
    
    with open("names.pkl", "rb") as file: 
        unpickled_triangle = Unpickler(file).load()
        # unpickled_names = Unpickler(file).load()
        # unpickled_names = pickle.load(file)
    
    # print("Names: ", names)
    # print("unpickled_names: ", unpickled_names)

    print(triangle)
    print(unpickled_triangle)


if __name__ == "__main__": 
    # main()
    pickle_unpickle_userdefined_object()