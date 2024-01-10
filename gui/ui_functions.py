from gui.auto import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton
from util.data_types import InventoryObject, TableObject
from db.fetch import fetch_all, fetch_all_for_table

class MainProgram(QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
          super().__init__(parent)
          self.setupUi(self)
          self.ham_menu_button.clicked.connect(self.toggle_burger)
          self.populate_table_with(fetch_all_for_table())
          
          
     def toggle_burger(self):
          if self.ham_menu_frame.height() == 200:
               self.ham_menu_frame.setFixedHeight(50)
               
          else:
               self.ham_menu_frame.setFixedHeight(200)
     

     def populate_table_with(self, data: [TableObject]):
          self.main_table.setRowCount(len(data))
          self.main_table.setColumnCount(13)  # we dont display 'enabled'
          for row, rowdata in enumerate(data):
               print(rowdata)
               for col, value in enumerate(rowdata):
                    item = QTableWidgetItem(str(value))
                    if col == 11:
                         if value == '':
                              item = QTableWidgetItem("No Notes")
                         else:
                              button = self.generate_notes_button(value)
                              self.main_table.setCellWidget(row, col, button)
                              continue
                    else:
                         print(f'value: {value} {row} {col} item: {item}')
                         self.main_table.setItem(row, col, item)
     def generate_notes_button(self, notes):
          button = QPushButton()
          button.setText("View Notes")
          button.clicked.connect(lambda: self.display_notes(notes))
          return button
          

     def display_notes(self, notes: str):
          # will be a text box 
          print(f'notes :DD {notes} {type(notes)}')
