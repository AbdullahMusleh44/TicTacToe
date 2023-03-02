import random

print("Tic Tac Toe")

numbers = [1,2,3,4,5,6,7,8,9]
board = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
         ]
rows = 3
columns = 3



def printBoard(): #printing the tic tac toe board
    for i in range(rows):
        print("\n+---+---+---+")
        print("|", end= "")
        for j in range(columns):
            print("", board[i][j], end =" |")
    print("\n+---+---+---+")

def editBoard(loc, XorO):
    loc = loc - 1 #set back location measure by 1

    if loc == 0: #which location on board
        board[0][0] = XorO #modify board with x or o
    elif loc == 1:
        board[0][1] = XorO
    elif loc == 2:
        board[0][2] = XorO
    elif loc == 3:
        board[1][0] = XorO
    elif loc == 4:
        board[1][1] = XorO
    elif loc == 5:
        board[1][2] = XorO
    elif loc == 6:
        board[2][0] = XorO
    elif loc == 7:
        board[2][1] = XorO
    elif loc == 8:
        board[2][2] = XorO

def decideWinner(board): #all possible wins
    # straight horizontal win
    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        print("X won!")
        return "X"
    elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        print("O won!")
        return "O"
    elif (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
        print("X won!")
        return "X"
    elif (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
        print("O won!")
        return "O"
    elif (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
        print("X won!")
        return "X"
    elif (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        print("O won!")
        return "O"

    # straight vertical win
    if (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        print("X won!")
        return "X"
    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
        print("O won!")
        return "O"
    elif (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
        print("X won!")
        return "X"
    elif (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
        print("O won!")
        return "O"
    elif (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        print("X won!")
        return "X"
    elif (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        print("O won!")
        return "O"

    #  diagonal win
    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        print("X won!")
        return "X"
    elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        print("O won!")
        return "O"
    elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        print("X won!")
        return "X"
    elif (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        print("O won!")
        return "O"
    else:
        return "N"

turnCounter = 0
endLoop = False

while endLoop == False:
    if (turnCounter % 2 == 0): #players turn
        printBoard()
        chosenNumber = int(input("Choose a number by typing it!"))
        if 1 <= chosenNumber <= 9:
            editBoard(chosenNumber, 'X')
            try:
                numbers.remove(chosenNumber)
            except ValueError:
                editBoard(chosenNumber, 'O')
                print("This number already chosen, try again")
                turnCounter = turnCounter + 1
        else:
            print("Try another number")
        turnCounter = turnCounter + 1
    else: #computers turn
        while True:
            try:
                computerChoice = random.choice(numbers)
            except IndexError:
                print("Game over, its a draw!")
                exit()
            print("Computer choice: ", computerChoice)
            if computerChoice in numbers:
                editBoard(computerChoice, 'O')
                numbers.remove(computerChoice)
                turnCounter = turnCounter + 1
                break

    winner = decideWinner(board) #decide the winner
    if winner != "N":
        print("\nGame over!")
        break
