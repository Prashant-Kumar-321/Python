def main(): 
    plate = input("What is your plate number? ")
    if is_valid(plate): 
        print("Valid")
    else: 
        print("Invalid")


# Utilities methods for is_valid method

def has_valid_length(plate): 
    return True if 2 <= len(plate) <= 6 else False # Ternary Operator


def  start_with_letters(plate): 
    return plate[0].isalpha() and plate[1].isalpha()


def has_middle_number_or_invalid_number_seq(plate):
    # flag variables
    first_digit = None
    found_digit = False 

    for char in plate: 
        if found_digit and char.isalpha(): # number is in-between
            return True
        if char.isdigit(): 
            first_digit = (char if found_digit == False else first_digit) 
            found_digit = True 
    
    # Number is not in the middle

    # check valid sequence
    return  first_digit == '0' # number not start with 0 


def has_special_char(plate): 
    for l in plate: 
        if not l.isalnum(): 
            return True 
    return False 


def is_valid(plate): 

    if not has_valid_length(plate) or not start_with_letters(plate) or has_middle_number_or_invalid_number_seq(plate) or has_special_char(plate): 
        return False 

    return True

if __name__ == "__main__": 
    main() 