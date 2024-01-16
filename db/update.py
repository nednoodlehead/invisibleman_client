import sqlite3

def update_notes(notes: str, uuid: str):
     with sqlite3.connect("main.db") as conn:
          conn.execute("UPDATE main SET notes = ? WHERE uniqueid = ?", (notes, uuid))
          conn.commit()
          

