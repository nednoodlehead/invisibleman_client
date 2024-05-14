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
            "SELECT name, serial, manufacturer, model, price, assetcategory, assettype, assignedto,\
                               assetlocation, purchasedate, installdate, replacementdate, notes, uniqueid FROM main\
                               WHERE status = 1"
        )
        for item in data:
            return_list.append(item)
    return return_list


def fetch_all_for_table() -> [TableObject]:
    return_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            "SELECT name, serial, manufacturer, model, price, assetcategory, assettype, assignedto, assetlocation, purchasedate, installdate, replacementdate, notes, uniqueid FROM main WHERE status = 1"
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


def fetch_obj_from_eol(eol_year):
    ret_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            "SELECT name, serial, manufacturer, model, price, assetcategory, assettype, assignedto,\
                               assetlocation, purchasedate, installdate, replacementdate, notes, uniqueid FROM main\
                               WHERE status = true AND strftime('%Y', replacementdate) = ? ",
            (eol_year,),
        )
    for item in data:
        ret_list.append(item)
    return ret_list


def fetch_obj_from_loc(location):
    ret_list = []
    with sqlite3.connect("main.db") as conn:
        data = conn.execute(
            "SELECT name, serial, manufacturer, model, price, assetcategory, assettype, assignedto,\
                               assetlocation, purchasedate, installdate, replacementdate, notes, uniqueid FROM main\
                               WHERE status = 1 AND assetlocation = ?",
            (location,),
        )
    for item in data:
        ret_list.append(item)
    return ret_list


def fetch_retired_assets(year: str):
    ret_list = []
    if year == "All":  # user wants all retired assets
        with sqlite3.connect("main.db") as conn:
            data = conn.execute(
                "SELECT name, serial, manufacturer, model, price, assetcategory, assettype, assignedto,\
                               assetlocation, purchasedate, installdate, replacementdate, notes, uniqueid FROM main\
                               WHERE status = false"
            )
    else:
        with sqlite3.connect("main.db") as conn:
            data = conn.execute(
                "SELECT name, serial, manufacturer, model, price, assetcategory, assettype, assignedto,\
                               assetlocation, purchasedate, installdate, replacementdate, notes, uniqueid FROM main\
                               WHERE status = 0 AND strftime('%Y', replacementdate) = ?",
                (year,),
            )
    for item in data:
        ret_list.append(item)
    return ret_list
