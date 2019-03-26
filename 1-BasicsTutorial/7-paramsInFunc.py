# part 7: function parameters and typing

# first some basic examples:

def addition(a, b):
    return (a + b)


# print(addition(3,5))

# or
'''
y = addition(3,5)
print(y)

'''

# or
y = addition("hey", " there")
print(y)

# or say
z = addition(str(5), " there")
print(z)

# an error throws up, saying we cant add str and int
# so make str(5) and run


# Now this is important: Python is dynamically typed


#We first want to display the game board,
#then once again, call the function to
#let the player put his position

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

'''
def game_board(player,row,col, just_display = False):
    if not just_display:
        game[row][col] = player
    print('  a  b  c')
    for count,row in enumerate(game):
        print(count,row)

game_board(1,0,0,True)
game_board(1,0,0)
'''

#note that the game map "game" is declared outside
#of the function, and changes to this is made inside the function.
#not a good practise, see the next tutorial


def game_board(player,row,col):

    game[row][col] = player
    print('  a  b  c')
    for count,row in enumerate(game):
        print(count,row)

game_board(1,0,0)
game_board(0,0,0)




