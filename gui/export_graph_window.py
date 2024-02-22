from PyQt5.QtWidgets import QWidget, QFrame, QLineEdit, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from data.visualization import DataCanvas
from volatile.write_to_volatile import read_from_config
from gui.settings import set_dark

class ExportGraph(QWidget):
     """
     window to export a graph to png to a specified directory!
     """
     def __init__(self, chart_type: str, data: str):
          super().__init__()

          self.config = read_from_config()
          if self.config["dark_mode"]:
               set_dark(self)
          # ui auto-gen
          self.graph_frame = QFrame(self)
          self.graph_frame.setObjectName(u"graph_frame")
          self.graph_frame.setGeometry(QRect(60, 20, 431, 211))
          self.graph_frame.setFrameShape(QFrame.StyledPanel)
          self.graph_frame.setFrameShadow(QFrame.Raised)
          self.path_text = QLineEdit(self)
          self.path_text.setObjectName(u"path_text")
          self.path_text.setGeometry(QRect(140, 280, 271, 20))
          self.path_label = QLabel("Path", self)
          self.path_label.setObjectName(u"path_label")
          self.path_label.setGeometry(QRect(50, 280, 81, 20))
          self.path_label.setLayoutDirection(Qt.LeftToRight)
          self.path_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
          self.y_axis_text = QLineEdit(self)
          self.y_axis_text.setObjectName(u"y_axis_text")
          self.y_axis_text.setGeometry(QRect(140, 320, 271, 20))
          self.y_axis_label = QLabel("Y Axis Values", self)
          self.y_axis_label.setObjectName(u"y_axis_label")
          self.y_axis_label.setGeometry(QRect(50, 320, 81, 20))
          self.y_axis_label.setLayoutDirection(Qt.LeftToRight)
          self.y_axis_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
          self.x_axis_text = QLineEdit(self)
          self.x_axis_text.setObjectName(u"x_axis_text")
          self.x_axis_text.setGeometry(QRect(140, 360, 271, 20))
          self.x_axis_label = QLabel("X Axis Values", self)
          self.x_axis_label.setObjectName(u"x_axis_label")
          self.x_axis_label.setGeometry(QRect(50, 360, 81, 20))
          self.x_axis_label.setLayoutDirection(Qt.LeftToRight)
          self.x_axis_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
          self.select_file_button = QPushButton("..", self)
          self.select_file_button.setObjectName(u"select_file_button")
          self.select_file_button.setGeometry(QRect(410, 280, 21, 21))
          self.update_button = QPushButton("Update View", self)
          self.update_button.setObjectName(u"update_button")
          self.update_button.setGeometry(QRect(230, 230, 75, 23))
          self.export_button = QPushButton("Export", self)
          self.export_button.setObjectName(u"export_button")
          self.export_button.setGeometry(QRect(170, 450, 201, 41))
          font = QFont()
          font.setPointSize(20)
          self.export_button.setFont(font)

          # ui functionality
          self.select_file_button.clicked.connect(self.open_file_dialog)
          self.canvas = DataCanvas(self.graph_frame)
          self.canvas.change_graph(data, chart_type)          
          
     def open_file_dialog(self):
          file_d = QFileDialog(self)
          file_d.setFileMode(QFileDialog.FileMode.DirectoryOnly)
          path = file_d.getExistingDirectory(self)
          if path is not None:
               self.path_text.setText(path)
