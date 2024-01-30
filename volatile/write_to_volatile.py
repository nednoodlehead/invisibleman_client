
# will be used to write to /volatile/assetcategory.json
# format is: <Category>: <years until replacement>
# e.g. {"HARDWARE": 4}
import json

def add_to_asset_list(name: str, years: int):
     with open("./volatile/assetcategory.json", "r") as f:
          raw = json.load(f)
          raw["Category"][name] = years
          json_data = json.dumps(raw, indent=4)
     with open("./volatile/assetcategory.json", "w") as w:  # stupid, didnt work otherwise..
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

def write_to_config(ham_menu: bool, checkboxes: dict):
     # completely overwrite the current config
     pre_json = {
          "ham_menu_status": ham_menu,
          "checkboxes": checkboxes
     }
     with open("./volatile/config.json", "w") as w:
          prep = json.dumps(pre_json, indent=4)
          w.write(prep)
