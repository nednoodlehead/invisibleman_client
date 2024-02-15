from gui.ui_functions import MainProgram
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtCore import Qt

# thank you: https://stackoverflow.com/questions/40817687/adding-functions-to-buttons-via-importing-pyqt5-ui
# idk why pyqt5 is so hard comparatively

def main():
     QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
     app = QApplication(sys.argv)
     ui = MainProgram()
     ui.show()
     sys.exit(app.exec_())

