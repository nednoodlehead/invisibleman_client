from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit
import json
def update_replacement_date(self):
     """
     updates the date of the replacement date based on the type of gear selected          
     """
     item = self.insert_asset_type_combobox.currentText()
     today = QDate.currentDate()
     # turn into json, and have user be able to change this from settings
     json_new = {
          "Network": 4,
          "Security": 4,
          "Hardware and Accessories": 4,
          "Telecommunications": 4,
          "Printing": 5,
          "Software": 1
       }
     self.insert_replacement_date_fmt.setDate(today.addYears(json_new[item]))

# called 
def refresh_asset_types(self):
     # will pull from a json (maybe send to volatile?)
     asset_types = []
     with open("./volatile/assetcategory.json") as f:
          raw_json = json.load(f)["Category"]
          for key, val in raw_json.items():
               asset_types.append(key)
     return asset_types

def add_asset_type(self, item_type: str, years_ahead: int):
     with open("./volatile/assetcategory.json", "r") as f:
          raw = json.load(f)
          raw[item_type] = years_ahead
          json_data = json.dumps(raw, indent=4)
     with open("./volatile/assetcategory.json") as w:
          w.write(json_data)
          
