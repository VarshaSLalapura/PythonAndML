game = [[1, 0, 1],
        [0, 1, 0],
        [0, 0, 1]]

# we want g[0][0] == g[1][1] == g[2][2]

diag = []

print(range(len(game)))
print(list(range(len(game))))
print()
for idx in range(len(game)):
    diag.append(game[idx][idx])

print(diag)

# now we want g[0][2] , g[1][1], g[2][0]

# first make the col index in reverse order
# i.e 2, 1, 0
print() #2
print(reversed(range(len(game[0]))))
for i in list(reversed(range(len(game[0])))):
    print(i)

print() #3

# now
# given the list of reversed indices,
# how to associate the index , value pair, not enumerate, since that is for forward order

col = list(reversed(range(len(game[0]))))
# col = [2, 1, 0]
row = range(len(game))
# row = [0, 1, 2]
# so associate 0,col[0], 1,col[1], 2,col[2]
# to get g[0][2], g[1][1], g[2][0]

for idx in row:
    print(idx,col[idx])

# now now now, this is long
# we can use the built in function rather!  ====> zip
print()
zipped = zip(row,col)
print(zipped)
for i in zipped:
    print(i)

for row,col in zip(row,col):
    print(row,col)

print()

# we could do it lot better
diags_1 = []
diags_2 = []

for row,col in enumerate(reversed(range(len(game[0])))):
    print(row,col)
    diags_1.append(game[col][row])
    diags_2.append(game[row][col])

print(diags_1)
print(diags_2)



