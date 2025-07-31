def initialize_board():
    grid = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    return grid

def display_board(board):
    for row in board:
        for element in row:
            print(f' {element}   |' , end= '  ')
        print()

def make_move(board, position, player):
    if position >= 0 or position <= 9:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == position:
                        board[i][j] = player
                        return
            print("invald postion")
            return

def check_winner(board):
    # check rows
    for i in range (3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
    # check columns
    if board[0][0] == board[1][0] == board[2][0]:
        return True
    if board[0][1] == board[1][1] == board[2][1]:
        return True
    if board[0][2] == board[1][2] == board[2][2]:
        return True
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'x' and board[i][j] != 'o':
                return False
    return True

def switch_player(current_player):
    if current_player == 'x':
        return 'o'
    return 'x'

def gameplay():
    board = initialize_board()
    display_board(board)
    player = input("enter x or o ? ")
    while True:
        position = int(input(f"PLAYER {player} Enter Number from 1-9 : "))
        make_move(board, position, player)
        display_board(board)
        print("*" * 30)
        if check_winner(board):
            print(f'{player} is Wins')
            return
        if is_board_full(board):
            print('Draw')
            return
        player = switch_player(player)

if __name__ == '__main__':
    gameplay()