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

def displayBoard(board, n):
    separation = "  " + "--"*(n+1)
    bottom = "    "
    for i in range(n):
        row = f"{i+1} | "
        values = ""
        for j in range(n):
            if board[i][j] == 1:
                values += 'x '
            elif board[i][j] == 2:
                values += 'o '
            else:
                values += '. '
        row +=values
        print(row)
        bottom += str(i+1) + " "
    else:
        print(separation)
        print(bottom)

def displayScore(score):
    print(f"Current score : {score[0]} vs {score[1]}")

def possibleSquare(board, n, i, j):
    if i < n and j < n:
        return True if(board[i][j] == 0) else False
    else:
        print("\nEntrez un carré valide\n")
        return False

def selectSquare(board, n):
    i = int(input("Entrez la ligne : ")) - 1
    j = int(input("Entrez la colonne : ")) - 1
    
    if possibleSquare(board, n, i, j):
        return [i, j]
    else:
        i = j = 0

def updateBoard(board, player, i, j):
    board[i][j] = player if player in {1, 2} else print("Update Board Error")       

def diagonal(board, n, i, j, player):
    tempi = i
    tempj = j
    score = 0
    
    
    
    while board[tempi-1][tempj-1] == player:
        score += 1
        tempi -= 1
        tempj -= 1
    else:
        tempi = i
        tempj = j
        while board[tempi+1][tempj+1] == player:
            score += 1
            tempi += 1
            tempj += 1
        else:
            tempi = i
            tempj = j
            while board[tempi+1][tempj-1] == player:
                score += 1
                tempi += 1
                tempj -= 1
            else:
                tempi = i
                tempj = j
                while board[tempi-1][tempj+1] == player:
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

def again(board, n):
    for i in range(n):
        return False if any(board[i]) else True


def updateScore(board, n, player, score, i, j):
    result = diagonal(board, n, i, j, player)
    if player in {1, 2}:
        score[player - 1] += result
    else:
        print("Score Update Error")

def win(score):
    print(score)

def displays(board, n, score, player):
    print(f"\nPlayer {player}\n")
    displayBoard(board, n)
    displayScore(score)

def diagonals(n):
    score = [0, 0]
    board = newBoard(n)
    player = 1

    displays(board, n, score, player)
    while again(board, n) :
        choosenSquare = selectSquare(board, n)
        if choosenSquare == None:
            choosenSquare = selectSquare(board, n)

        updateBoard(board, player, choosenSquare[0], choosenSquare[1])
        updateScore(board, n, player, score, choosenSquare[0], choosenSquare[1])

        player = 3 - player

        displays(board, n, score, player)
    else:
        win(score)

diagonals(4)