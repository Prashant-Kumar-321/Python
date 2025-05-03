# DECORATOR A POWERFUL TOOL TO WRITE CLEAN AND REUSABLE FUNCTIONAL CODE    

## Definition
A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it and returns an replacement function

## Syntax
```python   
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Add some functionality before calling the original function
        ...
        res = riginal_function(*args, **kwargs)
        # Add some functionality after calling the original function
        ...
        return res
    return wrapper_function

Decoratoring your function              
@decorator_function
def display():
    print("Display function executed")
```
When we'll call the ```display()``` function, it will execute the ```wrapper_function()``` inside the ```decorator_function()```

## Creating Decorator Factory by Passing Argument to Decorator
We can pass arguments to decorator functions by creating a decorator factory. 
```Decorator Factory``` A decorator factory is a function that returns a decorator. The decorator can then accept arguments and use them to modify the behavior of the original function.

```python
    def decorator_factory(arg1): 
        if arg1 == "hello": 
            def decorator_function(original_function): 
                def wrapper_function(*args, **kwargs): 
                    print(f"Decorator argument: {arg1}") 
                    return original_function(*args, **kwargs) 
                return wrapper_function
        else:
            def decorator_function(original_function): 
                def wrapper_function(*args, **kwargs): 
                    print(f"Decorator argument: {arg1}") 
                    return original_function(*args, **kwargs) 
                return wrapper_function

        return decorator_function

```

```Observation about Decorators``` Decorators are like constrcutor that we can use to create different versions of the inner function where enclosure variables are like private variables just like objects. 

## External References
[Detailed Essay for Understanding the Decorator and its nuances](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
