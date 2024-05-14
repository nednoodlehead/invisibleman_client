from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QComboBox,
    QLineEdit,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from gui.insert_functions import (
    refresh_asset_categories,
    refresh_asset_location,
    refresh_asset_types,
    fetch_categories_and_years,
    replace_json_target,
)
from volatile.write_to_volatile import add_to_asset_list, add_to_type_or_location
from gui.settings import set_dark


class GenericAddJsonWindow(QWidget):
    def __init__(self, target: str, parent_window):
        super().__init__()
        self.target = target  # deciding what json file to write to
        self.parent_window = (
            parent_window  # used to tell parent to update the comboboxes when done
        )
        # value should be either: "Category", "Type", "Location"
        # should each of these have their own file? or one file?

        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        if parent_window.config["dark_mode"] is True:
            set_dark(self)
        self.json_write_to_button = QPushButton(self)
        self.json_write_to_button.setObjectName("json_write_to_button")
        self.json_write_to_button.setGeometry(QRect(370, 380, 75, 23))
        self.json_exit_button = QPushButton(self)
        self.json_exit_button.setObjectName("json_exit_button")
        self.json_exit_button.setGeometry(QRect(370, 410, 75, 23))
        self.json_new_value_text = QLineEdit(self)
        self.json_new_value_text.setObjectName("json_new_value_text")
        self.json_new_value_text.setGeometry(QRect(320, 30, 113, 20))
        self.json_new_value_label = QLabel(self)
        self.json_new_value_label.setObjectName("json_new_value_label")
        self.json_new_value_label.setGeometry(QRect(360, 10, 51, 16))
        self.json_conditional_years_text = QLineEdit(self)
        self.json_conditional_years_text.setObjectName("json_conditional_years_text")
        self.json_conditional_years_text.setGeometry(QRect(320, 120, 113, 20))
        self.json_conditional_years_label = QLabel(self)
        self.json_conditional_years_label.setObjectName("json_conditional_years_label")
        self.json_conditional_years_label.setGeometry(QRect(330, 90, 111, 21))
        self.json_value_frame = QFrame(self)
        self.json_value_frame.setObjectName("json_value_frame")
        self.json_value_frame.setGeometry(QRect(50, 0, 201, 441))
        self.json_value_frame.setFrameShape(QFrame.StyledPanel)
        self.json_value_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.json_value_frame)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, 0, 211, 441))
        self.json_value_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.json_value_layout.setObjectName("json_value_layout")
        self.json_value_layout.setContentsMargins(0, 0, 0, 0)
        self.json_years_frame = QFrame(self)
        self.json_years_frame.setObjectName("json_years_frame")
        self.json_years_frame.setGeometry(QRect(250, 0, 41, 441))
        self.json_years_frame.setStyleSheet("")
        self.json_years_frame.setFrameShape(QFrame.StyledPanel)
        self.json_years_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.json_years_frame)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 41, 441))
        self.json_years_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.json_years_layout.setObjectName("json_years_layout")
        self.json_years_layout.setContentsMargins(0, 0, 0, 0)
        self.json_button_frame = QFrame(self)
        self.json_button_frame.setObjectName("json_button_frame")
        self.json_button_frame.setGeometry(QRect(10, 0, 41, 441))
        self.json_button_frame.setFrameShape(QFrame.StyledPanel)
        self.json_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.json_button_frame)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 41, 441))
        self.json_button_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.json_button_layout.setObjectName("json_button_layout")
        self.json_button_layout.setContentsMargins(0, 0, 0, 0)
        self.json_add_new_value_button = QPushButton(self)
        self.json_add_new_value_button.setObjectName("json_add_new_value_button")
        self.json_add_new_value_button.setGeometry(QRect(330, 170, 91, 23))
        font1 = QFont()
        font1.setPointSize(8)
        self.json_add_new_value_button.setFont(font1)
        self.json_write_to_button.setText("Update")
        self.json_exit_button.setText("Exit")
        self.json_new_value_label.setText("Value")
        self.json_conditional_years_text.setText("")
        self.json_conditional_years_label.setText("Years until expiry")
        self.json_add_new_value_button.setText("Add new value")
        font1 = QFont()
        font1.setPointSize(8)
        self.json_add_new_value_button.setFont(font1)

        if self.target != "Category":
            self.json_conditional_years_label.hide()
            self.json_conditional_years_text.hide()
            self.json_years_frame.setStyleSheet("")
        self.fill_layout_with_content()
        self.json_value_frame.raise_()
        self.json_add_new_value_button.clicked.connect(self.add_new_value_from_user)
        self.json_write_to_button.clicked.connect(self.write_changes)

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

    def fill_layout_with_content(self):
        data = None
        if self.target == "Category":
            data = fetch_categories_and_years(self)
            for cate, years in data.items():
                self.json_value_layout.addWidget(QLineEdit(cate))
                self.json_years_layout.addWidget(QLineEdit(str(years)))
                button = self.make_x_button()
                self.json_button_layout.addWidget(button)

        else:
            if self.target == "Type":
                data = refresh_asset_types(self)
            else:
                data = refresh_asset_location(self)
            for item in data:
                self.json_value_layout.addWidget(QLineEdit(item))
                button = self.make_x_button()
                self.json_button_layout.addWidget(button)

    def make_x_button(
        self,
    ):  # func to make the x and delete button for the little psuedo-menu
        button = QPushButton("X")
        button.clicked.connect(lambda: self.button_remove_item(button))
        return button

    def button_remove_item(self, button):  # func to bind to the button, to remove row
        index = self.json_button_layout.indexOf(button)
        self.remove_wid(index)

    def remove_wid(self, index):
        parts = [self.json_value_layout, self.json_button_layout]
        if (
            self.target == "Category"
        ):  # if the additional rows exist, also affect that part :D
            parts.append(self.json_years_layout)
        for layout in parts:
            item = layout.itemAt(index)
            wid = item.widget()
            wid.setParent(None)

    def add_new_value_from_user(self):
        if not self.json_new_value_text.text() == "":
            current_index = len(self.json_button_layout) + 1
            if self.target == "Category":
                self.json_years_layout.addWidget(
                    QLineEdit(self.json_conditional_years_text.text())
                )
            self.json_value_layout.addWidget(QLineEdit(self.json_new_value_text.text()))
            button = self.make_x_button()
            self.json_button_layout.addWidget(button)
        else:
            self.parent_window.display_error_message("Error adding empty string!")

    def write_changes(self):
        length = range(
            self.json_value_layout.count()
        )  # get how many times we have to iter over layout to get all items
        if self.target == "Category":
            data = {}
            for index in length:
                key = self.json_value_layout.itemAt(index).widget().text()
                val = self.json_years_layout.itemAt(index).widget().text()
                data[key] = int(val)  # create dict key, val pair to put into json
        else:
            data = []
            for index in length:
                val = (
                    self.json_value_layout.itemAt(index).widget().text()
                )  # get the data from the combobox
                data.append(val)
        replace_json_target(self.target, data)  # replace the json with the new data
        self.parent_window.refresh_combobox(
            self.target
        )  # send signal to main window to refresh comboboxes
        self.close()
        # write changes to json file
        # probably just pull from the layouts and create a dict, then write it?
