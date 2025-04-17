# will be used to write to /volatile/assetcategory.json
# format is: <Category>: <years until replacement>
# e.g. {"HARDWARE": 4}
import json


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
    # with open("10.100.0.9/srv/invisman/assetcategory.json", "r") as f:
    #     raw = json.load(f)
    #     raw[type_or_loc].append(new)
    #     json_data = json.dumps(raw, indent=4)
    # with open("10.100.0.9/srv/invisman/assetcategory.json", "w") as w:
    #     w.write(json_data)


def read_from_config() -> dict:
    """
    "ham_menu_status" & "checkboxes"
    """
    with open("./volatile/config.json", "r") as f:
        raw = json.load(f)
    return raw


def write_to_config(
    checkboxes: dict,
    dark_mode_on: bool,
    backup_path: str,
    report: bool,
    report_path: str,
    top_graph_type: str,
    top_graph_data: str,
    invisman_username: str,
    ssh_path: str,
    invisman_ip: str,
):
    # completely overwrite the current config
    pre_json = {
        "checkboxes": checkboxes,
        "dark_mode": dark_mode_on,
        "backup_path": backup_path,
        "default_report_path": report_path,
        "auto_open_report_on_create": report,
        "top_graph_type": top_graph_type,
        "top_graph_data": top_graph_data,
        "invisman_username": invisman_username,
        "ssh_path": ssh_path,
        "invisman_ip": invisman_ip,
    }
    with open("./volatile/config.json", "w") as w:
        prep = json.dumps(pre_json, indent=4)
        w.write(prep)
