# will be used to write to /volatile/assetcategory.json
# format is: <Category>: <years until replacement>
# e.g. {"HARDWARE": 4}
import json


authoriative_json = {
    "checkboxes": None,
    "dark_mode": True,
    "backup_path": "C:/",
    "default_report_path": "C:/",
    "auto_open_report_on_create": True,
    "top_graph_type": "Line",
    "top_graph_data": "Manufacturer",
    "invisman_ip": "192.168.1.1",
    "switch_view_on_insert": True
}

default_json = {
    "checkboxes": {
        "Asset Type": True,
        "Manufacturer": True,
        "Serial Number": True,
        "Model": True,
        "Cost": True,
        "Assigned To": True,
        "Name": True,
        "Asset Location": True,
        "Asset Category": True,
        "Deployment Date": True,
        "Replacement Date": True,
        "Notes": True,
        "Clouded or local": True
    },
    "dark_mode": True,
    "backup_path": "c:/",
    "default_report_path": "C:/",
    "auto_open_report_on_create": True,
    "top_graph_type": "Line",
    "top_graph_data": "Manufacturer",
    "invisman_ip": "192.168.1.1",
    "switch_view_on_insert": True
}


def add_to_asset_list(conn, name: str, years: int):
    # ok, so now the "json" lives on the server inside of the "config" table, so we query that.
    # also, this adding to list here WILL NOT check for duplicates, it is up to the inserter to not be a moron
    cur = conn.cursor()
    fixed_str = f'{name}@{years}'
    print("Adding to asset list on server!")
    cur.execute("insert into config values (Category, %s)", (fixed_str,))
    conn.commit()
    # we will also call this to refresh our config from the server! for the funny edge cases wherewe add a value, then try to use it
    


def add_to_type_or_location(conn, new: str, type_or_loc: str):
    cur = conn.cursor()
    print("adding type or location")
    # type or loc needs to have a capital letter at the beginning...
    cur.execute("insert into config values (%s, %s)", (type_or_loc, new))
    conn.commit()


def read_from_config() -> dict:
    """
    "ham_menu_status" & "checkboxes"
    """
    try:
        with open("./volatile/config.json", "r") as f:
            raw = json.load(f)
    except FileNotFoundError:
        with open("./volatile.config.json", "w") as f:
            f.write(json.dumps(default_json, indent=4))
            return default_json
    for key, val in authoriative_json.items():
        if key not in raw.keys():
            print(f"missing {key}, inserting...")
            raw[key] = val
            
        
    return raw


def write_to_config(pre_json: dict):
    # completely overwrite the current config
    with open("./volatile/config.json", "w") as w:
        prep = json.dumps(pre_json, indent=4)
        w.write(prep)
