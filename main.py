# game start, print empty board

# player x input two digits
# print board with input
# check for win, if no win, player o

# player o input
# print board with input
# check for win, if no win, player x

# game_board = {"00": " ", "01": " ", "02": " ",
#               "10": " ", "11": " ", "12": " ",
#               "20": " ", "21": " ", "22": " "}

game_board = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

# display(board) modeled after printBoard(board) from Chapter 5 of
#       book "Automate the Boring Stuff with Python" by Albert Sweigart.

def display(board):
    print("   0    1    2 ")
    print("0  " + board[0][0] + "  |" + board[0][1] + "  |" + board[0][2])
    print('   ---+---+---')
    print("1  " + board[1][0] + "  |" + board[1][1] + "  |" + board[1][2])
    print('   ---+---+---')
    print("2  " + board[2][0] + "  |" + board[2][1] + "  |" + board[2][2])

display(game_board)


# def x_turn():
#     x_move = input("X's move -- pick a coordinate: ")
#     game_board[x_move] = "X"
#     display(game_board)
#     o_turn()
#
# def o_turn():
#     o_move = input("O's move -- pick a coordinate: ")
#     game_board[o_move] = "O"
#     display(game_board)
#     x_turn()

def player_turn(player):
    row, col = input("{}'s move: ".format(player))
    row, col = int(row), int(col)
    if game_board[row][col] == " ":
        game_board[row][col] = "{}".format(player)
    else:
        print("This coordinate has been taken. Choose another!")
        return player_turn(player)

    display(game_board)

    if player == "X":
        return player_turn("O")
    else:
        return player_turn("X")

print("Player X will go first.\n")
print("""Type in row then column of board with no space.
'00' is top left, '12' is center right, etc.\n""")

for turn in range(9):
    player_turn("X")
