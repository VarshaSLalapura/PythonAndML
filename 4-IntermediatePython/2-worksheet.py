# string concatenation
# to read a file from a location
# using with open(os.path.join(oath,file_name)) as f

import os

path = "/home/varshalalapura/Desktop"
file_name = "To-Do-List"

with open(os.path.join(path,file_name)) as f:
    print(f.read())

# string formatting
# to print some_one has some_number of some_fuits using string format
some_one = "Bob"
some_number = "12"
some_fruits = "apples"

print('Bob has 12 apples')
print('{} has {} {}'.format(some_one, some_number, some_fruits))