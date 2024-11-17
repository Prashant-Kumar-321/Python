import re

name = input("What's your name ? ").strip()

matches = re.search(r"^(?P<last>.+), ?(?P<first>.+)$", name)

if matches: 
    name = matches.group("first") + " " + matches.group("last")

print(name)





