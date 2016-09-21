
import sys

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

def game_start():
    game_board = [[' ', ' ', ' '],
                  [' ', ' ', ' '],
                  [' ', ' ', ' ']]

    print("Player X will go first.\n")
    print("""Type in row then column of board with no space.
    '00' is top left, '12' is center right, etc.\n""")
    display(game_board)
    player_turn("X")

def player_turn(player):
    try:
        row, col = input("{}'s move: ".format(player))
        row, col = int(row), int(col)
    except IndexError:
        print("Try again. Row number then column number (00, 11, 22, etc.)")
        display(game_board)
        player_turn(player)
    if game_board[row][col] == " ":
        game_board[row][col] = "{}".format(player)
    else:
        print("This coordinate has been taken. Choose another!")
        player_turn(player)
    display(game_board)
    win_condition(game_board, row, col, player)
    next_player(player)

def next_player(player):
    if player == "X":
        player_turn("O")
    else:
        player_turn("X")

def has_spaces(game_board):
    for row in game_board:
        for i in row:
            if i == " ":
                return True
    return False

def win_condition(game_board, row, col, player):
    if player == game_board[row][0] == game_board[row][1] == game_board[row][2]:
        win_check(player)
    if player == game_board[0][col] == game_board[1][col] == game_board[2][col]:
        win_check(player)
    if player == game_board[0][0] == game_board[1][1] == game_board[2][2]:
        win_check(player)
    if player == game_board[2][0] == game_board[1][1] == game_board[0][2]:
        win_check(player)
    if has_spaces(game_board) == False:
         print("It's a TIE!")
         play_again()

def win_check(player):
    print("{} wins!".format(player))
    play_again()

def play_again():
    replay = input("Would you like to play again? [y/N] ")
    if replay.lower() == "y":
        game_start()
    else:
        sys.exit()

game_start()
