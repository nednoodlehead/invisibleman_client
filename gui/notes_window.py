from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import QRect, QDate, QDateTime
from db.update import update_notes
from db.fetch import fetch_notes_from_uuid
from gui.settings import set_dark
from volatile.write_to_volatile import read_from_config


class NotesWindow(QWidget):
    """
    separate window for viewing notes
    accessed from the notes button on a column
    """

    def __init__(self, uuid: str):
        super().__init__()
        self.uuid = uuid
        notes = fetch_notes_from_uuid(
            self.uuid
        )  # notes are found here so when updating with new notes, the button returns the right data
        self.setObjectName("Notes")
        self.label = QLabel("Notes")
        self.setGeometry(0, 0, 600, 500)
        self.label.setGeometry(0, 0, 50, 50)
        self.config = read_from_config()
        if self.config["dark_mode"] is True:
            set_dark(self)
        self.notes_window_note_browser = QTextEdit(notes, self)
        self.notes_window_note_browser.setObjectName("notes_window_note_browser")
        self.notes_window_note_browser.setGeometry(QRect(40, 30, 500, 290))
        self.notes_window_note_browser.setReadOnly(False)
        self.notes_window_update_text = QPushButton("Update", self)
        self.notes_window_update_text.setObjectName("notes_window_update_text")
        self.notes_window_update_text.clicked.connect(self.update_notes)
        self.notes_window_delete_text = QPushButton("Delete Text", self)
        self.notes_window_delete_text.move(450, 330)
        self.notes_window_update_text.move(40, 330)
        self.feedback_label = QLabel("", self)
        self.feedback_label.setGeometry(0, 0, 150, 50)
        self.feedback_label.move(40, 360)

    def update_notes(self):
        notes = self.notes_window_note_browser.toPlainText()
        update_notes(notes, self.uuid)
        time = QDateTime.currentDateTime()
        str_ver = time.toString("HH:mm:ss")
        self.feedback_label.setText(f"Last written: {str_ver}")
