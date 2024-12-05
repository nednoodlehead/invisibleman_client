import sqlite3
from util.data_types import InventoryObject
from PyQt5.QtCore import QDate

def update_notes(notes: str, uuid: str):
    with sqlite3.connect("main.db") as conn:
        conn.execute("UPDATE main SET notes = ? WHERE uniqueid = ?", (notes, uuid))
        conn.commit()
    # it could be an idea to refresh the notes button, so when its update, it changes to either 'View Notes' or
    # 'Add Notes' based on the value of the field. But seems sort of silly bcs of the overhead
    # of passing in a reference to the main class, then the logic of changing the button.
    # i dont think its worth it really...


def update_full_obj(obj: InventoryObject):
    rel = {"Active": False, "Retired": True}
    obj.status = rel[obj.status]
    with sqlite3.connect("main.db") as conn:
        conn.execute(
            """
                       UPDATE main 
                       SET
                       assettype = ?,
                       manufacturer = ?,
                       serial = ?,
                       model = ?,
                       cost = ?,
                       assignedto = ?,
                       assetlocation = ?,
                       assetcategory = ?,
                       deploymentdate = ?,
                       replacementdate = ?,
                       retirementdate = ?,
                       notes = ?,
                       status = ?
                       WHERE uniqueid = ?
                        """,
            (*obj,),
        )
        conn.commit()


def delete_from_uuid(uuid: str):
    with sqlite3.connect("main.db") as conn:
        conn.execute("DELETE FROM main WHERE uniqueid = ?", (uuid,))
        conn.commit()
        

def retire_from_uuid(uuid: str):
    """
        Used when we are done with an asset. it gets retired, we set retireddate to today.
    and status to false
    """
    today = QDate.currentDate().toString("yyyy-MM-dd")
    with sqlite3.connect("main.db") as conn:
        conn.execute("""
                    UPDATE main SET status = 1, retirementdate = ? WHERE uniqueid = ?
                     """, (today, uuid))
        conn.commit()

def unretire_from_uuid(uuid: str):
    with sqlite3.connect("main.db") as conn:
        conn.execute("UPDATE main SET status = 0, retirementdate = NULL WHERE uniqueid = ?", (uuid,))
        conn.commit()
