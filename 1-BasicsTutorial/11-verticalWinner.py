game = [[1, 1, 2],
        [1, 0, 1],
        [1, 2, 2]]




def winner(current_game):
    check = []
    column = [0, 1, 2]
    for col in column:
        for row in game:
            print()
            print(row)
            check.append(row[col])
            print(check)

        if check.count(check[0]) == len(check) and check[0] != 0:
            print("winner")


winner(game)
