import itertools

player_choice = itertools.cycle([1, 2])
for i in range(5):
    player = next(player_choice)

    print(player)


# list comprehension:
game = [[0 for x in range(3)] for x in range(3)]
print(game)
for row in game:
    print(row)


player = itertools.cycle([1,2])
for i in range(5):
    print(next(player)) # here player is the iterator, range(5) gives a sequence of iterable

# mutability:
# 1
x = [1]
def game():
    x[0] = 2

game()
print('x = ', x)
# 2
y = 1
def game1():
    y = 2

game1()
print(y)
# 3


def game2(zin=z):
    z = 2


play = True
while play:
    z = 1
    game2(z)
    print('z= ', z)
    play = False
