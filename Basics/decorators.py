from datetime import datetime
import time

def main(): 
    # print(say_hello("Jack"))

    # print_100_times("Prshant", 100)
    hello_world()

def my_decorator(func): 
    def wrapper(*args, **kwargs): 
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result 

    return wrapper

@my_decorator
def say_hello(name): 
    return f"Hello, {name}"


def calculate_running_time(func_name):
    def decorator(func): 
        def wrapper(*args, **kwargs): 
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            print(f"\n{func_name} takes : {(end-start)*100} ms.")

            return result 

        return wrapper
    return decorator

@calculate_running_time("print_100_times")
def print_100_times(element, repitition): 
    for i in range(repitition): 
        if i != repitition-1: 
            print(element, end="/", sep="/")
        else:     
            print(element)

# It takes function as argument and is nested function
# @decorator which is printing the developer name
def print_developer_name(fun_name=None): 
    def decorator(fun): 
        resolved_fun_name = fun_name or fun.__name__
        def wrapper(*args, **kwargs):
            # resolved_fun_name = fun_name or fun.__name__
            print("Developer name: Prashant Kumar Gupta")
            print(f"I am really very happy to call your function <{resolved_fun_name}>")

            return fun(*args, **kwargs)
        return wrapper
    return decorator

@print_developer_name("Hello World function")
def hello_world(): 
    print("Hello world!!")



if __name__ == "__main__": 
    main()

    