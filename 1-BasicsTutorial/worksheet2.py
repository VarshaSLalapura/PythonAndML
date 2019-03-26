# two parts: Display the 0 level board,
# Check if you want to play
# if the game is won
# next player has to play

import itertools

def winner(current_game):

    def all_equal(l,direction):
        if l.count(l[0])==len(l) and l[0]!= 0:
            print('Player {} has won the game {}'.format(l[0],direction))
            return True
        #else:
            #return False

    # Horizontal win
    for row in game:
        # print(row)
        if all_equal(row, direction="Horizontally"):
            return True

    # Vertical win
    check = []
    for row in game:
        check.append(row[0])

    if all_equal(check, direction="Vertically"):
        return True

    # diag
    diag = []
    for idx in list(range(len(game[0]))):
        diag.append(game[idx][idx])

    if all_equal(diag,direction="Diagonally \\"):
        return True

    # row = list(range(len(game)))
    # col = reversed(range(len(game[0])))
    # for i,j in zip(row,col):
    #     print(i,j)
    #
    diag = []
    for row,col in enumerate(reversed(range(len(game[0])))):
        print(game[col][row])
        diag.append(game[row][col])
    # print(diag)
    if all_equal(diag,direction='Diagonally /'):
        return True

    return False

def game_board(game_map=game,player=0,row=0,col=0,just_display=False):

    try:
        if game[row][col] != 0:
            print("Oops, position taken, try again")
            return game, False

        if not just_display:
            game[row][col] = player

        print('   0  1  2')
        for idx, row in enumerate(game):
            print(idx, row)
        return game, True

    except IndexError as e:
        print('Check you row/col choice(0,1,2) ',e)
        return game, False
    except Exception as e:
        print('Something is really wrong ',e)
        return game, False


play = True
while play:
    # game = ([[0 for i in range(len(game))] for i in range(len(game[0]))])
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game,_ = game_board(game_map=game,just_display=True)
    player_choice = itertools.cycle([1, 2])
    game_won = False
    while not game_won:
        played = False
        current_player = next(player_choice)
        while not played:
            print('top')
            print("current_player = ", current_player)
            row_choice = int(input("Which row would you like to play(0,1,2): "))
            col_choice = int(input("Which col would you like to play(0,1,2): "))
            game, played = game_board(game_map=game,player=current_player,row=row_choice,col=col_choice,just_display=False)
            print('played = ',played)
            # game_won = winner(current_game=game)
            # print('game_won',game_won)

            if winner(current_game=game):
                game_won = True
                again = input('Do you want to play again?(y/n):  ')
                if again.lower() == 'y':
                    print('Starting again')
                    play = True
                elif again.lower() == 'n':
                    print('Byeeee')
                    play = False
                else:
                    print('Check your input (y/n)')








