import os

names = ['Bob', 'Nimma', 'Devi', 'Next']
print('Hello there, ..........!')


print()
# region: List of Strings and join() method
# 1
for name in names:
    print('Hello there,',name)
# print(names, 'and', names, 'are with', names, 'and', names,  'on a holiday')

# print(name, 'and', name, 'are with', name, 'and', name,  'on a holiday')
print()

# 2
for name in names:
    sentence = ''.join(['Hello there,',name])
    print(sentence)

# 3 : want : Bob, Nimma, Devi, Next
print(', '.join(names))
# endregion

# region: file_location and reading in two lines: cc(code compaction)

file_loc = "/home/varshalalapura/Desktop"
file_name = 'To-Do-List'
# 1 : crude
my_file = file_loc + '/' + file_name
print(my_file)

# 2 : compact and readable
with open(os.path.join(file_loc,file_name)) as f:
    print(f.read())

# endregion

# region : good string concatenation practise

# # want : Bob has 12 apples

l = ['Bob',12]
print(l)
print('{} has {} apples'.format(l[0],l[1]))

# 2: more logical way and relatable and readable
who = 'Nimma'
how_many = '3'
what = 'oranges'
print('{} has {} {}'.format(who,how_many,what))
# endregion