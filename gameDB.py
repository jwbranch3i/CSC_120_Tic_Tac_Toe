import sqlite3

def dbSetup():
   db = sqlite3.connect("TicTacToe.db")
   db.execute("CREATE TABLE IF NOT EXISTS games(\
      gameDate TEXT,\
      gameTime TEXT,\
      winner TEXT,\
      board TEXT)")
   db.close()

