from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt



# THIS SOLVES AN ISSUE WHERE Null Replacement dates would always start at the top :sob:
# we evauluate it as the lowest, so we dont see these devices as much


class InvisManItem(QTableWidgetItem):
    def __lt__(self, other):
        if self.text() == "None":
            return False
        else:
            return self.text() > other.text()
