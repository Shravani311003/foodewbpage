import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "x"
winner = None
gameRunning = True

def printboard(board):
    print(board[0] + " | " + board[1]  + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4]  + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7]  + " | " + board[8])
    print("---------")
#printboard(board)
def playerInput(board):
    inp = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp <= 9  and board[inp-1] =="-":
        board[inp-1] = current_player
    else:
        print("Oops player is already in that spot!")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] !="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board [5] and board[3] !="-":
        winner = board[0]
        return True
    elif board[6] == board[7] == board[8] and board[6] !="-":
        winner = board[6]
        return True
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !="-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] !="-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] !="-":
        winner = board [0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board [3]
        return True
    
def checkTie(board):
    if "-" not in board:
        printboard(board)
        print("Its a tie!")
        gameRunning = False
def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is{winner}")
        gameRunning = False
        exit()
def switchPlayer():
    global current_player
    if current_player =="x":
        current_player ="o"
    else:
        current_player ="x"

def computer(board):
    while current_player =="o":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] ="o"
            switchPlayer()
    
while gameRunning:
    printboard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
