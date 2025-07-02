from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QSpinBox, QLineEdit
from PyQt5.QtCore import QRect, QDate, QDateTime
from db.update import update_extras
from db.fetch import fetch_specific_extra
from db.insert import new_extra
from gui.settings import set_dark
from volatile.write_to_volatile import read_from_config
from util.data_types import ExtraObject


class ExtraWindow(QWidget):
    """
    separate window for viewing notes
    accessed from the notes button on a column
    """

    def __init__(self, conn, uuid: str):
        super().__init__()
        self.uuid = uuid
        self.conn = conn
        if uuid:
            to_change = fetch_specific_extra(
                conn,
                self.uuid
            )  # notes are found here so when updating with new notes, the button returns the right data
            print(to_change)
        self.setObjectName("Notes")
        self.config = read_from_config()
        if self.config["dark_mode"] is True:
            set_dark(self)
        # ngl editing the code from qt desinger sort of sucks..
        self.item_name_text = QLineEdit(self)
        self.item_name_text.setObjectName(u"item_name_text")
        self.item_name_text.setGeometry(QRect(10, 60, 113, 20))
        self.item_name_label = QLabel(self)
        self.item_name_label.setObjectName(u"item_name_label")
        self.item_name_label.setGeometry(QRect(10, 40, 101, 16))
        self.manufacturer_text = QLineEdit(self)
        self.manufacturer_text.setObjectName(u"manufacturer_text")
        self.manufacturer_text.setGeometry(QRect(140, 60, 113, 20))
        self.manufacturer_label = QLabel(self)
        self.manufacturer_label.setObjectName(u"manufacturer_label")
        self.manufacturer_label.setGeometry(QRect(140, 40, 101, 16))
        self.amount_number = QSpinBox(self)
        self.amount_number.setObjectName(u"amount_number")
        self.amount_number.setGeometry(QRect(260, 60, 41, 22))
        self.amount_text = QLabel(self)
        self.amount_text.setObjectName(u"amount_text")
        self.amount_text.setGeometry(QRect(260, 40, 61, 16))
        self.low_amount_text = QLabel(self)
        self.low_amount_text.setObjectName(u"low_amount_text")
        self.low_amount_text.setGeometry(QRect(310, 40, 61, 16))
        self.low_amount_number = QSpinBox(self)
        self.low_amount_number.setObjectName(u"low_amount_number")
        self.low_amount_number.setGeometry(QRect(310, 60, 51, 22))
        self.reserved_label = QLabel(self)
        self.reserved_label.setObjectName(u"reserved_label")
        self.reserved_label.setGeometry(QRect(380, 40, 61, 16))
        self.reserved_text = QLineEdit(self)
        self.reserved_text.setObjectName(u"reserved_text")
        self.reserved_text.setGeometry(QRect(380, 60, 61, 20))
        self.notes_label = QLabel(self)
        self.notes_label.setObjectName(u"notes_label")
        self.notes_label.setGeometry(QRect(460, 10, 51, 16))
        self.notes_text = QTextEdit(self)
        self.notes_text.setObjectName(u"notes_text")
        self.notes_text.setGeometry(QRect(460, 30, 191, 91))
        self.extra_add_button = QPushButton(self)
        self.extra_add_button.setObjectName(u"extra_add_button")
        self.extra_add_button.setGeometry(QRect(10, 110, 101, 23))
        self.item_name_label.setText(u"Item name:")
        self.manufacturer_text.setText("")
        self.manufacturer_label.setText(u"Manufacturer")
        self.amount_text.setText(u"Amount")
        self.low_amount_text.setText(u"Low amount")
        self.reserved_label.setText(u"Reserved")
        self.notes_label.setText(u"Notes")
        self.extra_add_button.setText(u"Add!")
        self.extra_add_button.clicked.connect(self.update_extras)
        
    def update_extras(self):
        # self.uuid will be a null when this window is initialized if it needs to be (aka we are inserting new, not updating)
        item = ExtraObject(self.item_name_text.text(), self.manufacturer_text.text(), int(self.amount_number.text()), int(self.low_amount_number.text()), self.reserved_text.text(), self.notes_text.toPlainText(), self.uuid)
        if self.uuid:
            # updating
            update_extras(self.conn, item)
        else:
            new_extra(self.conn, item)        
