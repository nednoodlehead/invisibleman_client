from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit
import json


# so with the new architecture, we should probably keep a local verion of the asset cache so we arent making requests all the damn time
# we can also have a way to force a reload. a button in settings, and a signal from the server.. maybe.


# this force json sync will be called everytime the client begins a connection on startup
def force_json_sync(self, conn):
    print("FORCING SYNC!!")
    cur = conn.cursor()
    cur.execute("SELECT * from config")
    building_json = {"Category": {}, "Type":[], "Location": [], "Manufacturer": []}
    # this feels redundant, but i do sort of want the extra information, i have a feeling that somehow the json is gonna get messed up.
    for line in cur.fetchall():
        if line[0] == "Category":
            con, val = line[1].split("@")
            building_json["Category"][con] = int(val)
        elif line[0] == "Type":
            building_json["Type"].append(line[1])
        elif line[0] == "Location":
            building_json["Location"].append(line[1])
        elif line[0] == "Manufacturer":
            building_json["Manufacturer"].append(line[1])
        else:
            raise ValueError(f"How did we get here? json is misconfigured somewhere, this is expecting either 'category', 'type' or 'location' but we got: {line[0]}")
    with open("./volatile/assetcategory.json", "w") as w:
        json_obj = json.dumps(building_json, indent=4)
        w.write(json_obj)
        
        

def update_replacement_date(self):
    """
    updates the date of the replacement date based on the type of gear selected
    """
    item = self.insert_asset_category_combobox.currentText().split("@")[0]
    add_from = QDate.fromString(self.insert_deployment_date_fmt.text(), "yyyy-MM-dd")
    if item == "":  # if default value
        self.insert_replacement_date_fmt.setDate(QDate.currentDate())
        return None  # teminate..

    with open("./volatile/assetcategory.json", "r") as f:
        raw_json = json.load(f)["Category"]
    self.insert_replacement_date_fmt.setDate(add_from.addYears(raw_json[item]))


# might be quicker to also have a function to open the file once and return all the json, 1rw instead of 3..
def refresh_asset_categories(self, conn) -> list[str]:
    # asset_categories = []
    # with open("./volatile/assetcategory.json") as f:
    #     raw_json = json.load(f)["Category"]
    #     for key, val in raw_json.items():
    #         asset_categories.append(key)
    # return asset_categories
    cur = conn.cursor()
    cur.execute("select * from config where type = 'Category';")
    print(f"returning categories: {cur.fetchall()}")
    return [x[1] for x in cur.fetchall()]


def add_asset_type(self, item_type: str, years_ahead: int):
    with open("./volatile/assetcategory.json", "r") as f:
        raw = json.load(f)
        raw[item_type] = years_ahead
        json_data = json.dumps(raw, indent=4)
    with open("./volatile/assetcategory.json") as w:
        w.write(json_data)


# idk full reach of these, might want to re-write into
def refresh_asset_types(self, conn) -> list[str]:
    # asset_types = []
    # with open("./volatile/assetcategory.json") as f:
    #     raw_json = json.load(f)["Type"]
    #     for val in raw_json:
    #         asset_types.append(val)
    # return asset_types
    cur = conn.cursor()
    cur.execute("select * from config where type = 'Type';")
    return [x[1] for x in cur.fetchall()]


def refresh_asset_location(self, conn) -> list[str]:
    # asset_location = []
    # with open(
    #     "./volatile/assetcategory.json"
    # ) as f:  # maybe change the name of the json? assets.json? asset_info.json
    #     raw_json = json.load(f)["Location"]
    #     for val in raw_json:
    #         asset_location.append(val)
    # return asset_location
    cur = conn.cursor()
    cur.execute("select * from config where type = 'Location';")
    return [x[1] for x in cur.fetchall()]


def refresh_manufacturer(self, conn) -> list[str]:
    # asset_location = []
    # with open(
    #     "./volatile/assetcategory.json"
    # ) as f:  # maybe change the name of the json? assets.json? asset_info.json
    #     raw_json = json.load(f)["Manufacturer"]
    #     for val in raw_json:
    #         asset_location.append(val)
    # return asset_location
    cur = conn.cursor()
    cur.execute("select * from config where type = 'Manufacturer';")
    return [x[1] for x in cur.fetchall()]


def fetch_all_asset_types(self) -> tuple[list[str], list[str], list[str], list[str]]:  # category, type, location
    asset_types = []
    asset_categories = []
    asset_location = []
    manufacturer = []
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
            elif key == "Manufacturer":
                for asset in data:
                    manufacturer.append(asset)
            else:
                for location in data:
                    asset_location.append(location)
    return (asset_categories, asset_types, asset_location, manufacturer)


def fetch_categories_and_years(self, conn):
    # with open("volatile/assetcategory.json", "r") as f:
    #     return json.load(f)["Category"]
    # MIGHT HAVE TO REVERT TO PASSING THE CONNECTION :(
    cur = conn.cursor()
    cur.execute("select * from config where type = 'Category';")
    return [x[1] for x in cur.fetchall()]


