cities = []

def main():
    write_cities()
    read_cities()


def write_cities(): 
    with open("cities.txt", "a") as file: 
        for _ in range(3): 
            file.write(input("Enter city name : "))
            file.write("\n")
        

def read_cities(): 
    with open("cities.txt") as file: 
        for line in file: 
            cities.append(line.rstrip())
        

    for city in sorted(cities): 
        print(city)
    

if __name__ == "__main__":
    main() 
