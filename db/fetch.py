import sqlite3
from util.data_types import InventoryObject, TableObject, ExtraObject
from datetime import date


def fetch_all(conn) -> list[InventoryObject]:
    return_list = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM main;")
    for item in cur.fetchall():
        return_list.append(InventoryObject(*item))
    return return_list

def fetch_all_normal(conn) -> list[InventoryObject]:
    return_list = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM main;")
    for item in cur.fetchall():
        return_list.append(item)
    return return_list


def fetch_all_enabled(conn):  # [InventoryObject] without the enabled field
    return_list = []
    cur = conn.cursor()
    cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
        deploymentdate, replacementdate, notes, uniqueid FROM main WHERE status = false;
        """
    )
    for item in cur.fetchall():
        return_list.append(item)
    return return_list

def fetch_active_assets(conn):
    return_list = []
    cur = conn.cursor()
    cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
        deploymentdate, replacementdate, notes, CASE WHEN is_local = true then 'Local' WHEN is_local = false THEN 'Clouded' END FROM main WHERE status = false;
        """
    )
    for item in cur.fetchall():
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
        deploymentdate, replacementdate, retirementdate, notes, CASE WHEN is_local = true then 'Local' WHEN is_local = false THEN 'Clouded' END, status,  uniqueid FROM main WHERE status = false order by deploymentdate desc NULLS last;"""
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
        deploymentdate, replacementdate, retirementdate, notes, CASE WHEN is_local = true then 'Local' WHEN is_local = false THEN 'Clouded' END,
        status, uniqueid FROM main order by deploymentdate desc nulls last;
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
    cur.execute("""SELECT assettype, manufacturer, serial, model, cost, assignedto, name, assetlocation, assetcategory,
                 deploymentdate, replacementdate, retirementdate, notes, is_local, status, uniqueid FROM main WHERE uniqueid = %s;""", [uuid])
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
        notes, CASE WHEN is_local = false THEN 'Clouded' WHEN is_local = true THEN 'Local' END, retirementdate FROM main
        WHERE status = true;
        """,
    )
    for item in cur.fetchall():
        ret_list.append(item)
    return ret_list


def fetch_obj_from_loc(conn, location):
    ret_list = []
    cur = conn.cursor()
    cur.execute(
        """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
        assetlocation, assetcategory, deploymentdate, replacementdate,
        notes, CASE WHEN is_local = false THEN 'Clouded' WHEN is_local = true THEN 'Local' END FROM main
        WHERE status = false AND assetlocation = %s;
        """,
        (location,),
    )
    for item in cur.fetchall():
        ret_list.append(item)
    return ret_list


def fetch_retired_assets(conn, year: str, include_overdue: bool):
    ret_list = []
    cur = conn.cursor()
    if include_overdue:
        cur.execute(
            """
            SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
            assetlocation, assetcategory, deploymentdate, replacementdate, notes, CASE WHEN is_local = false THEN 'Clouded' WHEN is_local = true THEN 'Local' END
            FROM main
            WHERE replacementdate <= %s AND status = false;
            """, (year,)
        )
    else:

        cur.execute(
            """
        SELECT assettype, manufacturer, serial, model, cost, assignedto, name,
        assetlocation, assetcategory, deploymentdate, replacementdate, notes, CASE WHEN is_local = false THEN 'Clouded' WHEN is_local = true THEN 'Local' END
        FROM main where replacementdate between %s and %s and status = false;
            """, (date.today(), year)
        )
    for item in cur.fetchall():
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

def fetch_all_extras(conn):
    cur = conn.cursor()
    cur.execute("SELECT * from extras order by item;");
    return [x for x in cur.fetchall()]

def fetch_specific_extra(conn, uuid):
    cur = conn.cursor()
    cur.execute("select item, manufacturer, count, low_amount, reserved, notes from extras where uniqueid =%s;", (uuid,))
    return cur.fetchone() # [0] cause it returns a tuple with one item in it??

def fetch_changed_assets(conn, month=None, year=None):
    # MONTH SHOULD BE AN INT (1-12)
    # year should be: '2025'-like int
    # get only the target month and year. originally had the concept to delete the data after a given month / year, but why not keep this data. no reason to delete it... 
    today = date.today()
    if not month:
        month = today.month
    if not year:
        year = today.year
    cur = conn.cursor()
    # idk why this requires a left join, makes no sense
    # like all instances in the `left` should be represented in the middle
    cur.execute("""select old_name, new_name, old_location, new_location, edit_date, (CASE WHEN m.retirementdate is null then 'Active' else 'Retired' END) as is_retired
                 from changed
                 left join main as m on new_name = m.name
                 where date_part('year', edit_date) = %s and date_part('month', edit_date) = %s;""", (year, month))
    return cur.fetchall()

def fetch_from_date_range(conn, date_start, date_end):
    cur = conn.cursor()
    cur.execute("""select assettype, manufacturer, serial, model, cost, assignedto, name,
        assetlocation, assetcategory, deploymentdate, replacementdate, notes, CASE WHEN is_local = false THEN 'Clouded' WHEN is_local = true THEN 'Local' END
        FROM main where status = false AND replacementdate between %s AND %s""", (date_start, date_end))
    return [x for x in cur.fetchall()]

def fetch_by_variable(conn, display_name):
    # turn the display names into the columns names in the database
    # no, im not worried about sql injection, the possible values are derived from a list
    # would it make more sense to just have a separate function for each of these possibilities? Maybe?
    # this keeps it a bit simpler imo, and this list could be a 'remove whitespace and .lower()' but i prefer this
    # due to readability
    var_map = {
        "Manufacturer": "manufacturer",
        "Asset Category": "assetcategory",
        "Asset Type": "assettype",
        "Asset Location": "assetlocation",
        "Deployment Date": "deploymentdate",
        "Replacement Date": "replacementdate",
        # notes are handled a bit differnetly (with it being the 'notes or no notes' type, but that is handled later)
    }
    cur = conn.cursor()
    if display_name == "Deployment Date" or display_name == "Replacement Date":
        column = var_map[display_name]
        cur.execute(f"select extract(year from {column}) as yr, count(*) as total from main group by yr order by total desc;")
    elif display_name == "Notes":
        cur.execute("select count(*) filter (where notes is null) as No_notes, count(*) filter (where notes is not null) as Some_Notes from main")        
        y = cur.fetchall()
        return {"None": y[0][0], "Some": y[0][1]}
    else:
        column = var_map[display_name]
        cur.execute(f"select coalesce({column}, 'Unknown'), count(*) as total from main group by {column} order by total desc;")
    return cur.fetchall()
