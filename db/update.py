import sqlite3
from util.data_types import InventoryObject


def update_notes(notes: str, uuid: str):
    with sqlite3.connect("main.db") as conn:
        conn.execute("UPDATE main SET notes = ? WHERE uniqueid = ?", (notes, uuid))
        conn.commit()
    # it could be an idea to refresh the notes button, so when its update, it changes to either 'View Notes' or
    # 'Add Notes' based on the value of the field. But seems sort of silly bcs of the overhead
    # of passing in a reference to the main class, then the logic of changing the button.
    # i dont think its worth it really...


def update_full_obj(obj: InventoryObject):
    rel = {"Enabled": 1, "Disabled": 2}
    obj.status = rel[obj.status]
    with sqlite3.connect("main.db") as conn:
        conn.execute(
            """
                       UPDATE main 
                       SET assettype = ?,
                       manufacturer = ?,
                       serial = ?,
                       model = ?,
                       cost = ?,
                       assignedto = ?,
                       assetlocation = ?,
                       assetcategory = ?,
                       assettype = ?,
                       deplomentdate = ?,
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
