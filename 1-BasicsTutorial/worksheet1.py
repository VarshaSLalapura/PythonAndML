# import numpy as np
import itertools

def winner(current_game):

    def all_equal(l,direction):
        if l.count(l[0]) == len(l) and l[0]!= 0:
            print('Player {} has won the game {}'.format(l[0],direction))
            return True
        else:
            return False

    # Horizontal:
    for row in game:
        if all_equal(row,direction="Horizontally"):
            return True

    # Vertical:
    check = []

    for row in game:
        check.append(row[0])
        # print(check)
    if all_equal(check,direction="Vertically"):
        return True

    # Diagonal:
    diag = []
    for idx in range(len(game)):
        print(game[idx][idx])
        diag.append(game[idx][idx])
    if all_equal(diag,direction="Diagonally (\\)"):
        return True


    diag = []
    # row = range(len(game))
    # col = reversed(range(len(game)))
    for idx,row in enumerate(reversed(range(len(game[0])))):
        # print(idx,row)
        diag.append(game[idx][row])
    # print(diag)
    if all_equal(diag,direction="Diagonally /"):
        return True

    return False


def game_board(current_game, player=0, row=0, col=0, just_display=False):

    try:
        if game[row][col] != 0 :
            print("Oops, position already taken, try another")
            return game,False # careful of the order of return to match the same in the calling portion

        if not just_display:
            game[row][col] = player

        print('   0  1  2')
        for idx,row in enumerate(game):
            print(idx,row)
        return game,True

    except IndexError as e:
        print("Ooops! Please check your row/col choice(0,1,2) ",e)
        return game,False
    except Exception as e:
        print("WOOOooophs, some input is really crazily incorrect")
        return game,False


play = True
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    # we want to just display the board:
    game, _ = game_board(current_game=game, just_display=True)

    won = False
    player_choice = itertools.cycle([1, 2])
    while not won:
        current_player = next(player_choice) # placement of this statement in this loop and not below
        played = False
        while not played:
            # pick the player
            print("current_player", current_player)
            # ask which row column would he wanna play
            row_choice = int(input("Which row do you wanna play?(0,1,2): "))
            col_choice = int(input("Which col do you wanna play?(0,1,2): "))
            game, played = game_board(current_game=game, player=current_player, row=row_choice, col=col_choice,
                                      just_display=False)
            if winner(current_game=game):
                won = True
                again = input("Do you want to play agiain(y/n): ")
                if again.lower() == 'y':
                    print("Starting again")
                    play = True
                elif again.lower() == 'n':
                    print("Byeeeeee")
                    play = False
                else:
                    print("Incorrect input")
                    won = False



