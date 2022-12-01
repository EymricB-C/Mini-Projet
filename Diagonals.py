def newBoard(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        else:
            board.append(row)
    else:
        return board

# displays
def displayBoard(board, n):
    separation = "  " + "--"*(n+1)
    bottom = "    "
    if n >= 10:
        separation += "-"*(n+1)
        bottom += " "
    for i in range(n):
        row = f"{i+1} "
        values = ""
        if n >= 10 and i < 9:
            row += " "
            bottom += " "
        row += "| "
        for j in range(n):
            if n >= 10:
                values += " "
            values += "x " if board[i][j] == 1 else "o " if board[i][j] == 2 else ". "
        row +=values
        bottom += str(i+1) + " "
        print(row)
    else:
        print(separation)
        print(bottom)

def displayScore(score):
    print(f"Current score : {score[0]} vs {score[1]}")

def displays(board, n, score, player):
    print(f"\nPlayer {player}\n")
    displayBoard(board, n)
    displayScore(score)

#Square selection
def possibleSquare(board, n, i, j):
    if i < n and j < n and i >= 0 and j >= 0:
        return True if(board[i][j] == 0) else False
    else:
        print("\nEntrez un carré valide\n")
        return False

def selectSquare(board, n):
    i = input("Entrez la ligne : ")
    j = input("Entrez la colonne : ")
    
    if i.isdecimal() and j.isdecimal():
        i = int(i)-1
        j = int(j)-1
        if possibleSquare(board, n, i, j):
            return [i, j]
        else:
            i = j = 0
    else:
        i = j = 0

#update
def updateBoard(board, player, i, j):
    board[i][j] = player if player in {1, 2} else print("Update Board Error")       

def updateScore(board, n, player, score, i, j):
    result = diagonal(board, n, i, j, player)
    if player in {1, 2}:
        score[player - 1] += result
    else:
        print("Score Update Error")

#win verifier
def again(board, n):
    counter = 0
    for i in range(n):
        row = board[i]
        for j in range(n):
            if row[j] == 0:
                counter += 1
    else:
        if counter > 0:
            return True
        else:
            return False

def win(score):
    if score[0] > score[1] :
        return f"Player 1 have won : {score[0]} vs {score[1]}"
    elif score[0] < score[1]:
        return f"Player 2 have won : {score[0]} vs {score[1]}"
    else:
        return "same score, no winner"

#Diagonal
def diagonal(board, n, i, j, player):
    tempi = i
    tempj = j
    score = 0

    while tempi - 1 >= 0 and tempj - 1 >= 0 and board[tempi-1][tempj-1] == player:
        score += 1
        tempi -= 1
        tempj -= 1
    else:
        tempi = i
        tempj = j

    while tempi + 1 < n and tempj + 1 < n and board[tempi+1][tempj+1] == player:
        score += 1
        tempi += 1
        tempj += 1
    else:
        tempi = i
        tempj = j

    while tempi + 1 < n and tempj -1 >= 0 and board[tempi+1][tempj-1] == player:
        score += 1
        tempi += 1
        tempj -= 1
    else:
        tempi = i
        tempj = j

    while tempi - 1 >= 0 and tempj + 1 < n and board[tempi-1][tempj+1] == player:
        score += 1
        tempi -= 1
        tempj += 1
    else:
        tempi = i
        tempj = j

    if score > 0:
        return (score+1)
    else:
        return score

#Game Total
def diagonals(n):
    score = [0, 0]
    board = newBoard(n)
    player = 1

    displays(board, n, score, player)
    while again(board, n) :
        choosenSquare = selectSquare(board, n)
        if type(choosenSquare) == list:
            updateBoard(board, player, choosenSquare[0], choosenSquare[1])
            updateScore(board, n, player, score, choosenSquare[0], choosenSquare[1])
            player = 3 - player
            displays(board, n, score, player)
    else:
        print(win(score))

def start():
    lengthInput = input("\nHow many rows/columns do you want : ")
    if lengthInput.isdecimal() and int(lengthInput) > 0:
        diagonals(int(lengthInput))
    else:
        start()

start()