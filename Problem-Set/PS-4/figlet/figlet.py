from pyfiglet import Figlet 
from sys import exit, argv 
import random 

figlet = Figlet() 
available_fonts = figlet.getFonts()
random_font = True
font = None 

# handle command line arguments 
def handle_command_line_arg_error(): 
    global random_font, font

    if len(argv) == 3: # user has specified 2 arguments 

        if argv[1] != '-f' and argv[1] != '--font': 
            # termianate the program 
            exit("Wrong option")

        elif argv[2] not in available_fonts: 
            exit("Font not available")
        
        random_font = False 
        font = argv[2]

    elif len(argv) == 1: 
        random_font = True
        font = random.choice(available_fonts)

    else:
        exit("Invalid number of arguments: Expecting 2")

def main():

    user_input = input("Enter text: ")
    
    figlet.setFont(font=font)

    print(figlet.renderText(user_input))


if __name__ == '__main__': 
    handle_command_line_arg_error() 
    main()