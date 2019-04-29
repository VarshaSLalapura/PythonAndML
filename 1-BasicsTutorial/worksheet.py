# from colorama import init, Style, Fore
# init()


# print(Fore.RED + 'some red text')

game = [[0, 0, 1],
        [0, 0, 1],
        [1, 2, 0]]

check = []

for row in game:
    check.append(row[0])
print(check)

# for idx,row in enumerate(game):
#     print(idx,row)
#     coloured_row = ""
#     for item in row:
#
#         if item == 0:
#             coloured_row += "   "
#         elif item == 1:
#             coloured_row += Fore.MAGENTA + " X " + Style.RESET_ALL
#         elif item == 2:
#             coloured_row += Fore.GREEN + " 0 " + Style.RESET_ALL
#     print(idx, coloured_row)
#
# for idx, row in enumerate(game):
#     # print(idx, row)
#     coloured_row = ""
#     for item in row:
#         if item == 0:
#             coloured_row += "   "
#         elif item == 1:
#             coloured_row += Fore.GREEN + " X " + Style.RESET_ALL
#         elif item == 2:
#             coloured_row += Fore.MAGENTA + " 0 " + Style.RESET_ALL
#     print(idx, coloured_row)
#
#
# import this