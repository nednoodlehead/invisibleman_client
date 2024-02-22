from PyQt5.QtWidgets import QWidget, QFrame, QLineEdit, QLabel, QPushButton, QFileDialog, QCheckBox
from PyQt5.QtCore import QRect, Qt, QCoreApplication
from PyQt5.QtGui import QFont
from data.visualization import DataCanvas
from volatile.write_to_volatile import read_from_config
from gui.settings import set_dark
from util.export import open_explorer_at_file
import datetime

class ExportGraph(QWidget):
     """
     window to export a graph to png to a specified directory!
     """
     def __init__(self, window, top: bool):
          super().__init__()
          self.window = window
          self.top = top
          self.config = read_from_config()
          self.setWindowTitle(f"Export {"Line/Bar" if top else "Pie/Donut"} Graph")
          if self.config["dark_mode"]:
               set_dark(self)
# ui auto-gen
          self.resize(441, 257)
          self.path_text = QLineEdit(self)
          self.path_text.setObjectName(u"path_text")
          self.path_text.setGeometry(QRect(100, 60, 271, 20))
          self.path_label = QLabel(self)
          self.path_label.setObjectName(u"path_label")
          self.path_label.setGeometry(QRect(10, 60, 81, 20))
          self.path_label.setLayoutDirection(Qt.LeftToRight)
          self.path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
          self.file_explorer_button = QPushButton(self)
          self.file_explorer_button.setObjectName(u"file_explorer_button")
          self.file_explorer_button.setGeometry(QRect(370, 60, 21, 21))
          self.export_button = QPushButton(self)
          self.export_button.setObjectName(u"export_button")
          self.export_button.setGeometry(QRect(130, 130, 201, 41))
          font = QFont()
          font.setPointSize(20)
          self.export_button.setFont(font)
          self.trim_whitespace_checkbox = QCheckBox(self)
          self.trim_whitespace_checkbox.setObjectName(u"trim_whitespace_checkbox")
          self.trim_whitespace_checkbox.setGeometry(QRect(100, 90, 131, 21))

          self.retranslateUi(self)

          # setupUi
          self.export_button.clicked.connect(self.export_graph)
          self.file_explorer_button.clicked.connect(self.open_file_dialog)
          self.path_text.setText(self.config["default_report_path"])

     def retranslateUi(self, Form):
          self.path_label.setText(QCoreApplication.translate("Form", u"Path", None))
          self.file_explorer_button.setText(QCoreApplication.translate("Form", u"..", None))
          self.export_button.setText(QCoreApplication.translate("Form", u"Export", None))
          self.trim_whitespace_checkbox.setText(QCoreApplication.translate("Form", u"TrimWhitespace", None))          # retranslateUi          # ui functionality
          
          
     def open_file_dialog(self):
          file_d = QFileDialog(self)
          file_d.setFileMode(QFileDialog.FileMode.DirectoryOnly)
          path = file_d.getExistingDirectory(self)
          if path is not None:
               self.path_text.setText(path)
       
     def export_graph(self):
          path = self.config["default_report_path"]  # TODO maybe make this its own config item!
          if not path.endswith("/") or path.endswith("\\"):
               path = path + "/"
          time_date = str(datetime.datetime.now()).replace(":", "-")[:19]
          if self.top:
               fig = self.window.graph_1
               fig_data = self.window.analytics_field_combobox_top.currentText()
               fig_type = self.window.analytics_field_combobox_top_2.currentText()
          else:
               fig = self.window.graph_2
               fig_data = self.window.analytics_field_combobox_bottom.currentText()
               fig_type = self.window.analytics_field_combobox_bottom_2.currentText()
          file = f'{path}{fig_type}_{fig_data}_{time_date}.png'
          fig.figure.savefig(file)
          open_explorer_at_file(self.window, file)
          self.close()
