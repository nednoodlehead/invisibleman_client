from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit
import json


def update_replacement_date(self):
    """
    updates the date of the replacement date based on the type of gear selected
    """
    item = self.insert_asset_category_combobox.currentText()
    add_from = QDate.fromString(self.insert_install_date_fmt.text(), "yyyy-MM-dd")
    if item == "":  # if default value
        self.insert_replacement_date_fmt.setDate(QDate.currentDate())
        return None  # teminate..

    with open("./volatile/assetcategory.json", "r") as f:
        raw_json = json.load(f)["Category"]
    self.insert_replacement_date_fmt.setDate(add_from.addYears(raw_json[item]))


# might be quicker to also have a function to open the file once and return all the json, 1rw instead of 3..
def refresh_asset_categories(self) -> [str]:
    asset_categories = []
    with open("./volatile/assetcategory.json") as f:
        raw_json = json.load(f)["Category"]
        for key, val in raw_json.items():
            asset_categories.append(key)
    return asset_categories


def add_asset_type(self, item_type: str, years_ahead: int):
    with open("./volatile/assetcategory.json", "r") as f:
        raw = json.load(f)
        raw[item_type] = years_ahead
        json_data = json.dumps(raw, indent=4)
    with open("./volatile/assetcategory.json") as w:
        w.write(json_data)


# idk full reach of these, might want to re-write into
def refresh_asset_types(self) -> [str]:
    asset_types = []
    with open("./volatile/assetcategory.json") as f:
        raw_json = json.load(f)["Type"]
        for val in raw_json:
            asset_types.append(val)
    return asset_types


def refresh_asset_location(self) -> [str]:
    asset_location = []
    with open(
        "./volatile/assetcategory.json"
    ) as f:  # maybe change the name of the json? assets.json? asset_info.json
        raw_json = json.load(f)["Location"]
        for val in raw_json:
            asset_location.append(val)
    return asset_location


def fetch_all_asset_types(self) -> ([str], [str], [str]):  # category, type, location
    asset_types = []
    asset_categories = []
    asset_location = []
    with open("./volatile/assetcategory.json") as f:
        raw_json = json.load(f)
        post_first = False  # used to mark that we have parsed past the first dict
        for key, data in raw_json.items():
            if key == "Category":
                for cat, val in data.items():
                    asset_categories.append(cat)
            elif key == "Type":
                for asset in data:
                    asset_types.append(asset)
            else:
                for location in data:
                    asset_location.append(location)
    return (asset_categories, asset_types, asset_location)


def fetch_categories_and_years(self):
    with open("volatile/assetcategory.json", "r") as f:
        return json.load(f)["Category"]


def replace_json_target(target: str, data: dict):
    with open("volatile/assetcategory.json", "r") as f:
        raw_json = json.load(f)
        raw_json[target] = data
        json_data = json.dumps(raw_json, indent=4)
    with open("volatile/assetcategory.json", "w") as w:
        w.write(json_data)
