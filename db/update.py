import sqlite3
from util.data_types import InventoryObject

def update_notes(notes: str, uuid: str):
     with sqlite3.connect("main.db") as conn:
          conn.execute("UPDATE main SET notes = ? WHERE uniqueid = ?", (notes, uuid))
          conn.commit()

def update_full_obj(obj: InventoryObject):
     rel = {
          "Enabled": 1,
          "Disabled": 2
     }
     obj.status = rel[obj.status]
     with sqlite3.connect("main.db") as conn:
          conn.execute("""
                       UPDATE main 
                       SET name = ?,
                       serial = ?,
                       manufacturer = ?,
                       price = ?,
                       assetcategory = ?,
                       assettype = ?,
                       assignedto = ?,
                       assetlocation = ?,
                       purchasedate = ?,
                       installdate = ?,
                       replacementdate = ?,
                       notes = ?,
                       status = ?
                       WHERE uniqueid = ?
                        """,
                       (*obj, ))
          
