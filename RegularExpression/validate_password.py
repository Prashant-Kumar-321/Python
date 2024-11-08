import re

password = input("Enter a password ? ")

if re.search(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])[^\s]{8,256}$", password):
    print("Valid")

else: 
    print("Invalid")

