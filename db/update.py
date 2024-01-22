import sqlite3
from util.data_types import InventoryObject

def update_notes(notes: str, uuid: str):
     with sqlite3.connect("main.db") as conn:
          conn.execute("UPDATE main SET notes = ? WHERE uniqueid = ?", (notes, uuid))
          conn.commit()

def update_full_obj(obj: InventoryObject):
     with sqlite3.connect("main.db") as conn:
          conn.execute("""
                       UPDATE main 
                       SET name = ?,
                       SET serial = ?,
                       SET manufacturer = ?,
                       SET price = ?,
                       SET assetcategory = ?,
                       SET assettype = ?,
                       SET assignedto = ?,
                       SET assetlocation = ?,
                       SET purchasedate = ?,
                       SET installdate = ?,
                       SET replacementdate = ?,
                       SET notes = ?,
                       SET status = ?,
                       WHERE uniqueid = ?
                        """,
                       *obj)
