"""
Name: Tyler McCormack
lab10.py
"""

def main():
    #pass
    play()

def board():
    positionlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return positionlist

def display(positionlist):
    print("-" * 13)
    acc = 0
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(positionlist[acc], end=" | ")
            acc += 1
        print("\n" + "-" * 13)


def fillspot(board, spot, marker):
    board[spot- 1] = marker


def legalspot(board, spot):
    if (board[spot- 1] == "X" or board[spot-1] == "O") or (spot<1 or spot>9):
        return False
    else:
        return True


def gamewon(board):
    winCon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for condition in winCon:
        accX = 0
        accY = 0
        for spot in condition:
            if board[spot-1] == "X":
                accX += 1
            elif board[spot-1] == "O":
                accY += 1
        if accX == 3:
            #print("xwins")
            return "xwins"

        if accY == 3:
            #print("ywins")
            return "ywins"


def gameover(board, turncount):
    if (gamewon(board) == "xwins" or gamewon(board) == "ywins") or (turncount > 9):
        return True
    else: return False

def play():
    positionlist = board()
    turncount = 0
    while not gameover(positionlist, turncount):
        display(positionlist)
        if turncount == 0 or turncount % 2 == 0:
            print("It is X's turn.")
            marker = "X"
        else:
            print("It is O's turn.")
            marker = "O"
        spot = eval(input("Enter the spot you would like to place your mark"))
        if legalspot(positionlist, spot):
            fillspot(positionlist, spot, marker)
        else:
            print("Turn not legal. Turn forfeited.")
        turncount += 1
        if gamewon(positionlist) == "xwins":
            print("X Wins!")
            break
        if gamewon(positionlist) == "ywins":
            print("Y Wins!")
            break
        if turncount >= 9:
            print("It's a tie")


main()
