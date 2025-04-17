import sqlite3
from util.data_types import InventoryObject, TableObject


def fetch_all(conn) -> list[InventoryObject]:
    return_list = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM main;")
    for item in cur.fetchall():
        return_list.append(InventoryObject(*item))
    return return_list


def fetch_all_enabled(conn):  # [InventoryObject] without the enabled field
    return_list = []
    cur = conn.cursor()
    data = cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
        deploymentdate, replacementdate, notes, uniqueid FROM main WHERE status = false;
        """
    )
    for item in data:
        return_list.append(item)
    return return_list


def fetch_all_enabled_for_table(conn) -> list[TableObject]:
    return_list = []
    # RETIRED = 1
    # NOT RETIRED = 0
    cur = conn.cursor()
    data = cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
        deploymentdate, replacementdate, retirementdate, notes, status, uniqueid FROM main WHERE status = false order by deploymentdate desc NULLS last;"""
    )
    data = cur.fetchall()
    for item in data:
        return_list.append(TableObject(*item))
    return return_list


def fetch_all_for_table(conn) -> list[TableObject]:
    return_list = []
    cur = conn.cursor()
    cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
        deploymentdate, replacementdate, retirementdate, notes, status, uniqueid FROM main order by deploymentdate desc nulls last;
        """
    )
    for item in cur.fetchall():
        return_list.append(TableObject(*item))
    return return_list


# should only ever be called from a noteswindow being create, always with valid uuid.
def fetch_notes_from_uuid(conn, uuid: str) -> str:
    cur = conn.cursor()
    cur.execute("SELECT notes FROM main WHERE uniqueid = %s;", [uuid])
    return cur.fetchone()[0]  # grab the only option


def fetch_from_uuid_to_update(conn, uuid: str) -> InventoryObject:
    cur = conn.cursor()
    cur.execute("SELECT * FROM main WHERE uniqueid = %s;", [uuid])
    processed = cur.fetchone()
    obj = InventoryObject(*processed)
    return obj


def fetch_obj_from_retired(conn):
    ret_list = []
    # true = retired
    cur = conn.cursor()
    cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
        assetlocation, assetcategory, deploymentdate, replacementdate,
        notes, uniqueid, retirementdate FROM main
        WHERE status = true;
        """,
    )
    for item in cur.fetch_all():
        ret_list.append(item)
    return ret_list


def fetch_obj_from_loc(conn, location):
    ret_list = []
    cur = conn.cursor()
    cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
        assetlocation, assetcategory, deploymentdate, replacementdate,
        notes, uniqueid FROM main
        WHERE status = false AND assetlocation = %s;
        """,
        (location,),
    )
    for item in cur.fetch_all():
        ret_list.append(item)
    return ret_list


def fetch_retired_assets(conn, year: str):
    ret_list = []
    cur = conn.cursor()
    cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
        assetlocation, assetcategory, deploymentdate, replacementdate, notes, uniqueid
        FROM main
        WHERE replacementdate <= %s AND status = false;
        """, (year,)
    )
    for item in cur.fetch_all():
        ret_list.append(item)
    return ret_list

def fetch_all_serial(conn) -> list[str]:
    cur = conn.cursor()
    cur.execute("""
       SELECT serial FROM main;
    """)
        # x[0] because it returns data like: ('123',)
    return [x[0] for x in cur.fetchall()]


def fetch_by_serial(conn, finding: str) -> InventoryObject:
    cur = conn.cursor()
    cur.execute("SELECT * FROM main WHERE serial = %s;", (finding,))
    # this is strongly assuming that there is only one S/N that matches this. It will grab the first one (order based on insertion)
    # so, don't be stupid and have a bunch of same-type serial numbers. They should be unique irl anyways
    ret = cur.fetchone()
    obj = InventoryObject(*ret)
    # [0] because it returns in a tuple??
    return obj 

