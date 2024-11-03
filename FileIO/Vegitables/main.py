import vegitables 

FILE_PATH = './vegitables.csv'

def main(): 
    # name = input("What is the name of the vegitable ? ")
    # price = input("What's the price of the vegitable ? ")

    # vegitable = {"name": 'LadyFinger', "price": '60'}
    # vegitables.add_vegitables(FILE_PATH, vegitable)
    # vegitables.update_vegitable(FILE_PATH, {"name": "Cabage", "price": '50'}, {"name": "Cabage", "price": '100'})

    vegitables.delete_vegitable(FILE_PATH, {"name": "Tomato", "price": "100"})
    vegitables.print_vegitables(FILE_PATH)



if __name__ == "__main__": 
    main()