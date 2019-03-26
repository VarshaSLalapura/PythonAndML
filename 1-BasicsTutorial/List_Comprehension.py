# game_size = 3
#
# # game = []
# # for game in range(game_size):
# #     row = []
# #     for row in range(game_size):
# #         row.append(0)
# game = []
# for i in range(game_size):
#     row = []
#     for i in range(game_size):
#         print(row)
#         row.append(0)
#
#     game.append(row)
#
# print(game)
#
# # List Comprehension
# print([[0 for i in range(game_size)] for i in range((game_size))])
#
# # Dictionary:
#
# # dict1 = {"Key1": 200, "Key2": 400}
# # print(dict1.append("Key3": 500))
#
# # Dictionary comprehension
# data = {k: v for k, v in (('a', 1),('b',2),('c',3))}
# print(data)
#
# d = {n: n**2 for n in range(5)}
# print (d)
#
# # 0 0
# # 1 1
# # 2 4
# # 3 9
# # 4 16
# l = []
# for i in range(5):
#     print(i**2)
#     l.append(i**2)
#
# print(l)
# for idx,val in enumerate(l):
#     print(idx,l[idx])
# print()
#
# # now compact code
# print([i**2 for i in range(5)])
# # more compactness with condition on the for loop
# print([i**2 for i in range(5) if i%2==0])
#
#
# # nested lists:
# my_list = []
#
# for x in [2, 4, 6]:
#     for y in [2, 4, 6]:
#         my_list.append(x * y)
#
# print(my_list)
# print()
# # compact code
# print([x*y for x in range(2,8,2) for y in range(2,8,2)])
# print([[x*y for x in range(2,8,2)] for y in range(2,8,2)])
#


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
print('   0  1  2')
for idx, row in enumerate(game):
    print(idx, row)

print()
l = list(range(3))
l1 = str(l)
s = '  '
p = s.join(l1)
print('l1', type(l1))
print('p', p)

for i in list(range(3)):
    print(i)



