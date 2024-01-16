from gui.auto import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from PyQt5.QtCore import QDate
from util.data_types import InventoryObject, TableObject
from db.fetch import fetch_all, fetch_all_for_table
from gui.notes_window import NotesWindow
from types import MethodType
from gui.insert_functions import update_replacement_date, refresh_asset_types, add_asset_type
from gui.add_item_window import GenericAddJsonWindow
class MainProgram(QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
          super().__init__(parent)
          self.setupUi(self)
          self.imported_methods()  # call the imported methods into scope of the class
          self.active_notes_window = None
          self.active_json_window = None
          # ui functions
          self.ham_menu_button.clicked.connect(self.toggle_burger)
          self.populate_table_with(fetch_all_for_table())
          self.ham_button_insert.clicked.connect(lambda: self.swap_to_window(1))
          self.ham_button_view.clicked.connect(lambda: self.swap_to_window(0))
          self.ham_button_analytics.clicked.connect(lambda: self.swap_to_window(2))
          self.ham_button_reports.clicked.connect(lambda: self.swap_to_window(3))
          self.insert_asset_type_combobox.currentIndexChanged.connect(self.update_replacement_date)
          self.insert_asset_type_combobox.addItems(self.refresh_asset_types())
          self.insert_status_bool.addItems(["Enabled", "Disabled"])
          # thr possible? might be quicker to load "non-visible by defualt" content on sep thread
          self.insert_install_date_fmt.setDate(QDate.currentDate())
          self.insert_purchase_date_fmt.setDate(QDate.currentDate())
          # leave the insert_replacement_date_fmt for when the user selects the hardware type
          self.insert_asset_category_add_option.clicked.connect(lambda: self.display_generic_json("Category"))
          self.insert_asset_type_add_option.clicked.connect(lambda: self.display_generic_json("Type"))
          self.insert_asset_location_add_option.clicked.connect(lambda: self.display_generic_json("Location"))
          
     def imported_methods(self):
          # for loop at some point? lmao
          self.update_replacement_date = MethodType(update_replacement_date, self)
          self.refresh_asset_types = MethodType(refresh_asset_types, self)

     def toggle_burger(self):
          if self.ham_menu_frame.height() == 250:
               self.ham_menu_frame.setFixedHeight(50)
               
          else:
               self.ham_menu_frame.setFixedHeight(250)

     def swap_to_window(self, index: int):
          self.stackedWidget.setCurrentIndex(index)
          # grey out button that is selected by index?
     

     def populate_table_with(self, data: [TableObject]):
          self.main_table.setRowCount(len(data))
          self.main_table.setColumnCount(len(data[0]))  # set the column count to the size of the first data piece
          for row, rowdata in enumerate(data):
               for col, value in enumerate(rowdata):
                    item = QTableWidgetItem(str(value))
                    if col == 11:
                         if value == '':
                              item = QTableWidgetItem("No Notes")
                         else:
                              button = self.generate_notes_button(data[row].uniqueid)
                              self.main_table.setCellWidget(row, col, button)
                              continue
                    else:
                         self.main_table.setItem(row, col, item)

     def generate_notes_button(self, uuid: str):  # uuid so we can update to the right column
          button = QPushButton()
          button.setText("View Notes")
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

     def filter_columns(self, *args):
          for selected_column in args:
              pass 

     def display_generic_json(self, target: str):
          self.active_json_window = GenericAddJsonWindow(target)
          self.active_json_window.show()
          position = self.pos()
          position.setX(position.x() + 250)
          position.setY(position.y() + 250)
          self.active_json_window.move(position)
