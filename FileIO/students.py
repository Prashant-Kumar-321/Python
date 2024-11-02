# with open("students.csv", "r") as file: 

#     for line in file: 
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")


import csv

# students = []
# with open("students.csv", "r") as file: 
    # for line in file: 
    #     name, house = line.rstrip().split(",")
    #     student = {"name": name, "house": house}
    #     students.append(student)

#     reader = csv.DictReader(file)
#     for row in reader: 
#           students.append({"name": row["name"], "home": row["home"]})


# for student in sorted(students, key=lambda student : student["name"], reverse=False): 
#         print(f'{student["name"]} is from {student["home"]}')






# Writing to the csv file using csv module

name = input("What's your name ?")

home = input("Where is your home ? ")


with open("students.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])
    # writer.writerows([['Prashant', 'Ganaloya, Murhu'],['Shubham', 'Korakel, Khunti']])

    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name}) 

