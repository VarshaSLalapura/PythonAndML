# make the game map first:

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

'''
print('   a, b, c')
for count,row in enumerate(game):
    print(count,row)

#player wants to change row 0, ele 1:
game[0][1] = 1

print('   a, b, c')
for count,row in enumerate(game):
    print(count,row)
'''


# We see that we repeated the same code block twice, instead def
# a function and call it when needed

def game_board() -> object:
    """

    :rtype: object
    """
    print('   a  b  c')
    for count, row in enumerate(game):
        print(count, row)


'''
#now call the function, note use paranthesis after the function name, or
# it will simply be pointed and not called.
game_board()

#now a gamer makes a change in row 0, ele 1:
game[0][1] = 1

#see the changes on the board by calling it agian:

game_board()
'''

# we could also use a variable to call this function, for that
# first assign the function to a variable

x = game_board  # note, no use of paranthesis for assignment to variable

# make changes to the elem
game[0][1] = 1

# call x again, note calling needs paranthesis
x()

