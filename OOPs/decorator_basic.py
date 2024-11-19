def main(): 
    hello(2)


def decorator(function): 
    def hello_world(num, **kwargs): 
        # Add the custom behaviour before calling the original function 
        function(num, **kwargs)
        # Add the custom behaviour after calling the original function 
        print("world!",)
    
    return hello_world # return the new wrapped function 

@decorator
def hello(num): 
    print(f"Hello, {num}", end=' ')


if __name__ == "__main__": 
    main()

# lambda function syntax
# lambda arguments: definitions
