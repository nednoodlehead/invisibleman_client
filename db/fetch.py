import sqlite3
from util.data_types import InventoryObject, TableObject


def fetch_all() -> [InventoryObject]:
     return_list = []
     with sqlite3.connect("main.db") as conn:
          data = conn.execute("SELECT * FROM main")
          for item in data:
               return_list.append(InventoryObject(*item))
     return return_list
                         
def fetch_all_for_table() -> [TableObject]:
     return_list = []
     with sqlite3.connect("main.db") as conn:
          data = conn.execute("SELECT name, serial, manufacturer, price, assetcategory, assettype, assignedto, assetlocation, purchasedate, installdate, replacementdate, notes, uniqueid FROM main WHERE status = 1")
          for item in data:
               return_list.append(TableObject(*item))
     return return_list

# should only ever be called from a noteswindow being create, always with valid uuid.
def fetch_notes_from_uuid(uuid: str) -> str:
     with sqlite3.connect("main.db") as conn:
          data = conn.execute("SELECT notes FROM main WHERE uniqueid = ?", [uuid])
     return data.fetchone()[0]  # grab the only option
