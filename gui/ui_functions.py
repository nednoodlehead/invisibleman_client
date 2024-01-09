from gui.auto import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainProgram(QMainWindow, Ui_MainWindow):
     def __init__(self, parent=None):
          super().__init__(parent)
          self.setupUi(self)
          self.ham_menu_button.clicked.connect(self.hi)
          print("made it")

          
     def hi(self):
          print("hewwo")
