import sqlite3
from util.data_types import InventoryObject
def new_entry(insert: InventoryObject):
     conn = sqlite3.connect("main.db")
     temp = tuple(insert)
     conn.execute("INSERT INTO main VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", temp)
     conn.commit()
     conn.close()     
     
