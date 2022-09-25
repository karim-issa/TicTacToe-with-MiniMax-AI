from tkinter import *

root = Tk()
root.geometry("300x500")
root.title("TIC TAC TOE")

head = Label(root,text="TIC-TAC-TOE",fg="forestgreen",bg="light cyan",font=("Arial",20,"italic"))
head.pack()

p1_name = ""
p2_name = "Agent"
START = False

board={1: ' ', 2: ' ', 3: ' ',
       4: ' ', 5: ' ', 6: ' ',
       7: ' ', 8: ' ', 9: ' '}

def WinCheck(g_ltr):
    if b1['text'] == g_ltr and b2['text'] == g_ltr and b3['text'] == g_ltr:
        b1['bg'] = "light green";
        b2['bg'] = "light green";
        b3['bg'] = "light green"
        return "p1"
    elif b4['text'] == g_ltr and b5['text'] == g_ltr and b6['text'] == g_ltr:
        b4['bg'] = "light green";
        b5['bg'] = "light green";
        b6['bg'] = "light green"
        return "p1"
    elif b7['text'] == g_ltr and b8['text'] == g_ltr and b9['text'] == g_ltr:
        b7['bg'] = "light green";
        b8['bg'] = "light green";
        b9['bg'] = "light green"
        return "p1"
    elif b1['text'] == g_ltr and b4['text'] == g_ltr and b7['text'] == g_ltr:
        b1['bg'] = "light green";
        b4['bg'] = "light green";
        b7['bg'] = "light green"
        return "p1"
    elif b2['text'] == g_ltr and b5['text'] == g_ltr and b8['text'] == g_ltr:
        b2['bg'] = "light green";
        b5['bg'] = "light green";
        b8['bg'] = "light green"
        return "p1"
    elif b3['text'] == g_ltr and b6['text'] == g_ltr and b9['text'] == g_ltr:
        b3['bg'] = "light green";
        b6['bg'] = "light green";
        b9['bg'] = "light green"
        return "p1"
    elif b1['text'] == g_ltr and b5['text'] == g_ltr and b9['text'] == g_ltr:
        b1['bg'] = "light green";
        b5['bg'] = "light green";
        b9['bg'] = "light green"
        return "p1"
    elif b3['text'] == g_ltr and b5['text'] == g_ltr and b7['text'] == g_ltr:
        b3['bg'] = "light green";
        b5['bg'] = "light green";
        b7['bg'] = "light green"
        return "p1"

    elif (b1['text'] != "" and b2['text'] != "" and b3['text'] != "" and
          b4['text'] != "" and b5['text'] != "" and b6['text'] != "" and
          b7['text'] != "" and b8['text'] != "" and b9['text'] != ""):
        return "tie"

    else:
        return False



def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = "O"
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    return

def minimax(board, isMaximizing):
    if WinCheck("O"):
        return 1
    elif WinCheck("X"):
        return -1
    elif checkDraw():
        return 0
    if isMaximizing:
        bestScore=-800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = "O"
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore=800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = "X"
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

def Start():
    global p1_name, p2_name, START
    P1 = p1.get()
    P2 = "Agent"
    if P1.split() == []:
        text = "Enter Player 1 Name"
        turn.place(x=50,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    elif P2.split() == []:
        turn.place(x=50,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    elif P1.split() == P2.split():
        text = "Enter Different Player Names"
        turn.place(x=25,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    else:
        p1_name = P1
        p2_name = P2
        p1['font'] = ("Arial",8,"bold")
        p1['state']=DISABLED

        start.place(x=1000,y=1000)
        turn['text'] = "{}{} Turn".format(p1_name,"'s")
        turn['fg'] = "blue"
        turn['font'] = ("Ubuntu",20,"bold")
        turn.place(x=50,y=425)
        START = True

def DisableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = DISABLED
def EnableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = NORMAL
def BtnClick(button):
    global START,p1_name,p2_name
    if START == True:
        if button['text'] == "":
            if turn['text'] == "{}{} Turn".format(p1_name,"'s"):
                button['text'] = "O"
                turn['text'] = "{}{} Turn".format(p2_name,"'s")
            else:
                button['text'] = "X"
                turn['text'] = "{}{} Turn".format(p1_name,"'s")

        check = WinCheck()
        if check != False:
            restart.place(x=105,y=470)
            START = False
            if check=="p1":
                text = "{} Wins".format(p1_name)
                buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
                Remove = []
                for i in range(9):
                    if buttons[i]['bg'] == "light green":
                        Remove.append(buttons[i])
            elif check=="p2":
                text = "{} Wins".format(p2_name)
                buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
                Remove = []
                for i in range(9):
                    if buttons[i]['bg'] == "light blue":
                        Remove.append(buttons[i])
            else:
                text = "It is a tie !"
            turn['fg'] = "forestgreen"
            turn['text'] = text

            if check == "p1" or check == "p2":
                for i in range(len(Remove)):
                    buttons.remove(Remove[i])
                DisableButtons(buttons)

def Restart():
    Buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    EnableButtons([p1])
    EnableButtons(Buttons)
    restart.place(x=1000,y=1000)
    for a in range(len(Buttons)):
        Buttons[a]['text'] = ""
        Buttons[a]['bg'] = "SystemButtonFace"
    turn['text'] = ""
    start.place(x=107,y=410)
    p1['font'] = "TkTextFont"

Label(root,text="Player 1 :",fg="brown",font=("Courier",10,"bold")).place(x=0,y=50)
p1 = Entry(root)
p1.place(x=90,y=52)

start = Button(root,text="START",bg="gray90",fg="green",font=("Ubuntu",15,"bold"),command=Start)
start.place(x=107,y=410)

turn = Label(root,text="",font=("Ubuntu",15,"normal"))
turn.place(x=50,y=455)

###################################

b1 = Button(root,width=13,height=6)
b1.place(x=0,y=100)

b2 = Button(root,width=13,height=6)
b2.place(x=100,y=100)

b3 = Button(root,width=13,height=6)
b3.place(x=200,y=100)

b4 = Button(root,width=13,height=6)
b4.place(x=0,y=200)

b5 = Button(root,width=13,height=6)
b5.place(x=100,y=200)

b6 = Button(root,width=13,height=6)
b6.place(x=200,y=200)

b7 = Button(root,width=13,height=6)
b7.place(x=0,y=300)

b8 = Button(root,width=13,height=6)
b8.place(x=100,y=300)

b9 = Button(root,width=13,height=6)
b9.place(x=200,y=300)

###################################

restart = Button(root,text="Restart",fg="blue",bg="aquamarine",width = 10,height=1,font=("Courier",10,"bold"))
##restart.place(x=105,y=470)
restart.place(x=1000,y=1000)

root.mainloop()