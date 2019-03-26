game = [[1, 1, 1],
        [0, 0, 0],
        [1, 0, 0]]

'''
def winner(current_game):
    for row in game:
        print(row)

        col0 = row[0]
        col1 = row[1]
        col2 = row[2]

        if col0 == col1 == col2:
            print("winner")

winner(game)

This is static style of programming
'''

# Lets try dynamic programming
# logic is compare all the ele of a row to fist ele, if not true, continue iterating.
#

'''
def winner(current_game):

    for row in game:
        print(row)

        not_match = False
        for item in row:
            if item != row[0]:
                not_match = True

        if not not_match:
            print("winner")

winner(game)

#too long
'''
#so


def winner(current_game):
    for row in game:
        print(row)

        if row.count(row[0]) == len(row) and row[0] != 0:
            # we dont want winner if all a zeros in a row, 0 , 0 , 0 is a default start position and not winner state
            # so check for the first ele of row if zero
            print("winner")

winner(game)

'''

#Going one-step further checking the built in libraries in python.org
def winner(current_game):
    for row in game:
        print(row)

        #if row.count(row[0]) == len(row):
           # print("winner") #gosh, put the string in quotes
        if all(row): # all() function returns true if all the elements itered are True. so my row has all zeors, all are equal but not all are true condition satisfied
            print("winner")


winner(game)

#so we dont want to declare winner if all the elements are zeros in a row,
#all(row) function fits perfectly to the case
'''