import sqlite3
from util.data_types import InventoryObject, ExtraObject


def new_entry(conn, insert: InventoryObject):
    temp = tuple(insert)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO main VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", temp
    )
    conn.commit()

def new_extra(conn, obj: ExtraObject) -> None:
    cur = conn.cursor()
    print(obj.uniqueid, type(obj.uniqueid))
    cur.execute("insert into extras values (%s, %s, %s, %s, %s, %s, %s);", (obj.item, obj.manufacturer, obj.count, obj.low_amount, obj.reserved, obj.notes, obj.uniqueid))
    conn.commit()
