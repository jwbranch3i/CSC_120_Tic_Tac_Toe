# Function to print the current status of the Tic-Tac-Toe board
#---------------------------------------------
def prnBoard(board):
   for i in range(0, 3):
      print("[", end=" ")
      for j in range(0, 3):
         colSep = "" if j == 2 else " | "
         print(board[i][j] + colSep, end="")
      print(" ]")
      rowSep = "" if i == 2 else "------------"
      print(rowSep)



# Function to check if space is free
def isFree(row, col, board):
   free = False
   if isValid(row, col):
      if board[row-1][col-1] == "-":
         free = True
   return free      

# Function to check if selection is valid
def isValid(row, col):
   good = True
   if ((row-1)<1 or (row-1)>3) or ((col-1)<1 or (col-1)):
      good = False
   return good

# Function to set marker on board
def setMarker(row, col,board):
   board[row-1][col-1]

# Function to check for a winner
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

# Main program for Tic-Tac-Toe
print("Thanks for playing Tic-Tac-Toe")

# create board for new game
board = []
row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]
row3 = ["-", "-", "-"]
board.append(row1)
board.append(row2)
board.append(row3)

notDone = True 
activePlayer = "1"
while(notDone):
   prnBoard(board)
   print("Player " + activePlayer + " it's your turn")
   selectedRow = input("Enter row (1-3): ")
   selectedCol = input("Enter column (1-3):")

   validChoice = isFree(selectedRow, selectedCol, board)
   if validChoice:
      marker = " O "
      if activePlayer == "2":
         marker = " X"

      setMarker(selectedRow, selectedCol, board)
   else:
      print("Invalid selection.")



   notDone = False





