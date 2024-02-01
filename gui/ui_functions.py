from gui.auto import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QMessageBox, QMenu, QTableWidget, QCheckBox, QAction, QStyleFactory, QFileDialog
from PyQt5.QtCore import QDate, Qt, QDate, QFile, QTextStream
from PyQt5.QtGui import QCursor
from util.data_types import InventoryObject, TableObject, create_inventory_object
from util.export import export_all, export_eol, export_loc, export_ret
from db.fetch import fetch_all, fetch_all_for_table, fetch_from_uuid_to_update
from db.insert import new_entry
from db.update import update_full_obj
from gui.notes_window import NotesWindow
from gui.settings import dark_light_mode_switch, set_dark
from volatile.write_to_volatile import write_to_config, read_from_config
from types import MethodType
from gui.insert_functions import update_replacement_date, refresh_asset_types, add_asset_type, refresh_asset_categories, fetch_all_asset_types, refresh_asset_location
from gui.add_item_window import GenericAddJsonWindow
from datetime import datetime

class MainProgram(QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
          super().__init__(parent)
          self.setupUi(self)
          self.imported_methods()  # call the imported methods into scope of the class
          self.active_notes_window = None
          self.active_json_window = None
          self.default_columns = ["Name", "Serial Number", "Manufacturer", "Price", "Asset Category", "Asset Type", "Assigned To", "Asset Location",
                                 "Purchase Date", "Install Date", "Replacement Date", "Notes"]
          self.retired_asset_years = ["All", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008",
                                                               "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018",
                                                               "2019", "2020", "2021", "2022", "2023", "2024"]
          # self.setStyle(QStyleFactory.create("Fusion"))
          # there is some argument to use a QTableView instead of a QTableWidget, since the view better supports
          # M/V style programming, which would (in theory) significantly improve the performance of certain
          # operations, namely filtering. would require quite a lot of refactoring though. so maybe another time :)
          # https://stackoverflow.com/questions/6785481/how-to-implement-a-filter-option-in-qtablewidget
          # the concept is that QTableWidget has a built-in model, and a QTableView does not, so you can edit it
          # ui functions
          self.ham_menu_button.clicked.connect(self.toggle_burger)
          self.populate_table_with(fetch_all_for_table())
          self.ham_button_insert.clicked.connect(lambda: self.swap_to_window(1))
          self.ham_button_view.clicked.connect(lambda: self.swap_to_window(0))
          self.ham_button_analytics.clicked.connect(lambda: self.swap_to_window(2))
          self.ham_button_reports.clicked.connect(self.swap_reports_refresh)
          self.insert_asset_category_combobox.currentIndexChanged.connect(self.update_replacement_date)
          self.insert_insert_button.clicked.connect(self.check_data_and_insert)
          self.insert_clear_selections_button.clicked.connect(self.set_insert_data_to_default)
          self.refresh_table_button.clicked.connect(lambda: self.populate_table_with(fetch_all_for_table()))
          self.main_table.setSortingEnabled(True)
          self.view_columns_button.clicked.connect(self.view_button_reveal_checkboxes)
          self.settings_update_button.clicked.connect(self.write_config)
          self.filter_column_button.clicked.connect(self.handle_filter_request)
          self.filter_options_combobox.addItem("Global")
          self.filter_options_combobox.addItems(self.default_columns)
          self.reports_export_file_combobox.addItems(["Excel", "CSV"])
          self.reports_export_location_combobox.addItems(self.refresh_asset_location())
          self.reports_export_retired_assets_combobox.addItems(self.retired_asset_years)
          # allow us to reach settings
          self.actionSettings.triggered.connect(lambda: self.swap_to_window(4))
          self.settings_darkmode_checkbox.clicked.connect(lambda: dark_light_mode_switch(self, self.settings_darkmode_checkbox.isChecked()))
          # make all the checboxes checked by default and make the checkboxes do something when clicked
          # probably worth adding json support at some point, so when app is closed, it is written to json, and loaded on start
          self.config = read_from_config()
          if self.config["ham_menu_status"] is False:  # configure ham menu based on loaded config
               self.ham_menu_frame.setFixedHeight(50)
          if self.config["dark_mode"] is True:
               self.settings_darkmode_checkbox.setChecked(True)
               set_dark(self)
          else:
               self.setStyleSheet("QFrame#reports_export_frame{border: 1px solid black;\nborder-radius: 15px;}")
          # opens with height == 250, so no need to `else` set that..
          self.insert_widgets = [self.checkbox_name, self.checkbox_serial, self.checkbox_manufacturer, self.checkbox_price,
          self.checkbox_assetcategory, self.checkbox_assettype, self.checkbox_assignedto, self.checkbox_assetlocation, self.checkbox_purchasedate,
          self.checkbox_installdate, self.checkbox_replacementdate, self.checkbox_notes]
          for count, checkbox in enumerate(self.insert_widgets):
               self.handle_checkboxes_and_columns(count, checkbox)
          # populating combo boxes. "" is an empty default value 
          cat, typ, loc = self.fetch_all_asset_types()
          self.insert_asset_category_combobox.addItem("")
          self.insert_asset_type_combobox.addItem("")
          self.insert_asset_location_combobox.addItem("")
          self.insert_asset_category_combobox.addItems(cat)
          self.insert_asset_type_combobox.addItems(typ)
          self.insert_asset_location_combobox.addItems(loc)
          self.insert_status_bool.addItems(["Enabled", "Disabled"])
          # thr possible? might be quicker to load "non-visible by defualt" content on sep thread
          self.insert_install_date_fmt.setDate(QDate.currentDate())
          self.insert_purchase_date_fmt.setDate(QDate.currentDate())
          self.insert_price_spinbox.setMaximum(99999.99)
          # leave the insert_replacement_date_fmt for when the user selects the hardware type
          self.insert_asset_category_add_option.clicked.connect(lambda: self.display_generic_json("Category"))
          self.insert_asset_type_add_option.clicked.connect(lambda: self.display_generic_json("Type"))
          self.insert_asset_location_add_option.clicked.connect(lambda: self.display_generic_json("Location"))
          self.filter_clear_button.clicked.connect(self.clear_filter)
          self.export_file_dialog.clicked.connect(self.open_report_file_dialog)
          self.export_file_path_choice.setText(self.config["default_report_path"])
          self.reports_export_main_export_button.clicked.connect(self.interface_handle_export)
          # edit buttons
          self.set_table_size_and_headers(self.default_columns)
          self.main_table.setContextMenuPolicy(Qt.CustomContextMenu)
          self.main_table.customContextMenuRequested.connect(self.display_table_context_menu)
          
     # overwritten methods
     
     def closeEvent(self, event):
          self.write_config()
          event.accept()
          

     # regular methods
     def imported_methods(self):
          # for loop at some point? lmao
          self.update_replacement_date = MethodType(update_replacement_date, self)
          self.refresh_asset_types = MethodType(refresh_asset_types, self)
          self.refresh_asset_category = MethodType(refresh_asset_categories, self)
          self.refresh_asset_location = MethodType(refresh_asset_location, self)
          self.fetch_all_asset_types = MethodType(fetch_all_asset_types, self)

     def display_error_message(self, error: str):
          msg = QMessageBox()
          msg.setText(error)
          msg.setWindowTitle("Error")
          msg.exec_()

     def display_table_context_menu(self, position=None):
          menu = QMenu()
          menu.addAction("Update", lambda: self.send_update_data_to_insert(self.main_table.itemAt(position).row()))
          menu.exec_(QCursor.pos())

     def view_button_reveal_checkboxes(self):
          if self.view_toggle_frame.width() == 690:
               self.view_toggle_frame.setFixedWidth(80)
          else:
               self.view_toggle_frame.setFixedWidth(690)

     def handle_checkboxes_and_columns(self, column: int, box: QCheckBox):
          # box.clicked.connect(lambda: self.main_table.setColumnHidden(column, not box.isChecked))
          
          def button_target():
               self.main_table.setColumnHidden(column, not box.isChecked())
          # if you replace this function and col with lambda, it does not work. on god
          box.clicked.connect(button_target)
          if self.config["checkboxes"][self.default_columns[column]] is True:
               box.setChecked(True)               
          else:
               self.main_table.setColumnHidden(column, True)
               pass  # set setchecked false by default on startup?

     def tester(self):
          print("here")

     def open_report_file_dialog(self):
          filedialog = QFileDialog(self)
          filedialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
          path = filedialog.getExistingDirectory(self)
          if path is not None:
               self.export_file_path_choice.setText(path)
          
     def refresh_asset_value(self):
          # i dont see a scenario where the db would have different data than self.main_table
          total = 0
          for row_count in range(self.main_table.rowCount()):
               for column_count in range(self.main_table.columnCount()):
                    if column_count == 3:
                         item = self.main_table.item(row_count, column_count)
                         if item is not None:  # no reason to check for non int/float, since input is sanitized
                              total += (float(item.text()))
          # add commas between numbers...
          self.reports_asset_integer_label.setText(f"{total:,}")
                              
     def swap_reports_refresh(self):
          self.stackedWidget.setCurrentIndex(3)
          self.refresh_asset_value()

     def interface_handle_export(self):
          csv_val = True if self.reports_export_file_combobox.currentText() == "CSV" else False
          # ensure there is a / at the end :)
          user_file = self.export_file_path_choice.text()
          user_file = user_file if user_file.endswith("/") is False else f"{user_file}/"
          filename = f'{user_file}/{str(datetime.now()).replace(":", "-")[:19]}'  # should always end in a /, need to validate elsewhere
          if self.reports_export_export_all_radio.isChecked():
               export_all(self, csv_val, filename)
          elif self.reports_export_export_EOL_radio.isChecked():
               text = self.reports_export_EOL_text.text()
               if text is None:
                    self.display_error_message("End of Life Value not filled")          
               else:
                    export_eol(self, csv_val, filename, text)
          elif self.reports_export_export_location_radio.isChecked():
               # cant be none...
               export_loc(self, csv_val, filename, self.reports_export_location_combobox.currentText())
          elif self.reports_export_export_retired_radio.isChecked():
               # also cant be none, no null check required.. :)
               export_ret(self, csv_val, filename, self.reports_export_retired_assets_combobox.currentText())  # retired assets by year
          else:  # edge case where the user selects none of them
               self.display_error_message("Please select one of the radio buttons!")
               
     def send_update_data_to_insert(self, index):
          uuid = self.main_table.item(index, self.main_table.columnCount() -1).text()
          obj = fetch_from_uuid_to_update(uuid)
          self.swap_to_window(1)
          self.update_insert_page_from_obj(obj)

     def update_insert_page_from_obj(self, inventory_obj: InventoryObject):
          self.insert_name_text.setText(inventory_obj.name)
          self.insert_serial_text.setText(inventory_obj.serial)
          self.insert_manufacturer_text.setText(inventory_obj.manufacturer)
          self.insert_price_spinbox.setValue(float(inventory_obj.price))
          cat_index = self.insert_asset_category_combobox.findText(inventory_obj.assetcategory)
          self.insert_asset_category_combobox.setCurrentIndex(cat_index)
          type_index = self.insert_asset_type_combobox.findText(inventory_obj.assettype)
          self.insert_asset_type_combobox.setCurrentIndex(type_index)
          loc_index = self.insert_asset_location_combobox.findText(inventory_obj.assetlocation)
          self.insert_asset_location_combobox.setCurrentIndex(loc_index)
          self.insert_assigned_to_text.setText(inventory_obj.assignedto)
          self.insert_purchase_date_fmt.setDate(datetime.fromisoformat(inventory_obj.purchasedate))
          self.insert_install_date_fmt.setDate(datetime.fromisoformat(inventory_obj.installdate))
          self.insert_replacement_date_fmt.setDate(datetime.fromisoformat(inventory_obj.replacementdate))
          self.insert_notes_text.setText(inventory_obj.notes)
          if self.insert_status_bool == 0:
               self.insert_status_bool.setCurrentIndex(1)
          else:
               self.insert_status_bool.setCurrentIndex(0)
          self.insert_uuid_text.setText(inventory_obj.uniqueid)
          
                              
     def toggle_burger(self):
          if self.ham_menu_frame.height() == 250:
               self.ham_menu_frame.setFixedHeight(50)
               
          else:
               self.ham_menu_frame.setFixedHeight(250)

     def swap_to_window(self, index: int):
          self.stackedWidget.setCurrentIndex(index)
          # grey out button that is selected by index?

     def write_config(self):
          # get checkbox value
          report_export = True
          to_write = {
               "Name": self.checkbox_name.isChecked(),
               "Serial Number": self.checkbox_serial.isChecked(),
               "Manufacturer": self.checkbox_manufacturer.isChecked(),
               "Price": self.checkbox_price.isChecked(),
               "Asset Category": self.checkbox_assetcategory.isChecked(),
               "Asset Type": self.checkbox_assettype.isChecked(),
               "Assigned To": self.checkbox_assignedto.isChecked(),
               "Asset Location": self.checkbox_assetlocation.isChecked(),
               "Purchase Date": self.checkbox_purchasedate.isChecked(),
               "Install Date": self.checkbox_installdate.isChecked(),
               "Replacement Date": self.checkbox_replacementdate.isChecked(),
               "Notes": self.checkbox_notes.isChecked()
          }
          checked = True if self.ham_menu_frame.height() == 250 else False
          write_to_config(checked, to_write, self.settings_darkmode_checkbox.isChecked(),
                          self.settings_backup_dir_text.text(), report_export, self.export_file_path_choice.text())
     

     def populate_table_with(self, data: [TableObject]):
          self.main_table.setRowCount(len(data))
          self.main_table.setColumnCount(len(data[0]))  # set the column count to the size of the first data piece
          for row, rowdata in enumerate(data):
               for col, value in enumerate(rowdata):
                    item = QTableWidgetItem(str(value))
                    if col == 11:
                         if value == '':
                              button = self.generate_notes_button(data[row].uniqueid, "Add Notes")                              
                              self.main_table.setCellWidget(row, col, button)
                         else:
                              button = self.generate_notes_button(data[row].uniqueid, "View Notes")
                              self.main_table.setCellWidget(row, col, button)
                    else:
                         self.main_table.setItem(row, col, item)

     def generate_notes_button(self, uuid: str, display: str):  # uuid so we can update to the right column
          button = QPushButton()
          button.setText(display)
          button.clicked.connect(lambda: self.display_notes(uuid))
          return button
          

     def display_notes(self, uuid: str):
          # will be a text box 
          self.active_notes_window = NotesWindow(uuid)
          self.active_notes_window.show()
          position = self.pos()
          position.setX(position.x() + 250)
          position.setY(position.y() + 250)
          self.active_notes_window.move(position)      

     
     def display_generic_json(self, target: str):
          self.active_json_window = GenericAddJsonWindow(target, self)
          self.active_json_window.show()
          position = self.pos()
          position.setX(position.x() + 250)
          position.setY(position.y() + 250)
          self.active_json_window.move(position)

     def refresh_combobox(self, target: str):
          if target == "Category":
               self.insert_asset_category_combobox.clear()
               self.insert_asset_category_combobox.addItem("")
               self.insert_asset_category_combobox.addItems(self.refresh_asset_category())
          elif target == "Type":
               self.insert_asset_type_combobox.clear()
               self.insert_asset_type_combobox.addItem("")
               self.insert_asset_type_combobox.addItems(self.refresh_asset_types())
          else:
               self.insert_asset_location_combobox.clear()
               self.insert_asset_location_combobox.addItem("")
               self.insert_asset_location_combobox.addItems(self.refresh_asset_location())

     def check_data_and_insert(self):
          required = {"Serial": self.insert_serial_text, "Manufacturer": self.insert_manufacturer_text, "Asset Category":self.insert_asset_category_combobox,
          "Asset Type": self.insert_asset_type_combobox, "Asset Location": self.insert_asset_location_combobox}
          missing = []
          for name, item in required.items():
               try:
                    if item.text() == "":
                         missing.append(name)
               except AttributeError:  # comboboxes !!
                    if item.currentText() == "":
                         missing.append(name)
          if len(missing) != 0:
               self.display_error_message(f"Missing fields: {missing}")
          else:
               # we are creating a new entry if this is an empty value 
               if self.insert_uuid_text.text() == '':
                    
                    obj = create_inventory_object(self.insert_name_text.text(), self.insert_serial_text.text(), self.insert_manufacturer_text.text(),
                                            self.insert_price_spinbox.text(), self.insert_asset_category_combobox.currentText(), self.insert_asset_type_combobox.currentText(),
                                            self.insert_assigned_to_text.text(), self.insert_asset_location_combobox.currentText(), self.insert_purchase_date_fmt.text(), 
                                            self.insert_install_date_fmt.text(), self.insert_replacement_date_fmt.text(), self.insert_notes_text.toPlainText(),
                                            self.insert_status_bool.currentText())
                    new_entry(obj)               
               else:
                    # we are updating an existing entry! (since the uuid string was set)
                    obj = InventoryObject(self.insert_name_text.text(), self.insert_serial_text.text(), self.insert_manufacturer_text.text(), self.insert_price_spinbox.text(),
                                          self.insert_asset_category_combobox.currentText(), self.insert_asset_type_combobox.currentText(), self.insert_assigned_to_text.text(), self.insert_asset_location_combobox.currentText(),
                                          self.insert_purchase_date_fmt.text(), self.insert_install_date_fmt.text(), self.insert_replacement_date_fmt.text(),
                                          self.insert_notes_text.toPlainText(), self.insert_status_bool.currentText(), self.insert_uuid_text.text())
                    update_full_obj(obj)
               self.set_insert_data_to_default()
               self.populate_table_with(fetch_all_for_table())  # this will overwrite any filters / views

     def set_insert_data_to_default(self):
          today = QDate.currentDate()
          self.insert_name_text.setText("")
          self.insert_serial_text.setText("")
          self.insert_manufacturer_text.setText("")
          self.insert_price_spinbox.setValue(0.00)
          self.insert_asset_category_combobox.setCurrentIndex(0)  # to the empty string!
          self.insert_asset_type_combobox.setCurrentIndex(0)
          self.insert_asset_location_combobox.setCurrentIndex(0)
          self.insert_assigned_to_text.setText("")
          self.insert_purchase_date_fmt.setDate(today)
          self.insert_install_date_fmt.setDate(today)
          self.insert_replacement_date_fmt.setDate(today)
          self.insert_notes_text.setText("")
          self.insert_status_bool.setCurrentIndex(0)
          self.insert_uuid_text.setText("")

     def set_table_size_and_headers(self, headers: [str]):
          # kept sort of abigious since headers can be changed. if it was always all the headers it could be hardcoded
          headers.append("UUID")
          length = len(headers)
          self.main_table.setColumnCount(length)
          self.main_table.setHorizontalHeaderLabels(headers)
          # set the sizes of certain columns as needed
          for count, column_title in enumerate(headers):
               if column_title == "Asset Category":
                    header = self.main_table.columnWidth(count)
                    # maybe value should be calculated based off the longest string from the relevant json
                    self.main_table.setColumnWidth(count, 150)
               elif column_title == "Replacement Date":
                    self.main_table.setColumnWidth(count, 120)
          # alternating row colors :D
          self.main_table.setAlternatingRowColors(True)
          self.main_table.setColumnHidden(length -1, True)  # must be done here
               
     def filter_all_columns(self, word: str):
          for row_num in range(self.main_table.rowCount()):
               match = False
               for col_num in range(self.main_table.columnCount()):
                    cell = self.main_table.item(row_num, col_num)
                    if cell is None:
                         continue
                    else:
                         cell_content = cell.text()
                         if word in cell_content:
                              match = True
                              break
               if match is False:
                    self.main_table.setRowHidden(row_num, True)
                    
     def filter_certain_column(self, word: str, column: int):
          for row_num in range(self.main_table.rowCount()):
               match = False
               for col_num in range(self.main_table.columnCount()):
                    if col_num != column:
                         continue
                         cell = self.main_table.item(row_num, col_num)
                         if word in cell:
                              match = True
                              break  # break is logically implied, but since it would search meaningless columns...
               if match is False:
                    self.main_table.setRowHidden(row_num, True)
               

     def handle_filter_request(self):
          word = self.filter_user_text.text()
          category = self.filter_options_combobox.currentText()
          if category != "Global":
               column = self.default_columns.index(category)
               self.filter_certain_column(word, column)
          else:
               self.filter_all_columns(word)
               
     def clear_filter(self):
          for count in range(self.main_table.rowCount()):
               self.main_table.setRowHidden(count, False)
               
                              
          
               
