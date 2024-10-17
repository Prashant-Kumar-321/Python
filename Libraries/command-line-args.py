import sys

# print(f'Name of python file {sys.argv[0]}')
# print(f'My name is {sys.argv[1]}')

if len(sys.argv) < 2: 
    sys.exit(f"Too few arguments to {sys.argv[0]}")

# elif len(sys.argv) > 2: 
#     sys.exit(f"Too many arguments to {sys.argv[0]}") 

for arg in sys.argv[1:4]: 
    print(f"Hello! My name is {arg}")