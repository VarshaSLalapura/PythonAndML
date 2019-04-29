game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(current_game, player=0, row=0, col=0, just_display=True):
    try:
        if not just_display:
            game[row][col] = player

        print('   1  2  3')
        for count, row in enumerate(game):
            print(count, row)
        return current_game
    except IndexError as e:
        print("Did you input input out of the index range?",e)
        return False # note this return
    except Exception as e: # Exception and not exception
        print(str(e))
        return False # note this return

def h_winner(current_game):

    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0]!= 0:
            print("H_Winner")

def v_winner(current_game):

    for col in range(len(game[0])):
        print(col)
        check = []
        for row in game:
            print(row)
            check.append(row[col])
            print(check)

        if check.count(check[col]) == len(check) and check[col]!= 0:
                print("V_Winner")


def dia_winner(current_game):
    check = []

    for row in game:
       check.append(row[i])
       i+=1
       print(check)




game_board(current_game=game, just_display=True)
game_board(current_game=game, player=1, row=0, col=0, just_display=False)
game = game_board(current_game=game, player=1, row=2, col=2, just_display=False)
# print(game_board(current_game=game_board, player=1, row=2, col=2, just_display=False))

game = game_board(current_game=game, player=1, row=2, col=1, just_display=False)
game = game_board(current_game=game, player=1, row=2, col=0, just_display=False)
h_winner_is = h_winner(current_game=game)
game = game_board(current_game=game, player=1, row=1, col=0, just_display=False)
v_winner_is = v_winner(current_game=game)
game = game_board(current_game=game, player=1, row=1, col=1, just_display=False)
d_winner_is = dia_winner(current_game)