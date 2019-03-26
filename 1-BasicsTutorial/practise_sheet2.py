from typing import List

game = [[1, 0, 2],
        [0, 2, 0],
        [2, 0, 1]]  # type: List[List[int]]


def dia_winner(current_game, left_to_right=True):
    check = []
    i = len(game[0]) - 1
    if left_to_right:

        for row in game:
           check.append(row[i])
           i+=1
           print(check)
    else:
        for row in game:
           check.append(row[i])
           i-=1
           print(check)


# d_winner_is = dia_winner(current_game=game, left_to_right=False)

# we want this logic
# game[0][0]==game[1][1]==game[2][2], then winner
"""
row = range(len(game))
for i in row:
    print(i)

print()
col = reversed(range(len(game[0])))
for j in col:
    print(j)

for i in row:
    for j in col:
        print('&&&&&&')
        print(i,j)

for row in game:
    print(row)

"""
game = [[1, 0, 2],
        [0, 1, 0],
        [2, 0, 1]]

# left to right , access the diagonal items and put them in the list called diags
diags = []
for idx in range(len(game)):
    print(game[idx][idx])
    diags.append(game[idx][idx])

print(diags)
print()
# the ncheck if the list is having all the elements as the same first elem
if(diags.count(diags[0]) == len(diags)) and diags[0]!= 0:
    print("winner!")

# now going right to left:
# for that we need a logic to access the reversed indices:
print()
row = list(range(len(game)))
print(row)

for i in row:
    print(i)

print()
col = list(reversed(range(len(game))))
print(col)

for idx in row:
    print(idx,col[idx])


