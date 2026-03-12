# ok, so maybe there is an actual argument for using PyQt5.QtCore.QSettings, but it seems like
# honestly more work than just a json that i dump into and read on start
# plus it is probably easier to externally configure if something goes wrong with the appplication
from PyQt5.QtWidgets import QWidget, QStyleFactory
from PyQt5.QtGui import QPalette, QColor, QGuiApplication
from PyQt5.QtCore import Qt, QFile, QTextStream

# flip for dark / light mode


def dark_light_mode_switch(
    self: QWidget, is_dark: bool
):  # cant do MainProgram cause of circular import :(
    if is_dark:
        set_dark(self)
    else:
        set_light(self)
        # additional style sheets... smh
        # resets it to default bte
    # somewhat niche scneario updating the colors on the months when the color is switched..
    self.update_month_colors()


def set_dark(self):
    file = QFile("./gui/styles/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    self.setStyleSheet(stream.readAll())

def set_light(self):
    # extra settings for being in light mode..
    self.setStyleSheet(
    """
    QFrame#reports_export_frame {
        border: 1px solid black;
        border-radius: 15px;
    }
    QFrame#reports_utilities_frame {
        border: 1px solid black;
        border-radius: 15px;
    }
    QCalendarWidget QAbstractItemView:disabled {
        color: transparent;
    }
    """
    )  # lol bye bye style sheet
    self.update_month_colors()

