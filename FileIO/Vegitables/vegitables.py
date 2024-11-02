import csv
import os

# file -> where given vegitables has to be added: string
# vegitable -> This is the vegitable to be added : Dict

def add_vegitables(file_path, vegitable): 
    with open(file_path, 'a') as file: 
        writer = csv.DictWriter(file, fieldnames=["name", "price"])
        writer.writerow(vegitable)


def print_vegitables(file_path): 
    with open(file_path) as file: 
        reader = csv.DictReader(file)

        novegitables = True

        for row in reader: 
            print(f'[{row["name"]}, {row["price"]}]')
            novegitables = False
        
        if novegitables:
            print("No vegitables available")
        
        

def update_vegitable(file_path, old_vegitable, new_vegitable): 
    
    org_file = open(file_path)
    temp_file = open("./temporary.csv", 'w') # create a temporary file

    temp_file.write('name,price\n') # Create a header of the csv 

    reader = csv.DictReader(org_file)
    writer = csv.DictWriter(temp_file, fieldnames=['name', 'price'])

    for row in reader: 
        if row == old_vegitable:
            writer.writerow(new_vegitable)
        else: 
            writer.writerow(row)
    
    # delete the original file 
    os.remove(file_path)

    # rename the temporary file to the original file 
    os.rename('./temporary.csv', file_path)
    temp_file.close()


def delete_vegitable(file_path, vegitable): 
    temporary_file = './temporary.csv'

    org_file = open(file_path)
    temp_file = open(temporary_file, 'w')

    temp_file.write('name,price\n') # csv header

    reader = csv.DictReader(org_file)
    writer = csv.DictWriter(temp_file, fieldnames=['name', 'price'])

    for row in reader: 
        if row != vegitable: 
            writer.writerow(row)
    
    # remove the original file 
    os.remove(file_path)

    # rename temporary file 
    os.rename(temporary_file, file_path)
    temp_file.close()
