import sqlite3

#-------------------------------------
# Setup database
#-------------------------------------
def dbSetup():
   db = sqlite3.connect("TicTacToe.db")
   db.execute("CREATE TABLE IF NOT EXISTS games (\
      gameDateTime TEXT,\
      winner TEXT,\
      board TEXT)")
   db.close()


#-------------------------------------
# Save game date and time
#-------------------------------------
def dbSave(gDateTime, gWinner, gBoard):
   sql = """INSERT INTO games (gameDateTime, winner, board) VALUES ( ?, ?, ?);"""
   inData = (gDateTime, gWinner, gBoard)

   db = sqlite3.connect("TicTacToe.db")
   cursor = db.cursor()

   cursor.execute(sql, inData)

   cursor.close()
   db.commit()             
   db.close


#-------------------------------------
#count number of games
#-------------------------------------
def ctGames(item):
   sql_total_count = "SELECT COUNT(*) FROM games;"
   sql_O_count = "SELECT COUNT(*) FROM games WHERE winner='O';"
   sql_X_count = "SELECT COUNT(*) FROM games WHERE winner='X';"

   db = sqlite3.connect("TicTacToe.db")
   cursor = db.cursor()

   if item == "TOTAL":
      cursor.execute(sql_total_count)
   elif item == "O":
      cursor.execute(sql_O_count)
   else:
      cursor.execute(sql_X_count)   

   ct = cursor.fetchone()
   cursor.close()
   db.commit()             
   db.close

   return (ct[0])

#-------------------------------------
# get games
#-------------------------------------
def getGames():
   sql_select = "SELECT * FROM games;"
   db = sqlite3.connect("TicTacToe.db")
   cursor = db.cursor()

   cursor.execute(sql_select)
   result = cursor.fetchall()

   cursor.close()
   db.commit()             
   db.close

   return (result)

#-------------------------------------
# clear history
#-------------------------------------
def clearHistory():
   sql_del = "DELETE FROM games;"
   
   db = sqlite3.connect("TicTacToe.db")
   cursor = db.cursor()

   cursor.execute(sql_del)
   cursor.close()
   db.commit()             
   db.close


