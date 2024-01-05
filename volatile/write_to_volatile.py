
# will be used to write to /volatile/assetcategory.json
# format is: <Category>: <years until replacement>
# e.g. {"HARDWARE": 4}
import json

def add_to_asset_list(name: str, years: int):
     with open("./volatile\\assetcategory.json", "r") as f:
          raw = json.load(f)
          raw[name] = years
          json_data = json.dumps(raw, indent=4)
     with open(".\\volatile\\assetcategory.json", "w") as w:  # stupid, didnt work otherwise..
          w.write(json_data)
