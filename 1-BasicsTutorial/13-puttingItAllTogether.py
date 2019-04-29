# display the game board and feed in the inputs from the players
# all zeros and zero players is the default of the game
# determine who is the winner

def winner(current_game):
    print("Scanning horizontally")
    def are_all_equal(l):

        if l.count(l[0]) == len(l) and l[0]!=0:
           print("Player {} has won the game".format(l[0]))

    # horizontal winner:
    for row in game:
        print(row)

        are_all_equal(l=row)


    print("Scanning vertically")
    # vertical winner:
    # pick the 1st elem of each row , "make a list", check
    for col in range(len(game[0])):
        check = []
        for row in game:
            print(row[col])
            check.append(row[col])
        print(check)

        are_all_equal(l=check)



    print("Scanning diagonally \\")
    # diagonal winner:
    # \
    # take the elem g[0][0] , g[1][1], g[2][2], "make a list", check
    diag = []
    for idx,row in enumerate(game):
        print(idx)
        diag.append(game[idx][idx])
    print(diag)

    are_all_equal(l=diag)

    print("Scanning diagonally /")
    # we want to access g[0][2], g[1][1], g[2][0], "make a list", check
    diag = []
    for row,col in enumerate(reversed(range(len(game[0])))):
        print(row,col)
        print(game[row][col])
        diag.append(game[row][col])
    print(diag)

    are_all_equal(l=diag)


def game_board(current_game, player=0, row=0, col=0, just_display=False):
    try:

        if not just_display:
            game[row][col] = player

        print('   1  2  3')
        for idx,row in enumerate(game):
            print(idx,row)
        return current_game
    except IndexError as e:
        print("Check your row/col choice : ", e)
        return False
    except Exception as e:
        print("Something is really wrong with the set of inputs to this!!!  ", e)
        return False

play = True
import itertools
while play:

    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game = game_board(current_game=game, just_display=True) # if I wrote this here
    won_game = False
    player_choice = itertools.cycle([1, 2])
    #for i in player_choice:
    #    print(i)
    while not won_game:

        current_player = next(player_choice)
        print("Current_player {}".format(current_player))
        col_choice = int(input("Which col do you wanna play(0,1,2): "))
        row_choice = int(input("Which row do you wanna play(0,1,2): "))

        # game_board(current_game=game, just_display=False)
        game_board(current_game=game, player = current_player, row=row_choice, col=col_choice, just_display= False)
        # and this here check to run the code but first comment out return current_game in the func def
        # g = game_board(current_game=game, player=current_player, row=row_choice, col=col_choice, just_display=False)