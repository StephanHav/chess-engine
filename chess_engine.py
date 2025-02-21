import numpy as np

def generate_board():

    #Initialise 8x8 Matrix of strings
    board = [["" for i in range(9)] for i in range(9)]
    counter = 8
    
    #Initialise Teams (Black/White)
    for i in range(9):
        if i == 0 or i ==1:
            for j in range(8):
                board[i][j] = 'b'

        if i == 6 or i == 7:
            for j in range(8):
                board[i][j] = 'w'

        if i == 1 or i == 6:
            for j in range(8):
                board[i][j] = board[i][j] + 'P'

        if i == 0 or i == 7:
            for j in range(8):
                if j == 0 or j == 7:
                    board[i][j] = board[i][j] + 'R'

                if j == 1 or j == 6:
                    board[i][j] = board[i][j] + 'N'

                if j == 2 or j == 5:
                    board[i][j] = board[i][j] + 'B'
                
                if j == 3:
                    board[i][j] = board[i][j] + 'Q'

                if j == 4:
                    board[i][j] = board[i][j] + 'K'
        
        if i == 8:
            board[i] = [' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', '']
        
        for j in range(9):
            if j == 8 and i != 8:
                board[i][j] = ' ' + f'{counter}'
                counter -= 1

    return board

def legal_moves_white(board):
    
    moves = []
    for i in range(8):
        for j in range(8):

            #White Pawn
            if board[i][j] == 'wP':

                #Check if on starting position 
                if i == 6 and board[i-2][j] == '' and board[i-1][j] == '':
                    moves.append(f'{board[8][j]}{board[4][8]}')

                #1-step forward
                if board[i-1][j] == '':
                    moves.append(f'{board[8][j]}{board[i-1][8]}')
                
                #Take left
                if  board[i-1][j-1].startswith('b'):
                    moves.append(f'{board[8][j-1]}{board[i-1][8]}')

                #Take right
                if  board[i-1][j+1].startswith('b'):
                    moves.append(f'{board[8][j-1]}{board[i-1][8]}')
                
                #TODO: Promotion

                #TODO: En passant

            #White knight
            if board[i][j] == 'wN':
                print("knight here")

    moves = [move.replace(" ", "") for move in moves]

    return moves

def legal_moves_black(board):
    
    moves = []
    for i in range(8):
        for j in range(8):

            #White Pawn
            if board[i][j] == 'bP':

                #Check if on starting position 
                if i == 1 and board[i+2][j] == '' and board[i+1][j] == '':
                    moves.append(f'{board[8][j]}{board[5][8]}')

                #1-step forward
                if board[i+1][j] == '':
                    moves.append(f'{board[8][j]}{board[i+1][8]}')
                
                #Take left
                if  board[i+1][j+1].startswith('w'):
                    moves.append(f'{board[8][j+1]}{board[i+1][8]}')

                #Take right
                if  board[i+1][j-1].startswith('w'):
                    moves.append(f'{board[8][j-1]}{board[i+1][8]}')
                
                #TODO: Promotion

                #TODO: En passant

            #White knight
            if board[i][j] == 'bN':
                print("knight here")

    moves = [move.replace(" ", "") for move in moves]

    return moves

def pick_move():
    move = ''
    return move

def read_opponent_move():
    move = ''
    return

#Take in matrix representing board and print to STDOUT
def print_nice(board):
    for row in board:
        for i, square in enumerate(row):
            if square == '':
                row[i] = '  '
                
        print(row, '\n')

if __name__ == "__main__":

    print("Welcome to \n")
    print("_________ .__                           ________                   __                                      ._______________  _______  _______   ")
    print("\_   ___ \|  |__   ____   ______ ______ \______ \   ____   _______/  |________  ____ ___.__. ___________   |   ____/\   _  \ \   _  \ \   _  \  ")
    print("/    \  \/|  |  \_/ __ \ /  ___//  ___/  |    |  \_/ __ \ /  ___/\   __\_  __ \/  _ \   |  |/ __ \_  __ \  |____  \ /  /_\  \/  /_\  \/  /_\  \ ")
    print("\     \___|   Y  \  ___/ \___ \ \___ \   |    `   \  ___/ \___ \  |  |  |  | \(  <_> )___  \  ___/|  | \/  /       \   \_/   \  \_/   \  \_/   \ ")
    print(" \______  /___|  /\___  >____  >____  > /_______  /\___  >____  > |__|  |__|   \____// ____|\___  >__|    /______  / \_____  /\_____  /\_____  /")
    print("        \/     \/     \/     \/     \/          \/     \/     \/                     \/         \/               \/        \/       \/       \/ \n")
 
    #print(legal_moves_white(generate_board()))
    print_nice(generate_board())