from datetime import datetime

def main(): 
    n = int(input("Enter a natural number "))

    print_natural_number(n)

# defining the decorator which would compute the execution time of given function
def execution_time(fun): 
    def compute_time(*args, **kwargs): 
        start_time = datetime.now()
        fun(*args, **kwargs)
        end_time = datetime.now()

        delta_time = end_time - start_time

        execution_time = (delta_time.days * 24 * 60 * 60 + delta_time.seconds) * (1000000) + delta_time.microseconds # Microseconds

        execution_time = execution_time / 1000.0 # milliseconds

        print(f"Function Execution time = {execution_time}ms")
    
    return compute_time

@execution_time
def print_natural_number(n): 
    for i in range(1, n+1, 1): 
        print(i, end=" ")
    print()
    

if __name__ == "__main__": 
    main()
