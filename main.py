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


# win_condition = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"], ["00", "10", "20"], ["01", "11", "21"], ["02", "12", "22"]]
# def win():



# x_move = str(input("Your move: "))
#
# if x_move in game_board:
#     game_board = game_board[x_move]
