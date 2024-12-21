from datetime import datetime, date
import re, sys
import inflect

inflect_engine = inflect.engine()

def main(): 
    dob = input('Enter your dob in the format YYYY-MM-DD  ')
    minutes = get_elpased_minutes(dob)
    print(get_word(minutes) + ' minutes')

def get_word(number): 
    return inflect_engine.number_to_words(number, andword="")

def get_elpased_minutes(dob, today=date.today()):
    if not is_valid(dob): 
        sys.exit('Enter Valid date of birth in the specified format')

    year, month, day = dob.split('-')
    try: 
        dob = date(int(year), int(month), int(day))
    except ValueError: 
        sys.exit('day is out range for the month')

    dt = today - dob

    elapsed_minutes = dt.days * 24 * 60

    return elapsed_minutes

def is_valid(dob): 
    pattern = r'^\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[01])$'

    matches = re.search(pattern, dob)
    if matches: 
        return True  
       
    else: 
        return False 

# Automatically the date object handles this case so 
# no need to explicitly check this case leav it as it is
def is_leap_year(year):
    year = int(year)
        
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) 


if __name__ == "__main__": 
    main()  


