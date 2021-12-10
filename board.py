from datetime import datetime
import gameDB

# ---------------------------------------------
# function to create board for new game
# ---------------------------------------------
def makeBoard():
   board = []
   row1 = ["-", "-", "-"]
   row2 = ["-", "-", "-"]
   row3 = ["-", "-", "-"]
   board.append(row1)
   board.append(row2)
   board.append(row3)
   return(board)

# ---------------------------------------------
# Function to print the current status of the Tic-Tac-Toe board
# ---------------------------------------------
def prnBoard(board):
    for i in range(0, 3):
        print("[", end=" ")
        for j in range(0, 3):
            colSep = "" if j == 2 else " | "
            print(board[i][j] + colSep, end="")
        print(" ]")
        rowSep = "" if i == 2 else "------------"
        print(rowSep)


# ---------------------------------------------
# Function to check if space is free
# ---------------------------------------------
def isFree(row, col, board):
    free = False
    if isValid(row, col):
        if board[row-1][col-1] == "-":
            free = True
    return free

# ---------------------------------------------
# Function to check if selection is valid
# ---------------------------------------------
def isValid(row, col):
    good = True
    if (row < 1 or row > 3) or (col < 1 or col > 3):
        good = False
    return good

# ---------------------------------------------
# Function to set marker on board
# ---------------------------------------------
def setMarker(row, col, board, marker):
    board[row-1][col-1] = marker

# ---------------------------------------------
# Function to check for a winner
# ---------------------------------------------
def isWinner(board):
    winner = "-"
    for i in range(0, 3):
        line = board[i][0].strip() + board[i][1].strip() + board[i][2].strip()
        if line == "OOO":
            winner = "O"
        elif line == "XXX":
            winner = "X"

    for i in range(0, 3):
        line = board[0][i].strip() + board[1][i].strip() + board[2][i].strip()
        if line == "OOO":
            winner = "O"
        elif line == "XXX":
            winner = "X"

    line = board[0][0].strip() + board[1][1].strip() + board[2][2].strip()
    if line == "OOO":
        winner = "O"
    elif line == "XXX":
        winner = "X"

    line = board[2][0].strip() + board[1][1].strip() + board[0][2].strip()
    if line == "OOO":
        winner = "O"
    elif line == "XXX":
        winner = "X"

    return winner

# ---------------------------------------------
# compress board
# ---------------------------------------------
def compressBoard(board):
   compressed = ""
   for i in range(0,3):
      for j in range(0, 3):
         compressed = compressed + board[i][j]

   return (compressed)

# ---------------------------------------------
# decompress board
# ---------------------------------------------
def deCompressBoard(compressedBoard):
   board = makeBoard()
   k = 0
   for i in range(0, 3):
      for j in range(0, 3):
         board[i][j] = compressedBoard[k]
         k = k + 1
   return (board)

# ---------------------------------------------
# ---------------------------------------------
# Main program for Tic-Tac-Toe
# ---------------------------------------------
# ---------------------------------------------
print("\n\nWelcome to my Tic-Tac-Toe game")
playMore = True
gameDB.dbSetup()
while(playMore):

   board = makeBoard()

   print("\nMenu----------------------")
   print("1. Play")
   print("2. Print Game History")
   print("3. Clear History")
   print("4. Exit")
   choice = int(input("Enter Selection:"))

   if choice == 4:
      playMore = False
   elif choice == 1:
      notDone = True
      activePlayer = "1"
      print("Player 1 is 'O', Player 2 is 'X'\n")

      while(notDone):
         prnBoard(board)
         print("Player " + activePlayer + " it's your turn")
         selectedRow = int(input("Enter row (1-3): "))
         selectedCol = int(input("Enter column (1-3): "))

         validChoice = isFree(selectedRow, selectedCol, board)
         if validChoice:
            marker = "O"
            if activePlayer == "2":
                  marker = "X"

            setMarker(selectedRow, selectedCol, board, marker)
            winner = isWinner(board)
            if winner == "-":
                  if activePlayer == "2":
                     activePlayer = "1"
                  else:
                     activePlayer = "2"
            else:
                  notDone = False

         else:
            print("*** Invalid selection. ***")

      prnBoard(board)
      print("Player " + activePlayer + " is the winner!!")

      gameDay = datetime.now()
      gDate = gameDay.strftime("%m/%d/%Y %H:%M:%S")
      gWinner = marker
      gBoard = compressBoard(board)
      gameDB.dbSave(gDate, gWinner, gBoard)
   elif choice == 2:
      numberGames = gameDB.ctGames("TOTAL")
      numOGames = gameDB.ctGames("O")
      numXGames = gameDB.ctGames("X")

      print ("\nGame History")
      print ("------------")
      print (str(numberGames) + " Total games played.")
      print (str(numOGames) + " games won by player 1 'O'")
      print (str(numXGames) + " games won by player 2 'X'")
      print (str(numberGames - (numOGames + numXGames)) + " Tie games")
      print ("\nGame List")
      print ("------------")

      gameHistory = gameDB.getGames()
      ct = 1
      for i in gameHistory:
         if (i[1] == "O"):
            tPlayer = "Winner Player 1 'O'"
         elif (i[1] == "X"):
            tPlayer = "Winner Player 2 'X'"
         else:
            tPlayer = "Tie Game"
         print("Game " + str(ct) + " - " + i[0] + " " + tPlayer)

         tboard = deCompressBoard(i[2])
         prnBoard(tboard)
         ct = ct + 1


   elif choice == 3:
      gameDB.clearHistory()


print("Thank you for playing\n")
