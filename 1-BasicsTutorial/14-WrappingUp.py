import itertools
from colorama import Fore, Style, init
init()

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def winner(current_game):

    def all_equal(l,direction):
        if l.count(l[0]) == len(l) and l[0]!=0:
            print("Player {} has won the game {}".format(l[0],direction))
            return True
        else:
            return False

    # Horizontally
    for row in game:
        # print(row)
        if all_equal(row,direction="Horizontally"):
            return True

    # Vertically
    for col in range(len(game[0])):
        check = []
        for item in game:
            check.append(item[col])

    if all_equal(check, direction = "Vertically"):
        return True

    # Diagonally (\)
    diag = []
    for idx in range(len(game)):
        diag.append(game[idx][idx])

    if all_equal(diag, direction = "Diagonally (\\)"):
        return True

    # Diagonally (/)
    diag = []
    for row,col in enumerate(reversed(range(len(game[0])))):
        diag.append(game[row][col])

    if all_equal(diag, direction="Diagonally (/)"):
        return True

    return False


def game_board(game_map=game, player=0, row=0, col=0, just_display=False):
    try:
        if game[row][col]!=0:
            print("Position already taken, try another")
            return game, False
        if not just_display:
            game[row][col] = player

        print("   "+"  ".join(str(i) for i in range(len(game[0]))))
        # print('   1  2  3')
        print("   " + "  ".join(str(i) for i in range(len(game[0]))))
        # print('   1  2  3')
        for idx, row in enumerate(game):
            # print(idx, row)
            coloured_row = ""
            for item in row:
                if item == 0:
                    coloured_row += "   "
                elif item == 1:
                    coloured_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item == 2:
                    coloured_row += Fore.MAGENTA + " 0 " + Style.RESET_ALL
            print(idx, coloured_row)
        return game, True

    except IndexError as e:
        print("Check your row/col choice(0,1,2) ", e)
        return game, False
    except Exception as e:
        print("Something went really wrong!... ", e)
        return game, False


start_game = True
while start_game:
    # game1 = [[0, 0, 0],
    #         [0, 0, 0],
    #         [0, 0, 0]]
    print([[0 for i in range(len(game))] for i in range(len(game))])
    game_won = False

    # display the default settings:
    game_board(game_map=game, just_display=True)
    player = itertools.cycle([1, 2])

    while not game_won:
        current_player = next(player)
        played = False
        while not played:
            print("Current_player : ", current_player)
            row_choice = int(input("Which row would you like to play(0, 1, 2)"))
            col_choice = int(input("Which col would you like to play(0, 1, 2)"))
            game, played = game_board(game_map=game, player=current_player, row=row_choice, col=col_choice,
                                      just_display=False)

        if winner(current_game=game):
            game_won = True
            print("###")
            again = input("Game Over! Do you want to play the game again(y,n): ")
            if again.lower() == 'y':
                start_game = True
            elif again.lower() == 'n':
                start_game = False
                print("Byeeeeeeee")
            else:
                print("Invalid answer")
                game_won = False


