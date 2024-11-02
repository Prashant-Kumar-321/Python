# name = input("What's your name ? ")

# with open('names.txt', 'a') as file: 
#     file.write(f'{name}\n')


# Read names from the file 

def read_all_names(): 
    # with open("names.txt", "r") as file: 
    #     lines = file.readlines()

    # for line in lines:
    #     print(f'Hello, {line.rstrip()}')

    # ## Compact version ## 
    names = []

    with open("names.txt", "r") as file: 
        for line in file: 
            names.append(line.rstrip())

    for name in sorted(names): 
        print("Hello,", name)

read_all_names()
