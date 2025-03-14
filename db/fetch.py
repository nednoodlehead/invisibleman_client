import sqlite3
from util.data_types import InventoryObject, TableObject


def fetch_all() -> [InventoryObject]:
    return_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute("SELECT * FROM main")
        for item in data:
            return_list.append(InventoryObject(*item))
    return return_list


def fetch_all_enabled():  # [InventoryObject] without the enabled field
    return_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            """
            SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
            deploymentdate, replacementdate, notes, uniqueid FROM main WHERE status = 0;
            """
        )
        for item in data:
            return_list.append(item)
    return return_list


def fetch_all_enabled_for_table() -> [TableObject]:
    return_list = []
    # RETIRED = 1
    # NOT RETIRED = 0
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            """
            SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
            deploymentdate, replacementdate, retirementdate, notes, status, uniqueid FROM main WHERE status = 0
            """
        )
        for item in data:
            return_list.append(TableObject(*item))
    return return_list


def fetch_all_for_table() -> [TableObject]:
    return_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            """
            SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
            deploymentdate, replacementdate, retirementdate, notes, status, uniqueid FROM main
            """
        )
        for item in data:
            return_list.append(TableObject(*item))
    return return_list


# should only ever be called from a noteswindow being create, always with valid uuid.
def fetch_notes_from_uuid(uuid: str) -> str:
    with sqlite3.connect("main.db") as conn:
        data = conn.execute("SELECT notes FROM main WHERE uniqueid = ?", [uuid])
    return data.fetchone()[0]  # grab the only option


def fetch_from_uuid_to_update(uuid: str) -> InventoryObject:
    with sqlite3.connect("main.db") as conn:
        data = conn.execute("SELECT * FROM main WHERE uniqueid = ?", [uuid])
    processed = data.fetchone()
    obj = InventoryObject(*processed)
    return obj


def fetch_obj_from_retired():
    ret_list = []
    with sqlite3.connect("main.db") as conn:
        # remember. 1 = retired
        data = conn.execute(
            """
            SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
            assetlocation, assetcategory, deploymentdate, replacementdate,
            notes, uniqueid, retirementdate FROM main
            WHERE status = 1 
            """,
        )
    for item in data:
        ret_list.append(item)
    return ret_list


def fetch_obj_from_loc(location):
    ret_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            """
            SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
            assetlocation, assetcategory, deploymentdate, replacementdate,
            notes, uniqueid FROM main
            WHERE status = 0 AND assetlocation = ?
            """,
            (location,),
        )
    for item in data:
        ret_list.append(item)
    return ret_list


def fetch_retired_assets(year: str):
    ret_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            """
            SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
            assetlocation, assetcategory, deploymentdate, replacementdate, notes, uniqueid
            FROM main
            WHERE replacementdate <= ? AND status = 0
            """, (year,)
        )
    for item in data:
        ret_list.append(item)
    return ret_list

def fetch_all_serial() -> [str]:
    with sqlite3.connect("main.db") as conn:
        data = conn.execute("""
           SELECT serial FROM main 
        """)
        # x[0] because it returns data like: ('123',)
    return [x[0] for x in data]


def fetch_by_serial(finding: str) -> InventoryObject:
    with sqlite3.connect("main.db") as conn:
        proc = conn.execute("SELECT * FROM main WHERE serial = ?", (finding,))
        # this is strongly assuming that there is only one S/N that matches this. It will grab the first one (order based on insertion)
        # so, don't be stupid and have a bunch of same-type serial numbers. They should be unique irl anyways
        ret = proc.fetchone()
        obj = InventoryObject(*ret)
    # [0] because it returns in a tuple??
    return obj 

