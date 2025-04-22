import sqlite3
from util.data_types import InventoryObject
from PyQt5.QtCore import QDate
from datetime import date


def update_notes(conn, notes: str, uuid: str):
    cur = conn.cursor()
    cur.execute("UPDATE main SET notes = %s WHERE uniqueid = %s", (notes, uuid))
    conn.commit()
    # it could be an idea to refresh the notes button, so when its update, it changes to either 'View Notes' or
    # 'Add Notes' based on the value of the field. But seems sort of silly bcs of the overhead
    # of passing in a reference to the main class, then the logic of changing the button.
    # i dont think its worth it really...


def update_full_obj(conn, obj: InventoryObject):
    rel = {"Active": False, "Retired": True}
    obj.status = rel[obj.status]
    cur = conn.cursor()
    # so here we check for empty strings and '2000-01-01' dates, which we will turn into null. So it can be better represented, and actually make sense.
    obj.assettype = None if obj.assettype == "" else obj.assettype
    obj.manufacturer = None if obj.manufacturer == "" else obj.manufacturer
    obj.serial = None if obj.serial == "" else obj.serial
    obj.model = None if obj.model == "" else obj.model
    obj.assignedto = None if obj.assignedto == "" else obj.assignedto
    obj.name = None if obj.assignedto == "" else obj.name
    obj.assetlocation = None if obj.assignedto == "" else obj.assetlocation
    obj.assetcategory = None if obj.assetcategory == "" else obj.assetcategory
    obj.deploymentdate = None if obj.deploymentdate == date.fromisoformat("2000-01-01") else obj.deploymentdate
    obj.replacementdate = None if obj.replacementdate == date.fromisoformat("2000-01-01") else obj.replacementdate
    obj.retirementdate = None if obj.retirementdate == date.fromisoformat("2000-01-01") else obj.retirementdate
    obj.notes = None if obj.notes == "" else obj.notes
    for x in obj:
        print(type(x), x)
    cur.execute(
        """
                   UPDATE main 
                   SET
                   assettype = %s,
                   manufacturer = %s,
                   serial = %s,
                   model = %s,
                   cost = %s,
                   assignedto = %s,
                   name = %s,
                   assetlocation = %s,
                   assetcategory = %s,
                   deploymentdate = %s,
                   replacementdate = %s,
                   retirementdate = %s,
                   notes = %s,
                   status = %s
                   WHERE uniqueid = %s;
                    """,
        (*obj,),
    )
    conn.commit()


def delete_from_uuid(conn, uuid: str):
    conn.execute("DELETE FROM main WHERE uniqueid = %s;", (uuid,))
    conn.commit()
        

def retire_from_uuid(conn, uuid: str):
    """
        Used when we are done with an asset. it gets retired, we set retireddate to today.
    and status to false
    """
    cur = conn.cursor()
    today = date.today()
    cur.execute("""
                UPDATE main SET status = True, retirementdate = %s WHERE uniqueid = %s;
                 """, (today, uuid))
    conn.commit()

def unretire_from_uuid(conn, uuid: str):
    cur = conn.cursor()
    cur.execute("UPDATE main SET status = False, retirementdate = NULL WHERE uniqueid = %s;", (uuid,))
    conn.commit()

def replace_server_config(conn, dict_or_list, target: str):
    cur = conn.cursor()
    cur.execute("delete from config where type = %s", (target,))
    if isinstance(dict_or_list, dict):
        for key, val in dict_or_list.items():
            # this is going to spam updates, wont it!?
            fixed_str = f'{key}@{val}' 
            cur.execute("insert into config (type, data) values ('Category', %s)", (fixed_str,))
    else:
        for val in dict_or_list:
            # this is going to spam updates, wont it!?
            cur.execute("insert into config (type, data) values (%s, %s)", (target, val))
    conn.commit()
