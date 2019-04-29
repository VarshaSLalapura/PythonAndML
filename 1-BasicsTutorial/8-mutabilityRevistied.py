game = 'This is a game'


def game_board():
    game = 'A game'
    print(game)

print(game)
game_board()
print(game)


print('########')
game1 = '1This is a game'
print(game1)
print(id(game1))
print()

def game_board1():

    game1 = '1A game'
    print(game1)
    print(id(game1))

game_board1()
print(game1)
print(id(game1))

print('########')
game = "I want to play a game"
print(game)
print(id(game))


def game_board():

    global game
    print(id(game))
    game = "A game"
    print(id(game))
    return game


game_board()
print(game)
print(id(game)) # now the id is the id of the function call and game object inside it


print('llllllllllll')

x = 1
def test():
    x = 2
test()
print(x) # 1


x = 1
def test():
    global x
    x = 2
test()
print(x) # 2


x = [1]
def test():
    x = [2]
test()
print(x) #[2] , incorrect, pl check the answer


x = [1]
def test():
    global x
    x = [2]
test()
print(x) #2

# important
x = [1]
def test():
    x[0] = 2
test()
print(x) #2
print()

x = [1]


def test():
    x = [22]
    return x


x = test()
print(x)






























