import vegitables 

FILE_PATH = './vegitables.csv'

def main(): 
    # name = input("What is the name of the vegitable ? ")
    # price = input("What's the price of the vegitable ? ")

    # vegitable = {"name": name, "price": price}

    # vegitables.add_vegitables(FILE_PATH, vegitable)
    # vegitables.update_vegitable(FILE_PATH, {"name": "Onion", "price": '80'}, {"name": "Onion", "price": '100'})

    vegitables.delete_vegitable(FILE_PATH, {"name": "Onion", "price": "100"})
    vegitables.print_vegitables(FILE_PATH)



if __name__ == "__main__": 
    main()