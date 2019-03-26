# if the user has fat fingers and inputs a or someother input that
# will cause the tic tac toe to throw errors and he doesnot like
# to see the non-sense instead sees a short msg, heres how it is


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print(game)


def game_board(game_map, player, row, col, just_display=False):
    from logging import exception
    try:
        if not just_display:
            game[row][col] = player
        print('   a  b  c')
        for count, row in enumerate(game):
            print(count, row)
        return(game_map)

    except IndexError as e:
        print("Make sure you input row/col as 0,1 or 2", e)
        # print("Something went wrong, please check")
        return False
    except Exception as e:
        print("Something went very wrong!!!", str(e))
        return False

game = game_board(game, 1, 0, 0, True)
game = game_board(game_board, 1, 1, 0)  #this should also throw up error since I input game_board function name, but IT ISN't?????
                                        #game object
print(id(game))
# game = game_board(game, 1, 3, 0) #this throws up error, index out of range
# to cool the user with less intimidating error msg we can do
# try: except thingy

# we could take one step further to say except: IndexedError as e
print(game_board(game_board, 1, 1, 0)) # here it ISSSSSS throwing the exception, how come?
print(id(game))