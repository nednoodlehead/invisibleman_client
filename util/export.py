

# capabilities to export data to csv / excel sheet
# uses openpxyl & csv
# examples: https://foss.heptapod.net/openpyxl/openpyxl
import openpyxl
import csv
import sqlite3
from util.data_types import InventoryObject
from db.fetch import fetch_all_enabled, fetch_obj_from_eol, fetch_obj_from_loc, fetch_obj_from_eol, fetch_retired_assets
# self is passed in so we can update the self.reports_export_status_content label
# in rust i would just pass the result<> up the stream, but that design pattern doesnt really fit
# too well in python. also passed in to see self.main_table

# im also not too sure if pulling from main_table or db is quicker, im assuming db is better.. 

# TODO refactor this file so its less redundant.. dont need 4 if csv statements

def export_all(self, csv: bool, file: str):
     csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
     file = f"{file}_ALL{csv_or_xlsx_str}"
     data = fetch_all_enabled()
     if csv:
          write_iter_into_csv(self.default_columns, data, file)
     else:  # excel export :D
          pass

def export_eol(self, csv: bool, file: str, year: str):
     csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
     file = f"{file}_EOL{csv_or_xlsx_str}"
     data = fetch_obj_from_eol(year)
     if csv:
          write_iter_into_csv(self.default_columns, data, file)
     else:  # excel export :D
          pass

def export_loc(self, csv: bool, file: str, place: str):
     csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
     file = f"{file}_location{csv_or_xlsx_str}"
     data = fetch_obj_from_loc(place)
     if csv:
          write_iter_into_csv(self.default_columns, data, file)
     else:  # excel export :D
          pass

def export_ret(self, csv: bool, file: str, year: str):  # can be year or 'All'
     csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
     file = f"{file}_retired{csv_or_xlsx_str}"
     data = fetch_retired_assets(year)
     if csv:
          write_iter_into_csv(self.default_columns, data, file)
     else:  # excel export :D
          pass

def write_iter_into_csv(columns, iterable, filename: str):
     with open(filename, "w") as csv_file:
          wr = csv.writer(csv_file, delimiter=",")
          wr.writerow(columns)
          for item in iterable:
               wr.writerow(list(item))
