# capabilities to export data to csv / excel sheet
# uses openpxyl & csv
# examples: https://foss.heptapod.net/openpyxl/openpyxl
import os
import shutil
import openpyxl
from openpyxl.worksheet.table import TABLESTYLES, Table, TableStyleInfo
from openpyxl.styles import Color, PatternFill
import csv
import sqlite3
import datetime
from util.data_types import InventoryObject
from db.fetch import (
    fetch_all_enabled,
    fetch_obj_from_retired,
    fetch_obj_from_loc,
    fetch_retired_assets,
    fetch_changed_assets
)
import datetime
import dateutil.relativedelta
# self is passed in so we can update the self.reports_export_status_content label
# in rust i would just pass the result<> up the stream, but that design pattern doesnt really fit
# too well in python. also passed in to see self.main_table

# im also not too sure if pulling from main_table or db is quicker, im assuming db is better..

# TODO refactor this file so its less redundant.. dont need 4 if csv statements


def export_active(self, csv: bool, file: str):
    csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
    file = f"{file}_ACTIVE{csv_or_xlsx_str}"
    data = fetch_all_enabled(self.connection)
    if csv:
        write_iter_into_csv(self.default_columns, data, file)
    else:  # excel export :D
        write_iter_into_excel(self.default_columns, data, file)
    open_explorer_at_file(self, file)


def export_retired(self, csv: bool, file: str):
    csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
    file = f"{file}_RETIRED{csv_or_xlsx_str}"
    data = fetch_obj_from_retired(self.connection)
    all_col = self.default_columns.copy()
    all_col.append("Retirement Date")
    if csv:
        write_iter_into_csv(all_col, data, file)
    else:  # excel export :D
        write_iter_into_excel(all_col, data, file)
    open_explorer_at_file(self, file)


def export_loc(self, csv: bool, file: str, place: str):
    csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
    file = f"{file}_LOCATION{csv_or_xlsx_str}"
    data = fetch_obj_from_loc(self.connection, place)
    if csv:
        write_iter_into_csv(self.default_columns, data, file)
    else:  # excel export :D
        write_iter_into_excel(self.default_columns, data, file)
    open_explorer_at_file(self, file)


def export_replacementdate(self, csv: bool, file: str, time_period: str, include_overdue):
    # time period is our 3, 6, 9, 12, 24 month period
    csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
    file = f"{file}_DUE-REPLACEMENT{csv_or_xlsx_str}"
    num = int(time_period.split(" ")[0])  # the number part of the '3 Months' or '12 Months'
    time_period = datetime.date.today() + dateutil.relativedelta.relativedelta(months=num)
    data = fetch_retired_assets(self.connection, time_period, include_overdue)
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
    letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    row_hex = "9A9C9B"
    active_ws = wb.active
    color = PatternFill(start_color=row_hex, end_color=row_hex, fill_type='solid')
    active_ws.append(columns)
    for count, row in enumerate(iterable):
        active_ws.append(row)
        if (count + 1) % 2 == 0:
            for letter in letter_list:
                active_ws[f'{letter}{count}'].fill = color                
    for col in letter_list:
        active_ws.column_dimensions[col].width = 20
    # we add +1 because indexes start at 0 in py, but start at one in excel..
    table = Table(displayName="exported", ref=f'A1:L{len(iterable) +1}')
    active_ws.add_table(table)
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
    self.display_message("Success!", f"Backup created successfully: {filename}")
    open_explorer_at_file(self, end_file)

def export_changed(self, csv: bool, file: str, month, year):
    # we are going to export the entire `changed` table
    csv_or_xlsx_str = ".csv" if csv is True else ".xlsx"
    data = fetch_changed_assets(self.connection, month, year)
    special_columns = ["Old Name", "New Name", "Old Location", "New Location", "Date Changed"]
    final_filename = f'changed_assets-{file}{csv_or_xlsx_str}'
    if csv:
        write_iter_into_csv(special_columns, data, file)
    else:  # excel export :D
        write_iter_into_excel(special_columns, data, file)
    open_explorer_at_file(self, file)
