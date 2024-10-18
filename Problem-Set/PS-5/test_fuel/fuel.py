
def main():
    fraction = input("Enter Fraction")
    print(guage(convert(fraction))) 

# This function converts given fraction into perceantage

def convert(fraction): 
    # get the Numerator and Denometer part
    x, y = fraction.split('/')
    x, y = int(x), int(y)

    # Test for possible exceptions
    if y == 0: 
        raise ZeroDivisionError("A number can not be divided by Zero")
    elif x > y : 
        raise ValueError("Numberator must be less than Denometer") 

    percentage = int(round(x / y * 100, 0))

    return percentage


def guage(percentage:int): 
    if percentage <= 1: 
        return 'E'
    elif percentage >= 99: 
        return 'F'
    else: 
        return f'{percentage}%'


if __name__ == "__main__":
    main()