# tic , tac , toe game
from typing import Tuple, List

game_t = (0, 0, 0,
          0, 0, 0,
          0, 0, 0)  # type: Tuple[int, int, int, int, int, int, int, int, int]

print(game_t)

game_l = [0, 0, 0,
          0, 0, 0,
          0, 0, 0]  # type: List[int]  

print(game_l)

# from flat to non-flat version, i.e row column version of the list, we need list of lists
# [] for the outer list,
# [],[],[] for the set of lists within

game_ll = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]  # type: List[List[int]]
print(game_ll)

for row in game_ll:
    print(row)

print("1#############")

print('  a,  b,  c')
game_ll = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0], ]

count = 0
for row in game_ll:
    print(count, row)
    count += 1

print('2######')

print('   a  b  c')
game_ll = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for count, row in enumerate(game_ll):  # type: (int, List[int])
    print(count, row)

'''

print('   a  b  c')
game_ll = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# count1 = 0
for count1, row in enumerate(game_ll):  # type: (int, List[int])
    print('items in %d row :' %count1)
    for item in row: # here each row is a list itself, so iterate over the items in the list
        print(item)

'''
# part 5 of the tutorial
# indexing and slicing
l = [1,2,3,4,5]

print('2nd element in the list l : ', l[1])

# want to slice the list from 2 : 5 meaning access the elements from 2 to 4
print('slice of the list from 2 : 5', l[2:5])

print('everything from the 2nd index of l:' , l[2 :])

print('last element of l : ', l[-1])


# we can set something at a specific index:
l[1] = 10 # because it is mutable

# now check l
print(l)

# now in case of game_ll object which is list of list type:
# to access the 0th row of the game_ll
print(game_ll[0]) # this will print [0, 0 ,0]

# lets say we want to modify 0th row, 2nd element in that row:
game_ll[0][1] = 1

print(game_ll)
# this gave a flat version, we want line after line,

#for count1, row in game_ll:
#   print(count,row)

# the above two lines of code throws up error, too many values to unpack, so i missed the enumerate function on the variable

for count1,row in enumerate(game_ll):
    print(count1,row)

#Now we have block of code for count..... which is written repeatedly,
#we want to define a function for this repeating block of code

#just made out that variable is in some styling case,
#function is in
#camelCase
# class is in title case where each word is CapitalizedInTheBeginning

#so lets define the function:
def game_board():
    for count1, row in enumerate(game_ll):
        print(count1, row)

game_board()

game_ll[0][0] = 1

game_board()



