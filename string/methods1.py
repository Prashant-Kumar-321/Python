string = 'my name is nishant'
# print(string.replace('nishant', 'Prashant')) # All occurences are replaced by new string
string = 'abdefgababcfg' 
# print(string.replace('ab', 'AB'))
# print(string)

string = 'aaa,bbb,ccc'
full_name = 'Prashant kumar gupta'
# print(string.split(','))
# print(full_name.split())

name_comps = full_name.split()
# full_name = '----'.join(name_comps)
# print(full_name)


s = 'Hello'

# ******** String formatting *********** 

value = 2.791514
# print(f"approximate value = {value:.2f}") # rounded upto 2 decimal places

car = {
    'tires': 4, 
    'doors': 2
}

# print(f"car = {car}")


address_book = [
    {
        'name': 'N.x.', 
        'addr': '15 Jones St',
        'bonus':70,
    }, 
    {
        'name': 'J.P.',
        'addr': '1005 5th St',
        'bonus': 400
    },
    {
        'name': 'A.A.', 
        'addr': '20001 Bdwy',
        'bonus': 5,
    }
]

# print(f"{'Name':8} || {'Pddress':20} || {'Bonus':>5}")
# for person in address_book: 
#     print(f"{person['name']:8} || {person['addr']:20} || {person['bonus']:>5}")


# String % 

# % c style formating 
text = ("%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." %(3, 'huff', 'puff', 'house'))
# print(text)


# ***************** Strings Unicode vs Bytes ********** 
byte_string = b"A sample byte string"
print(byte_string.decode()) # Convert into regular string
ustring = "A unicode \u018e string \xf1" 
b = ustring.encode()
print(b.decode() == ustring)

