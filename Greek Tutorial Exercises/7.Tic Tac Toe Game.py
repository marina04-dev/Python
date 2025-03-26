# Tic Tac Toe Game: Without Functions (Lesson 7: Exercise 6.1-6.5)
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player = "O"

for _ in range(9):
    # Board Printing
    print("  +---+---+---+")
    print(str(2) + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("  +---+---+---+")
    print(str(1) + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("  +---+---+---+")
    print(str(0) + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("  +---+---+---+")
    print("    0   1   2")

    # Choose Next Player
    if player == "X":
        player = "O"
    else:
        player = "X"

    # User Input
    while True:
        print("Player " + player + " plays! ")
        row = int(input("Enter the number of a row (0-2): "))
        col = int(input("Enter the number of a column (0-2): "))
        if row < 0 or row > 2:
            print("Row out of Bounds (0-2). ")
            continue
        elif col < 0 or col > 2:
            print("Column out of Bounds (0-2). ")
            continue
        elif board[row][col]!=" ":
            print("Pick an Empty Box")
            continue
        else:
            board[row][col]=player
            break

    # Winner Checking
    winner = False
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2]) and board[0][0] != " ":
        winner = player
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) and board[1][0] != " ":
        winner = player
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]) and board[2][0] != " ":
        winner = player
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0]) and board[0][0] != " ":
        winner = player
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1]) and board[0][1] != " ":
        winner = player
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2]) and board[0][2] != " ":
        winner = player
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != " ":
        winner = player
    elif (board[2][0] == board[1][1] and board[1][1] == board[0][2]) and board[2][0] != " ":
        winner = player

    if winner:
        print("+---+---+---+")
        print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
        print("+---+---+---+")
        print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
        print("+---+---+---+")
        print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
        print("+---+---+---+")
        print("Player " + player + "won! ")
        break

else:
    print("+---+---+---+")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("+---+---+---+")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("+---+---+---+")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("+---+---+---+")
    print("Draw! ")
