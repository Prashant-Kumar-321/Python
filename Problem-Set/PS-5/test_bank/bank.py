def main(): 
    greeting = input("Enter greeting = ") 
    val = value(greeting) 
    print("$", val) 


def value(greet:str):
    if greet == "": 
        return 100
    
    greet = greet.strip()
    prefix = greet[0:5].lower()

    if prefix == 'hello': 
        return 0
    elif prefix[0] == 'h': 
        return 20 
    else: 
        return 100


if __name__ == "__main__": 
    main()
