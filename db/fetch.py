import sqlite3
from util.data_types import InventoryObject


def fetch_all() -> [InventoryObject]:
     return_list = []
     with sqlite3.connect("main.db") as conn:
          data = conn.execute("SELECT * FROM main")
          for item in data:
               return_list.append(InventoryObject(*item))
     return return_list
                         
