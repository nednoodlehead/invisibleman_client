
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QPushButton, QComboBox, QLineEdit
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from volatile.write_to_volatile import add_to_asset_list, add_to_type_or_location

class GenericAddJsonWindow(QWidget):
     def __init__(self, target: str):
          super().__init__()
          self.target = target  # deciding what json file to write to
          # value should be either: "Category", "Type", "Location"
          # should each of these have their own file? or one file?
          self.json_info_label = QLabel(f"Add info for {self.target}", self)
          self.json_info_label.setObjectName("json_info_label")
          self.json_info_label.setGeometry(QRect(20, 20, 201, 16))
          self.json_add_button = QPushButton("Add", self)
          self.json_add_button.setObjectName(u"json_add_button")
          self.json_add_button.clicked.connect(self.get_values_and_process)
          self.json_add_button.setGeometry(QRect(20, 250, 75, 23))
          self.json_exit_button = QPushButton("Exit", self)
          self.json_exit_button.setObjectName(u"json_exit_button")
          self.json_exit_button.setGeometry(QRect(300, 250, 75, 23))
          self.json_value_text = QLineEdit(self)
          self.json_value_text.setObjectName(u"json_value_text")
          self.json_value_text.setGeometry(QRect(160, 60, 113, 20))
          self.insert_assigned_to_label = QLabel("Value", self)
          self.insert_assigned_to_label.setObjectName(u"insert_assigned_to_label")
          self.insert_assigned_to_label.setGeometry(QRect(40, 60, 110, 21))
          font = QFont()
          font.setPointSize(10)
          self.insert_assigned_to_label.setFont(font)
          self.json_conditional_text = QLineEdit(self)
          self.json_conditional_text.setObjectName(u"json_conditional_text")
          self.json_conditional_text.setGeometry(QRect(160, 100, 113, 20))
          self.json_conditional_years_label = QLabel("Years until expiry", self)
          self.json_conditional_years_label.setObjectName(u"json_conditional_years_label")
          self.json_conditional_years_label.setGeometry(QRect(40, 100, 110, 21))
          self.json_conditional_years_label.setFont(font)
          if self.target != "Category":
               self.json_conditional_text.hide()
               self.json_conditional_years_label.hide()

     def get_values_and_process(self):
          years = self.json_conditional_text.text()
          data = self.json_value_text.text()
          if years.isdigit():
               new_int = int(years)
               add_to_asset_list(data, new_int)
          else:
               add_to_type_or_location(data, self.target)
          self.close()
          # also need to send signal to main program to tell it to refresh the relevant combobox
