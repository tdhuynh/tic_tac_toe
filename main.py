# game start, print empty board

# player x input two digits
# print board with input
# check for win, if no win, player o

# player o input
# print board with input
# check for win, if no win, player x


# board inspiration from book ""
game_board = {"00": " ", "01": " ", "02": " ",
              "10": " ", "11": " ", "12": " ",
              "20": " ", "21": " ", "22": " "}

def display(board):
    print("   0    1    2 ")
    print("0  " + board['00'] + "  |" + board['01'] + "  |" + board['02'])
    print('   ---+---+---')
    print("1  " + board['10'] + "  |" + board['11'] + "  |" + board['12'])
    print('   ---+---+---')
    print("2  " + board['20'] + "  |" + board['21'] + "  |" + board['22'])

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
    player_move = input("{}'s move -- pick a coordinate: ".format(player.upper()))
    game_board[player_move] = "{}".format(player.upper())
    display(game_board)
    if player.upper() == "X":
        player = "O"
        return player_turn(player)
    else:
        player = "X"
        return player_turn(player)



print("Player X will go first.")

while True:
    player_turn("X")
