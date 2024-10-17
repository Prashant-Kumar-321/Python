import inflect

InfEngine = inflect.engine()


def main(): 
    names = []
    while(True): 
        name = input('Name: ')
        if name == 'ctrl-D': 
            break 
        names.append(name)


if __name__ == "__main__": 
    try: 
        key = input("Enter shortuct: ")
    except KeyboardInterrupt: 
        print("Keyboard Interrruption has occured")
        print(KeyboardInterrupt.key)
    
    print(key)
    # main() 




















































# concating the tuples 
# t1 = (1, 2) 
# t2 = t1 + (2, 3) 
# t3 = t2 + t1 

# # coverting list into tuples 
# l = [1, 2, 3] 
# lt = tuple(l) 

