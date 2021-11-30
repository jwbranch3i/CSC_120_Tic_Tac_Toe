def prnBoard(board):
   for i in range(0, 3):
      print("[", end=" ")
      for j in range(0, 3):
         colSep = "" if j == 2 else " | "
         print(board[i][j] + colSep, end="")
      print(" ]")
      rowSep = "" if i == 2 else "------------"
      print(rowSep)


board = []
row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]
row3 = ["-", "-", "-"]
board.append(row1)
board.append(row2)
board.append(row3)

prnBoard(board)


