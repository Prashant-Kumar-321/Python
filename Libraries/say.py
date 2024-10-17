import cowsay
import sys

from saying import hello 

# if len(sys.argv) == 2: 
#     cowsay.trex(f"Hello! {sys.argv[1]}")

if len(sys.argv) != 2: 
    sys.exit("Give appropriate number of arguments")

# print(__name__)
hello("Prashant")
