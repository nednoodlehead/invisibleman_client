# ok, so maybe there is an actual argument for using PyQt5.QtCore.QSettings, but it seems like
# honestly more work than just a json that i dump into and read on start
# plus it is probably easier to externally configure if something goes wrong with the appplication
from PyQt5.QtWidgets import QWidget, QStyleFactory
from PyQt5.QtGui import QPalette, QColor, QGuiApplication
from PyQt5.QtCore import Qt, QFile, QTextStream
# flip for dark / light mode



def dark_light_mode_switch(self: QWidget, is_dark: bool):  # cant do MainProgram cause of circular import :(
     if is_dark:
          set_dark(self)
     else:
          print("SWAP!!")
          self.setStyleSheet("QFrame#reports_export_frame{border: 1px solid black;\nborder-radius: 15px;}")  # lol bye bye style sheet 
          # resets it to default bte
     
def set_dark(self):
     file = QFile("./gui/styles/dark.qss")
     file.open(QFile.ReadOnly | QFile.Text)
     stream = QTextStream(file)
     self.setStyleSheet(stream.readAll())
