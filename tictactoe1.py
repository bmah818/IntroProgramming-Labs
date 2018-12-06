# CMPT 120 Intro to Programming
# Lab #7 
# Author: Bryan Mah
# Created: 2018/11/08
symbol = [ " ", "x", "o" ]

def printRow(row):
    print("|", end="")
    for cell in row:
        print(" " + symbol[cell] + " |", end="")
def printBoard(board):
    for i in range(3):
def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
        # if so, set it to the player number
    pass
def getPlayerMove():
    input("") # prompt the user separately for the row and column numbers
    return (0,0) # then return that row and column instead of (0,0)
def hasBlanks(board):
    # for each row in the board...
        # for each square in the row...
            # check whether the square is blank
    return True     
def main():
    board = [] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
main()
