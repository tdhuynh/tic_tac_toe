# game start, print empty board

# player x input two digits
# print board with input
# check for win, if no win, player o

# player o input
# print board with input
# check for win, if no win, player x

game_board = [['X', 'X', 'X'],
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

# still working on win conditions
# def win_check():
#      for condition in win_conditions:
#          if all(game_board[condition] == "X" for coord in condition):
#              print("X wins!")
#          elif all(game_board[condition] == "O" for coord in condition):
#              print("O wins!")
#          else:
#              continue

def player_turn(player):
    try:
        row, col = input("{}'s move: ".format(player))
        row, col = int(row), int(col)
    except ValueError:
        print("Try again. Row number then column number (00, 11, 22, etc.)")
        display(game_board)
        return player_turn(player)

    if game_board[row][col] == " ":
        game_board[row][col] = "{}".format(player)
    else:
        print("This coordinate has been taken. Choose another!")
        return player_turn(player)

    display(game_board)
#    win_check(player)
    if player == "X":
        return player_turn("O")
    else:
        return player_turn("X")

print("Player X will go first.\n")
print("""Type in row then column of board with no space.
'00' is top left, '12' is center right, etc.\n""")

display(game_board)
player_turn("X")
