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
    temporary_file = './temporary.csv'

    with open(file_path, 'r') as org_file, open(temporary_file, "w") as temp_file: 
        reader = csv.DictReader(org_file)
        writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader: 
            if row == old_vegitable:
                writer.writerow(new_vegitable)
                continue
            
            writer.writerow(row)
    
    # delete the original file 
    os.remove(file_path)

    # rename the temporary file to the original file 
    os.rename(temporary_file, file_path)


def delete_vegitable(file_path, vegitable): 
    temporary_file = './temporary.csv'
    with open(file_path) as org_file, open(temporary_file, 'w') as temp_file: 
        reader = csv.DictReader(org_file)
        writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader: 
            if row != vegitable: 
                writer.writerow(row)
    
    # remove the original file 
    os.remove(file_path)

    # rename temporary file 
    os.rename(temporary_file, file_path)
