import sqlite3
from util.data_types import InventoryObject


def new_entry(conn, insert: InventoryObject):
    temp = tuple(insert)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO main VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", temp
    )
    conn.commit()
