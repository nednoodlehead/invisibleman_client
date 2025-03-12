# will be used to write to /volatile/assetcategory.json
# format is: <Category>: <years until replacement>
# e.g. {"HARDWARE": 4}
import json


def add_to_asset_list(name: str, years: int):
    with open("./volatile/assetcategory.json", "r") as f:
        raw = json.load(f)
        raw["Category"][name] = years
        json_data = json.dumps(raw, indent=4)
    with open(
        "./volatile/assetcategory.json", "w"
    ) as w:  # stupid, didnt work otherwise..
        w.write(json_data)


def add_to_type_or_location(new: str, type_or_loc: str):
    with open("./volatile/assetcategory.json", "r") as f:
        raw = json.load(f)
        raw[type_or_loc].append(new)
        json_data = json.dumps(raw, indent=4)
    with open("./volatile/assetcategory.json", "w") as w:
        w.write(json_data)


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
    }
    with open("./volatile/config.json", "w") as w:
        prep = json.dumps(pre_json, indent=4)
        w.write(prep)
