

# capabilities to export data to csv / excel sheet
# uses openpxyl & csv
# examples: https://foss.heptapod.net/openpyxl/openpyxl
import os
import shutil
import openpyxl
import csv
import sqlite3
import datetime
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
          write_iter_into_excel(self.default_columns, data, file)
     open_explorer_at_file(self, file)
def export_eol(self, csv: bool, file: str, year: str):
     csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
     file = f"{file}_EOL{csv_or_xlsx_str}"
     data = fetch_obj_from_eol(year)
     if csv:
          write_iter_into_csv(self.default_columns, data, file)
     else:  # excel export :D
          write_iter_into_excel(self.default_columns, data, file)
     open_explorer_at_file(self, file)
def export_loc(self, csv: bool, file: str, place: str):
     csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
     file = f"{file}_location{csv_or_xlsx_str}"
     data = fetch_obj_from_loc(place)
     if csv:
          write_iter_into_csv(self.default_columns, data, file)
     else:  # excel export :D
          write_iter_into_excel(self.default_columns, data, file)
     open_explorer_at_file(self, file)
def export_ret(self, csv: bool, file: str, year: str):  # can be year or 'All'
     csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
     file = f"{file}_retired{csv_or_xlsx_str}"
     data = fetch_retired_assets(year)
     if csv:
          write_iter_into_csv(self.default_columns, data, file)
     else:  # excel export :D
          write_iter_into_excel(self.default_columns, data, file)
     open_explorer_at_file(self, file)
def write_iter_into_csv(columns, iterable, filename: str):
     with open(filename, "w") as csv_file:
          wr = csv.writer(csv_file, delimiter=",")
          wr.writerow(columns)
          for item in iterable:
               wr.writerow(list(item))

def write_iter_into_excel(columns, iterable, filename: str):
     wb = openpyxl.Workbook()
     active_ws = wb.active
     active_ws.append(columns)
     for row in iterable:
          active_ws.append(row)
     wb.save(filename)

# not really an 'export' file, but is only used here, an fits nowhere else really..
def open_explorer_at_file(self, file: str):
     # maybe have setting (only one or the other) to open the file in explorer, or to open the file..
     file = os.path.dirname(file)

     
     if self.settings_report_auto_open_checkbox.isChecked():
          file = os.path.realpath(file)
          os.startfile(file)

def create_backup(self):
     time_and_date = str(datetime.datetime.now()).replace(":", "-")[:19]
     filename = f"INVMAN_BACKUP__{time_and_date}"
     backup_dir = self.config["backup_path"]
     if not backup_dir.endswith("/") or not backup_dir.endswith("\\"):
          backup_dir += "/"
     filename += ".db"
     end_file = f"{backup_dir}{filename}"
     shutil.copyfile("main.db", end_file)     
     self.display_error_message(f"Backup created successfully: {filename}")
     open_explorer_at_file(self, end_file)
