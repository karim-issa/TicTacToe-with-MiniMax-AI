
board = {1: ' ',2:' ',3:' ',
         4:' ',5:' ',6:' ',
         7:' ',8:' ',9:' '}

PlayerLetter = input("Choose X or O")
PlayerLetter = PlayerLetter.lower()
while PlayerLetter not in ['X','O','x','o']:
    print("Your letter must be X or O! ")
    PlayerLetter = input("Choose X or O")
    PlayerLetter=PlayerLetter.lower()

if PlayerLetter == 'x':
    BotLetter = 'o'
    print("Agent Letter is O!")
    print("Your letter is X")
else:
    BotLetter ='x'
    print("Agent Letter is X!")
    print("Your letter is O")
def printBoard():
    print('\n',board[1],"|",board[2],"|",board[3], "\n",
          board[4],"|",board[5],"|",board[6],"\n",
          board[7],"|",board[8],"|",board[9])

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def checkWin():
        if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
            return True
        elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
            return True
        elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
            return True
        else:
            return False
def checkWinLetter(letter):
        if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
            return True
        elif board[1] == board[5] and board[1] == board[9] and board[1] == letter:
            return True
        elif board[1] == board[4] and board[1] == board[7] and board[1] == letter:
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] == letter:
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] == letter:
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] == letter:
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] == letter:
            return True
        else:
            return False
def InsertLetter(letter,position):
    if board[position] == ' ' and position in [1,2,3,4,5,6,7,8,9]:
        board[position] = letter
        printBoard()
        if checkDraw():
            print("It's a tie")
            exit()
        if checkWin():
            if letter == PlayerLetter:
                print("Player Wins! ")
                exit()
            else:
                print("Bot Wins")
                exit()
    else:
        while board[position] != ' ' or position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            position = int(input("Choose a position between 1 and 9 that isn't taken! : "))
        InsertLetter(position)
def PlayerMove():
    pos = int(input('Choose a position! : '))
    InsertLetter(PlayerLetter,pos)

def BotMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = BotLetter
            score = MiniMax(False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    InsertLetter(BotLetter,bestMove)
def MiniMax(isMaximizing):
    if checkWinLetter(BotLetter):
        return 1
    elif checkWinLetter(PlayerLetter):
        return -1
    elif checkDraw():
        return 0
    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = BotLetter
                score = MiniMax(False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = PlayerLetter
                score = MiniMax(True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore
def RunGame():
    while not checkWin() :
        if PlayerLetter == 'x':
            PlayerMove()
            BotMove()
        else:
            BotMove()
            PlayerMove()

RunGame()