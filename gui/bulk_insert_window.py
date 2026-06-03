
from PyQt5.QtCore import (QCoreApplication, QDate, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from gui.settings import set_dark
from datetime import datetime
from util.data_types import InventoryObject
from db.insert import bulk_insert
import openpyxl
import json
from dateutil.relativedelta import relativedelta

class BulkWindow(QWidget):
    def __init__(self, parent_window):
        super().__init__()
        if parent_window.config["dark_mode"] is True:
            set_dark(self)
        self.parent_window = parent_window
        
        self.setObjectName(u"self")
        self.resize(962, 601)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(326, 22, 131, 41))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(620, 60, 171, 16))
        self.bulk_file_path_text = QLineEdit(self)
        self.bulk_file_path_text.setObjectName(u"bulk_file_path_text")
        self.bulk_file_path_text.setGeometry(QRect(580, 80, 281, 20))
        self.bulk_file_text_file_browse = QPushButton(self)
        self.bulk_file_text_file_browse.setObjectName(u"bulk_file_text_file_browse")
        self.bulk_file_text_file_browse.setGeometry(QRect(860, 80, 31, 23))
        self.bulk_conditional_excel_headers_frame = QFrame(self)
        self.bulk_conditional_excel_headers_frame.setObjectName(u"bulk_conditional_excel_headers_frame")
        self.bulk_conditional_excel_headers_frame.setGeometry(QRect(620, 110, 211, 80))
        self.bulk_conditional_excel_headers_frame.setFrameShape(QFrame.StyledPanel)
        self.bulk_conditional_excel_headers_frame.setFrameShadow(QFrame.Raised)
        self.bulk_conditional_excel_headers_checkbox = QCheckBox(self.bulk_conditional_excel_headers_frame)
        self.bulk_conditional_excel_headers_checkbox.setObjectName(u"bulk_conditional_excel_headers_checkbox")
        self.bulk_conditional_excel_headers_checkbox.setGeometry(QRect(10, 30, 141, 21))
        self.bulk_preset_combobox = QComboBox(self)
        self.bulk_preset_combobox.setObjectName(u"bulk_preset_combobox")
        self.bulk_preset_combobox.setGeometry(QRect(620, 220, 211, 22))
        self.bulk_preset_combobox.setEditable(True)
        self.label_asset_type = QLabel(self)
        self.label_asset_type.setObjectName(u"label_asset_type")
        self.label_asset_type.setGeometry(QRect(30, 50, 231, 15))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_asset_type.setFont(font1)
        self.label_asset_type.setAlignment(Qt.AlignCenter)
        self.label_manufacturer = QLabel(self)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        self.label_manufacturer.setGeometry(QRect(30, 95, 231, 15))
        self.label_manufacturer.setFont(font1)
        self.label_manufacturer.setAlignment(Qt.AlignCenter)
        self.bulk_column_prefilled_serial = QLineEdit(self)
        self.bulk_column_prefilled_serial.setObjectName(u"bulk_column_prefilled_serial")
        self.bulk_column_prefilled_serial.setGeometry(QRect(20, 150, 121, 20))
        self.label_cost = QLabel(self)
        self.label_cost.setObjectName(u"label_cost")
        self.label_cost.setGeometry(QRect(30, 215, 231, 15))
        self.label_cost.setFont(font1)
        self.label_cost.setAlignment(Qt.AlignCenter)
        self.label_serial = QLabel(self)
        self.label_serial.setObjectName(u"label_serial")
        self.label_serial.setGeometry(QRect(20, 135, 231, 15))
        self.label_serial.setFont(font1)
        self.label_serial.setAlignment(Qt.AlignCenter)
        self.bulk_column_prefilled_device = QLineEdit(self)
        self.bulk_column_prefilled_device.setObjectName(u"bulk_column_prefilled_device")
        self.bulk_column_prefilled_device.setGeometry(QRect(20, 310, 121, 20))
        self.label_category = QLabel(self)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(30, 375, 231, 15))
        self.label_category.setFont(font1)
        self.label_category.setAlignment(Qt.AlignCenter)
        self.bulk_column_prefilled_assigned = QLineEdit(self)
        self.bulk_column_prefilled_assigned.setObjectName(u"bulk_column_prefilled_assigned")
        self.bulk_column_prefilled_assigned.setGeometry(QRect(20, 270, 121, 20))
        self.label_assignedto = QLabel(self)
        self.label_assignedto.setObjectName(u"label_assignedto")
        self.label_assignedto.setGeometry(QRect(30, 255, 231, 15))
        self.label_assignedto.setFont(font1)
        self.label_assignedto.setAlignment(Qt.AlignCenter)
        self.label_name = QLabel(self)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(30, 295, 231, 15))
        self.label_name.setFont(font1)
        self.label_name.setAlignment(Qt.AlignCenter)
        self.label_location = QLabel(self)
        self.label_location.setObjectName(u"label_location")
        self.label_location.setGeometry(QRect(30, 335, 231, 15))
        self.label_location.setFont(font1)
        self.label_location.setAlignment(Qt.AlignCenter)
        self.bulk_column_prefilled_cost = QDoubleSpinBox(self)
        self.bulk_column_prefilled_cost.setObjectName(u"bulk_column_prefilled_cost")
        self.bulk_column_prefilled_cost.setGeometry(QRect(20, 230, 121, 22))
        self.label_islocal = QLabel(self)
        self.label_islocal.setObjectName(u"label_islocal")
        self.label_islocal.setGeometry(QRect(30, 460, 231, 15))
        self.label_islocal.setFont(font1)
        self.label_islocal.setAlignment(Qt.AlignCenter)
        self.label_deploymentdate = QLabel(self)
        self.label_deploymentdate.setObjectName(u"label_deploymentdate")
        self.label_deploymentdate.setGeometry(QRect(30, 415, 231, 15))
        self.label_deploymentdate.setFont(font1)
        self.label_deploymentdate.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 470, 120, 25))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.bulk_column_prefilled_is_local_yes = QRadioButton(self.frame_2)
        self.bulk_column_prefilled_is_local_yes.setObjectName(u"bulk_column_prefilled_is_local_yes")
        self.bulk_column_prefilled_is_local_yes.setGeometry(QRect(10, 10, 41, 17))
        self.bulk_column_prefilled_is_local_no = QRadioButton(self.frame_2)
        self.bulk_column_prefilled_is_local_no.setObjectName(u"bulk_column_prefilled_is_local_no")
        self.bulk_column_prefilled_is_local_no.setGeometry(QRect(70, 10, 51, 17))
        self.bulk_save_profile = QPushButton(self)
        self.bulk_save_profile.setObjectName(u"bulk_save_profile")
        self.bulk_save_profile.setGeometry(QRect(620, 250, 101, 23))
        self.frame_3 = QFrame(self)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 510, 120, 25))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.bulk_column_prefilled_is_retired_yes = QRadioButton(self.frame_3)
        self.bulk_column_prefilled_is_retired_yes.setObjectName(u"bulk_column_prefilled_is_retired_yes")
        self.bulk_column_prefilled_is_retired_yes.setGeometry(QRect(10, 10, 41, 17))
        self.bulk_column_prefilled_is_retired_no = QRadioButton(self.frame_3)
        self.bulk_column_prefilled_is_retired_no.setObjectName(u"bulk_column_prefilled_is_retired_no")
        self.bulk_column_prefilled_is_retired_no.setGeometry(QRect(70, 10, 51, 17))
        self.label_isretired = QLabel(self)
        self.label_isretired.setObjectName(u"label_isretired")
        self.label_isretired.setGeometry(QRect(30, 505, 231, 12))
        self.label_isretired.setFont(font1)
        self.label_isretired.setAlignment(Qt.AlignCenter)
        self.label_notes = QLabel(self)
        self.label_notes.setObjectName(u"label_notes")
        self.label_notes.setGeometry(QRect(30, 544, 231, 13))
        self.label_notes.setFont(font1)
        self.label_notes.setAlignment(Qt.AlignCenter)
        self.bulk_column_prefilled_notes = QLineEdit(self)
        self.bulk_column_prefilled_notes.setObjectName(u"bulk_column_prefilled_notes")
        self.bulk_column_prefilled_notes.setGeometry(QRect(20, 560, 121, 20))
        self.bulk_column_number_asset = QLineEdit(self)
        self.bulk_column_number_asset.setObjectName(u"bulk_column_number_asset")
        self.bulk_column_number_asset.setGeometry(QRect(190, 70, 41, 20))
        self.bulk_column_number_manu = QLineEdit(self)
        self.bulk_column_number_manu.setObjectName(u"bulk_column_number_manu")
        self.bulk_column_number_manu.setGeometry(QRect(190, 110, 41, 20))
        self.bulk_column_number_cost = QLineEdit(self)
        self.bulk_column_number_cost.setObjectName(u"bulk_column_number_cost")
        self.bulk_column_number_cost.setGeometry(QRect(190, 230, 41, 20))
        self.bulk_column_number_serial = QLineEdit(self)
        self.bulk_column_number_serial.setObjectName(u"bulk_column_number_serial")
        self.bulk_column_number_serial.setGeometry(QRect(190, 150, 41, 20))
        self.bulk_column_number_category = QLineEdit(self)
        self.bulk_column_number_category.setObjectName(u"bulk_column_number_category")
        self.bulk_column_number_category.setGeometry(QRect(190, 390, 41, 20))
        self.bulk_column_number_location = QLineEdit(self)
        self.bulk_column_number_location.setObjectName(u"bulk_column_number_location")
        self.bulk_column_number_location.setGeometry(QRect(190, 350, 41, 20))
        self.bulk_column_number_name = QLineEdit(self)
        self.bulk_column_number_name.setObjectName(u"bulk_column_number_name")
        self.bulk_column_number_name.setGeometry(QRect(190, 310, 41, 20))
        self.bulk_column_number_assigned = QLineEdit(self)
        self.bulk_column_number_assigned.setObjectName(u"bulk_column_number_assigned")
        self.bulk_column_number_assigned.setGeometry(QRect(190, 270, 41, 20))
        self.bulk_column_number_deployment = QLineEdit(self)
        self.bulk_column_number_deployment.setObjectName(u"bulk_column_number_deployment")
        self.bulk_column_number_deployment.setGeometry(QRect(190, 435, 41, 20))
        self.bulk_column_number_local = QLineEdit(self)
        self.bulk_column_number_local.setObjectName(u"bulk_column_number_local")
        self.bulk_column_number_local.setGeometry(QRect(190, 480, 41, 20))
        self.bulk_column_number_retired = QLineEdit(self)
        self.bulk_column_number_retired.setObjectName(u"bulk_column_number_retired")
        self.bulk_column_number_retired.setGeometry(QRect(190, 520, 41, 20))
        self.bulk_column_number_notes = QLineEdit(self)
        self.bulk_column_number_notes.setObjectName(u"bulk_column_number_notes")
        self.bulk_column_number_notes.setGeometry(QRect(190, 560, 41, 20))
        self.bulk_column_prefilled_deployment = QDateEdit(self)
        self.bulk_column_prefilled_deployment.setObjectName(u"bulk_column_prefilled_deployment")
        self.bulk_column_prefilled_deployment.setGeometry(QRect(20, 435, 110, 22))
        self.bulk_column_prefilled_location = QComboBox(self)
        self.bulk_column_prefilled_location.setObjectName(u"bulk_column_prefilled_location")
        self.bulk_column_prefilled_location.setGeometry(QRect(20, 350, 120, 20))
        self.bulk_column_prefilled_category = QComboBox(self)
        self.bulk_column_prefilled_category.setObjectName(u"bulk_column_prefilled_category")
        self.bulk_column_prefilled_category.setGeometry(QRect(20, 395, 120, 20))
        self.bulk_column_prefilled_asset = QComboBox(self)
        self.bulk_column_prefilled_asset.setObjectName(u"bulk_column_prefilled_asset")
        self.bulk_column_prefilled_asset.setGeometry(QRect(20, 70, 120, 20))
        self.bulk_insert_button = QPushButton(self)
        self.bulk_insert_button.setObjectName(u"bulk_insert_button")
        self.bulk_insert_button.setGeometry(QRect(690, 500, 91, 31))
        self.bulk_column_prefilled_manu = QComboBox(self)
        self.bulk_column_prefilled_manu.setObjectName(u"bulk_column_prefilled_manu")
        self.bulk_column_prefilled_manu.setGeometry(QRect(20, 110, 121, 22))
        self.bulk_column_prefilled_model = QLineEdit(self)
        self.bulk_column_prefilled_model.setObjectName(u"bulk_column_prefilled_model")
        self.bulk_column_prefilled_model.setGeometry(QRect(20, 190, 121, 20))
        self.label_serial_2 = QLabel(self)
        self.label_serial_2.setObjectName(u"label_serial_2")
        self.label_serial_2.setGeometry(QRect(20, 175, 231, 15))
        self.label_serial_2.setFont(font1)
        self.label_serial_2.setAlignment(Qt.AlignCenter)
        self.bulk_column_number_model = QLineEdit(self)
        self.bulk_column_number_model.setObjectName(u"bulk_column_number_model")
        self.bulk_column_number_model.setGeometry(QRect(190, 190, 41, 20))

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("bulk_insert_window", u"Form", None))
        self.label.setText(QCoreApplication.translate("bulk_insert_window", u"Bulk Insert", None))
        self.label_2.setText(QCoreApplication.translate("bulk_insert_window", u"Path of file (csv & xlsx supported)", None))
        self.bulk_file_text_file_browse.setText(QCoreApplication.translate("bulk_insert_window", u"...", None))
        self.bulk_conditional_excel_headers_checkbox.setText(QCoreApplication.translate("bulk_insert_window", u"My excel file has headers", None))
        self.label_asset_type.setText(QCoreApplication.translate("bulk_insert_window", u"Asset Type", None))
        self.label_manufacturer.setText(QCoreApplication.translate("bulk_insert_window", u"Manufacturer", None))
        self.label_cost.setText(QCoreApplication.translate("bulk_insert_window", u"Cost", None))
        self.label_serial.setText(QCoreApplication.translate("bulk_insert_window", u"Serial Number", None))
        self.label_category.setText(QCoreApplication.translate("bulk_insert_window", u"Asset Category", None))
        self.label_assignedto.setText(QCoreApplication.translate("bulk_insert_window", u"Assigned to", None))
        self.label_name.setText(QCoreApplication.translate("bulk_insert_window", u"Device Name", None))
        self.label_location.setText(QCoreApplication.translate("bulk_insert_window", u"Asset Location", None))
        self.label_islocal.setText(QCoreApplication.translate("bulk_insert_window", u"Is local", None))
        self.label_deploymentdate.setText(QCoreApplication.translate("bulk_insert_window", u"Deployment Date", None))
        self.bulk_column_prefilled_is_local_yes.setText(QCoreApplication.translate("bulk_insert_window", u"Yes", None))
        self.bulk_column_prefilled_is_local_no.setText(QCoreApplication.translate("bulk_insert_window", u"No", None))
        self.bulk_save_profile.setText(QCoreApplication.translate("bulk_insert_window", u"Save Bulk profile", None))
        self.bulk_column_prefilled_is_retired_yes.setText(QCoreApplication.translate("bulk_insert_window", u"Yes", None))
        self.bulk_column_prefilled_is_retired_no.setText(QCoreApplication.translate("bulk_insert_window", u"No", None))
        self.label_isretired.setText(QCoreApplication.translate("bulk_insert_window", u"Is retired", None))
        self.label_notes.setText(QCoreApplication.translate("bulk_insert_window", u"Notes", None))
        self.bulk_column_prefilled_notes.setText("")
        self.bulk_insert_button.setText(QCoreApplication.translate("bulk_insert_window", u"Insert!!", None))
        self.label_serial_2.setText(QCoreApplication.translate("bulk_insert_window", u"Model", None))
    # retranslateUi
        """
        Not auto-generated
            
        """
        self.bulk_column_prefilled_cost.setMaximum(99999.99) 
        self.bulk_column_prefilled_deployment.setDate(self.parent_window.today) # does doing this instead of QDate.today() save computation power? probably not. idk
        self.bulk_file_text_file_browse.clicked.connect(self.open_file_dialog)
        # set the container's width to 0 to hide it by default:
        self.bulk_conditional_excel_headers_frame.setFixedWidth(0)
        self.bulk_insert_button.clicked.connect(self.bulk_insert_function)
        # add in the blank items
        self.bulk_column_prefilled_manu.addItem("")
        self.bulk_column_prefilled_asset.addItem("")        
        self.bulk_column_prefilled_location.addItem("")
        self.bulk_column_prefilled_category.addItem("")
        
        self.bulk_column_prefilled_manu.addItems(self.parent_window.manufacturers)
        self.bulk_column_prefilled_asset.addItems(self.parent_window.asset_types)        
        self.bulk_column_prefilled_location.addItems(self.parent_window.locations)
        self.bulk_column_prefilled_category.addItems(self.parent_window.categories)
        self.bulk_file_path_text.textChanged.connect(self.check_if_should_reveal_excel_option)
        self.bulk_save_profile.clicked.connect(self.save_bulk_profile)
        self.bulk_preset_combobox.currentTextChanged.connect(self.handle_combobox_change)
        self.bulk_preset_combobox.addItem("")
        for x in self.parent_window.config["bulk_presets"]:
            self.bulk_preset_combobox.addItem(x["profile_name"])

        
    def open_file_dialog(self):
        filedialog = QFileDialog
        path = filedialog.getOpenFileName(self)
        if path is not None and path != "":
            try:
                self.bulk_file_path_text.setText(path[0])
            except TypeError:
                pass

    def handle_combobox_change(self):
        """
            called when the preset combobox's value changes
            we'll clear all the field in the (bulk insert) ui
            if not empty, we fill the gui out with the saved preset information
            
        """
        combobox_value = self.bulk_preset_combobox.currentText()
        for combo in (self.bulk_column_prefilled_asset, self.bulk_column_prefilled_manu, self.bulk_column_prefilled_location, self.bulk_column_prefilled_category):
            combo.setCurrentText("")
        # clear the line edits too
        for line in (self.bulk_column_number_asset, self.bulk_column_number_manu, self.bulk_column_number_cost, self.bulk_column_number_serial, self.bulk_column_number_category,
                    self.bulk_column_number_location, self.bulk_column_number_name, self.bulk_column_number_assigned, self.bulk_column_number_deployment, self.bulk_column_number_local,
                    self.bulk_column_number_retired, self.bulk_column_number_notes, self.bulk_column_prefilled_serial, self.bulk_column_prefilled_model, self.bulk_column_prefilled_assigned,
                    self.bulk_column_prefilled_device, self.bulk_column_prefilled_notes, self.bulk_column_number_model):
            line.clear()                    
        self.bulk_column_prefilled_cost.setValue(0.0)
        self.bulk_column_prefilled_deployment.setDate(self.parent_window.today)
        for checkbox in (self.bulk_column_prefilled_is_local_yes, self.bulk_column_prefilled_is_local_no, self.bulk_column_prefilled_is_retired_no, self.bulk_column_prefilled_is_retired_yes):
            checkbox.setAutoExclusive(False) # for some reason this autoexclusive part is needed for thme to actually uncheck
            checkbox.setChecked(False)
            checkbox.setAutoExclusive(True)
        if combobox_value != "":
            json_data = self.parent_window.config["bulk_presets"]
            for profile in json_data:
                if combobox_value == profile["profile_name"]:
                    bulk_data = profile # will always be bound..
                    break # can stop looking once we've found it
            if "bulk_data" not in locals():
                # if the variable is unbound, we don't need to continue, since we would be trying to fetch a non-existant profile
                return
            # now we populate the fields with the data from the profile
            for name, data in bulk_data.items():
                if data[1] == "":
                    # when there is nothing to update.. update nothing
                    continue
                if not isinstance(data[1], str): # if the provided info isn't a string, conver to string
                    data = (data[0], str(data[1]))
                if name == "assettype":
                    if data[0] is True:
                        self.bulk_column_prefilled_asset.setCurrentText(data[1])
                    else:
                        self.bulk_column_number_asset.setText(data[1])
                elif name == "manu":
                    if data[0] is True:
                        self.bulk_column_prefilled_manu.setCurrentText(data[1])
                    else:
                        self.bulk_column_number_manu.setText(data[1])
                elif name == "serial":
                    if data[0] is True:
                        self.bulk_column_prefilled_serial.setText(data[1])
                    else:
                        self.bulk_column_number_serial.setText(data[1])
                elif name == "model":
                    if data[0] is True:
                        self.bulk_column_prefilled_model.setText(data[1])
                    else:
                        self.bulk_column_number_model.setText(data[1])
                elif name == "cost":
                    if data[0] is True:
                        self.bulk_column_prefilled_cost.setValue(float(data[1])) # mildly redundant that we cast this twice...
                    else:
                        self.bulk_column_number_cost.setText(data[1])
                elif name == "assigned":
                    if data[0] is True:
                        self.bulk_column_prefilled_assigned.setText(data[1])
                    else:
                        self.bulk_column_number_assigned.setText(data[1])
                elif name == "name":
                    if data[0] is True:
                        self.bulk_column_prefilled_device.setText(data[1])
                    else:
                        self.bulk_column_number_name.setText(data[1]) # TODO naming conv here and the else
                elif name == "location":
                    if data[0] is True:
                        self.bulk_column_prefilled_location.setCurrentText(data[1])
                    else:
                        self.bulk_column_number_location.setText(data[1])
                elif name == "category":
                    if data[0] is True:
                        self.bulk_column_prefilled_category.setCurrentText(data[1])
                    else:
                        self.bulk_column_number_category.setText(data[1])
                elif name == "deployment":
                    if data[0] is True:
                        self.bulk_column_prefilled_deployment.setDate(QDate.fromString(data[1]))
                    else:
                        self.bulk_column_number_deployment.setText(data[1])
                elif name == "local":
                    if data[0] is True: # true means that one of the buttons is clicked
                        if data[1] is True:
                            self.bulk_column_prefilled_is_local_no.setChecked(False)
                            self.bulk_column_prefilled_is_local_yes.setChecked(True) # in the case where the other is selected beforehand...
                        else:
                            self.bulk_column_prefilled_is_local_no.setChecked(True)
                            self.bulk_column_prefilled_is_local_yes.setChecked(False)
                    else:
                        self.bulk_column_number_local.setText(data[1])
                elif name == "retired":
                    if data[0] is True: # true means that one of the buttons is clicked
                        if data[1] is True:
                            self.bulk_column_prefilled_is_retired_no.setChecked(False)
                            self.bulk_column_prefilled_is_retired_yes.setChecked(True) # in the case where the other is selected beforehand...
                        else:
                            self.bulk_column_prefilled_is_retired_no.setChecked(True)
                            self.bulk_column_prefilled_is_retired_yes.setChecked(False) # in the case where the other is selected beforehand...
                    else:
                        self.bulk_column_number_retired.setText(data[1])
                elif name == "notes":
                    if data[0] is True:
                        self.bulk_column_prefilled_notes.setText(data[1])
                    else:
                        self.bulk_column_number_notes.setText(data[1])
                        
                        
                
        

    def check_if_should_reveal_excel_option(self):
        text = self.bulk_file_path_text.text()
        if not isinstance(text, str):
            return
        if text.endswith("xlsx"):
            self.bulk_conditional_excel_headers_frame.setFixedWidth(210)
        else:
            self.bulk_conditional_excel_headers_frame.setFixedWidth(0)
            
    def translate_word_to_column_num(self, value: str):
        """
        called when:
        the user inserts an ambiguous column position by specifying the title of the column (eg. 'location') rather than the number / excel column
        the user supplies an excel column value (eg. 'C', 'AB')

        returns:
            int: column number        
        
        """
        file = self.bulk_file_path_text.text()
        if value.isnumeric():
            return int(value)
        if len(value) <= 2: # very likely we're looking at a value like "A" or "AB" (excel notation)
            upper_ver = value.upper() # turn it into uppercase so ord() doesn't get confused
            col_num = 0
            for lt in upper_ver:
                # doing -65 turns ord('A') into int(0), which is what we want. (consider index starts at 0)
                col_num += (ord(lt) - 65)
            return col_num
        if file.endswith(".xlsx"):
            import openpyxl
            x = openpyxl.open(file)            
            wb = x.active
            letter = 'A'
            while True:
                if wb[f"{letter}1"].value == value:
                    return ord(letter.upper()) - 65
                # give us the right letter...
                if letter == "BA":
                    self.parent_window.display_message("Error!", f"Failure finding excel letter column from phrase: {value} in file: \n{file}")
                    return
                if letter == "Z":
                    letter = "AB"
                    continue
                elif len(letter) == 2:
                    letter = chr(ord(letter[1]) + 1) + "A"
                else:
                    letter = chr(ord(letter) + 1)
        elif file.endswith(".csv"):
            import csv
            with open(file, "r", encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                for row in reader:
                    print("ROW!", row)
                    for position, name in enumerate(row):
                        if name == value:
                            return position
                    self.parent_window.display_message("Malformed value", f'{value} not found in the headers of: \n{file}')
                    return
                self.parent_window.display_message("Error!", f"Cannot find value {value} in headers of: \n{file}")
        else:
            self.parent_window.display_message("Error!", "File passed in is not .xlsx or .csv")

    def save_bulk_profile(self):
        """
        we take the existing data from what the user has filled out, and store it in the bulk profile store
        the bulk profiles live in the self.parent_window.config["bulk_presets"] <-- might do some naming changes
        """
        profile_name = self.bulk_preset_combobox.currentText()
        existing_names = [x["profile_name"] for x in self.parent_window.config["bulk_presets"]]
            
        _asset = True if self.bulk_column_number_asset.text() == "" else False
        _manu = True if self.bulk_column_number_manu.text() == "" else False
        _serial = True if self.bulk_column_number_serial.text() == "" else False
        _model = True if self.bulk_column_number_model.text() == "" else False
        _cost = True if self.bulk_column_number_cost.text() == "" else False
        _assigned = True if self.bulk_column_number_assigned.text() == "" else False
        _name = True if self.bulk_column_number_name.text() == "" else False
        _location = True if self.bulk_column_number_location.text() == "" else False
        _category = True if self.bulk_column_number_category.text() == "" else False
        _deployment = True if self.bulk_column_number_deployment.text() == "" else False
        _local = True if self.bulk_column_number_local.text() == "" else False
        _retired = True if self.bulk_column_number_retired.text() == "" else False
        _notes = True if self.bulk_column_number_notes.text() == "" else False
        print("status of _notes {should be true}", _notes)
        # so if the name the user tried is valid, we want to add it into the list here (as well as the config below...)
        # there is an argument for standardization here. will do one day with the partial rewrite. should be standardized with the other naming conventions in config
        new_profile = {
            "profile_name": profile_name,
            # we'll follow the same format as before, where we have a tuple (bool, value) bool = if we will use the premade option (on the left)
            # so if "Assettype" if like: "Assettype": (True, Laptop), we'll fill out the field on the left with 'Laptop'. If it was false, we'd fill out the
            # right part with "Laptop", which would mean we're looking in the given file for that column name
            "assettype": (_asset, self.bulk_column_prefilled_asset.currentText() if _asset else self.bulk_column_number_asset.text()),
            "manu": (_manu, self.bulk_column_prefilled_manu.currentText() if _manu else self.bulk_column_number_manu.text()),
            "serial": (_serial, self.bulk_column_prefilled_serial.text() if _serial else self.bulk_column_number_serial.text()),
            "model": (_model, self.bulk_column_prefilled_model.text() if _model else self.bulk_column_number_model.text()),
            "cost": (_cost, self.bulk_column_prefilled_cost.value() if _cost else self.bulk_column_number_cost.text()),
            "assigned": (_assigned, self.bulk_column_prefilled_assigned.text() if _assigned else self.bulk_column_number_assigned.text()),
            "name": (_name, self.bulk_column_prefilled_device.text() if _name else self.bulk_column_number_name.text()), # TODO rename. should be bulkk_prefilled_name
            "location": (_location, self.bulk_column_prefilled_location.currentText() if _location else self.bulk_column_number_location.text()),
            "category": (_category, self.bulk_column_prefilled_category.currentText() if _category else self.bulk_column_number_category.text()),
            "deployment": (_deployment, str(self.bulk_column_prefilled_deployment.date().toPyDate()) if _deployment else self.bulk_column_number_deployment.text()), # doing .date().to_String() turns it into 'mon jan 1 2025', not "2025-01-01"
            "local": (_local, self.bulk_column_prefilled_is_local_yes.isChecked() if _local else self.bulk_column_number_local.text()),
            "retired": (_retired, self.bulk_column_prefilled_is_retired_yes.isChecked() if _retired else self.bulk_column_number_retired.text()),
            "notes": (_notes, self.bulk_column_prefilled_notes.text() if _notes else self.bulk_column_number_notes.text()),
        }
        if profile_name in existing_names: # we're going to overwrite an existing name
            print("profile info", profile_name, type(profile_name))
            # self.parent_window.config["bulk_presets"].pop(profile_name)
            for i, data in enumerate(self.parent_window.config["bulk_presets"]):
                print("i and data", i, data)
                if data["profile_name"] == profile_name:
                    # remove the old profile and add he new one
                    print("removing old data config")
                    self.parent_window.config["bulk_presets"].pop(i)
                    print("adding", data)
                    self.parent_window.config["bulk_presets"].append(new_profile)
                    break
        else:
            # it would already exist either way...
            self.parent_window.config["bulk_presets"].append(new_profile)  
            existing_names.append(profile_name)
            
        # reset the combobox with the new items
        self.bulk_preset_combobox.clear()
        self.bulk_preset_combobox.addItem("")
        print("this!", self.parent_window.config["bulk_presets"])
        print(f"the names of the profiles: {existing_names}")
        self.bulk_preset_combobox.addItems(existing_names)
        self.bulk_preset_combobox.setCurrentText(profile_name)
        # just  alittle bit of user feedback smh
        self.parent_window.display_message("Success!", "Bulk profile saved successfully!")

    def bulk_insert_function(self):
        # build the obj from the existing data
        obj = BulkData().build(self)  # does a check for null filepath
        if not obj:
            # pretty much if it returned Err() lmao. just terminate
            return
        print("obj??!?!", obj)
        file_path = self.bulk_file_path_text.text()
        if file_path.endswith(".xlsx"): # redundant as hell smh
            # we'll read the entire file and iterate over each row
            inventory_obj_list = []
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active
            data = [list(row) for row in ws.iter_rows(values_only=True)]
            should_skip_first = self.bulk_conditional_excel_headers_checkbox.isChecked()
            self.parent_window.connection.autocommit = False # set to false so we don't end up half-committing the bulk items and making a mess
            for row in data:
                if should_skip_first:
                    # if we are reading the headers in excel...
                    should_skip_first = False
                    continue
                # this seems stupid. very fitting.
                inventory_obj = InventoryObject.__new__(InventoryObject).init_empty()
                # if a field in BulkData has the False option, we will pull from the file
                if obj.asset[0] is False:
                    inventory_obj.assettype = row[obj.asset[1]]
                else:
                    inventory_obj.assettype = obj.asset[1]
                if obj.manu[0] is False:
                    inventory_obj.manufacturer = row[obj.manu[1]]
                else:
                    inventory_obj.manufacturer = obj.manu[1]
                if obj.serial[0] is False:
                    inventory_obj.serial = row[obj.serial[1]]
                else:
                    inventory_obj.serial = obj.serial[1]
                if obj.model[0] is False:
                    inventory_obj.model = row[obj.model[1]]
                else:
                    inventory_obj.model = obj.model[1]
                if obj.cost[0] is False:
                    inventory_obj.cost = row[obj.cost[1]]
                else:
                    inventory_obj.cost = obj.cost[1]
                if obj.assigned[0] is False:
                    inventory_obj.assignedto = row[obj.assigned[1]]
                else:
                    inventory_obj.assignedto = obj.assigned[1]
                if obj.name[0] is False:
                    inventory_obj.name = row[obj.name[1]]
                else:
                    inventory_obj.name = obj.name[1]
                if obj.location[0] is False:
                    inventory_obj.assetlocation = row[obj.location[1]]
                else:
                    inventory_obj.assetlocation = obj.location[1]
                if obj.category[0] is False:
                    inventory_obj.assetcategory = row[obj.category[1]]
                else:
                    inventory_obj.assetcategory = obj.category[1]
                if obj.deployment[0] is False:
                    inventory_obj.deploymentdate = row[obj.deployment[1]]
                else:
                    inventory_obj.deploymentdate = obj.deployment[1]
                if obj.is_local[0] is False:
                    # remember: false means we take from the file (row=from file)
                    print("wtf is local wh is it this", obj.is_local)
                    inventory_obj.is_local = row[obj.is_local[1]]
                else:
                    print("wtf is local", obj.is_local)
                    inventory_obj.is_local = obj.is_local[1]
                if obj.is_retired[0] is False:
                    inventory_obj.status = row[obj.is_retired[1]]
                else:
                    inventory_obj.status = obj.is_retired[1] # row should only be in the else branch?
                if obj.notes[0] is False:
                    inventory_obj.notes = row[obj.notes[1]]
                else:
                    inventory_obj.notes = obj.notes[1]
                # set some defaults:
                inventory_obj.retirementdate = None
                inventory_obj.replacementdate = self.update_replacement_date_if_can(inventory_obj.deploymentdate, inventory_obj.assettype)
                inventory_obj.loandate = None
                inventory_obj.returndate = None
                inventory_obj_list.append(inventory_obj)
            print("len of rows:", len(inventory_obj_list))
            bulk_insert(self.parent_window.connection, inventory_obj_list)
        else: # we check in the `build` function to make sure this makes sense.
            self.parent_window.display_message("Error!", "Csv import not implemented yet")
            pass
                    
                
    def update_replacement_date_if_can(self, date, asset_type):
        with open("./volatile/assetcategory.json", "r") as f:
            raw_json = json.load(f)["Category"]
        try:
            # if what the user supplied actually is found in the json
            add_years = raw_json[asset_type]
            return date + relativedelta(add_years)
        except KeyError:
            return date
        
            
class BulkData:
    def __init__(self) -> None:
        # for each of these, there are two values: (boolean_is_static, value)
        # so when we use the function to insert, we can pull data correctly from the other sources
        self.asset = ()        
        self.manu = ()
        self.serial = ()
        self.model = ()
        self.cost = ()
        self.assigned = ()
        self.name = ()
        self.location = ()
        self.category = ()
        self.deployment = ()
        self.is_local = ()
        self.is_retired = ()
        self.notes = ()
        
    def build(self, parent_window): # creates self
        """
        function to parse the content on the bulk insert page


        Returns:
            BulkData
            each field in bulkdata has a (bool, value) structure. the bool is whether or not the value should come from the 'pre-made' option         
            
        """
        if parent_window.bulk_column_number_asset.text() == "":
            # this means we're going to use the pre-made option
            self.asset = (True, parent_window.bulk_column_prefilled_asset.currentText())
        else:
            self.asset = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_asset.text()))
        if parent_window.bulk_column_number_manu.text() == "":
            self.manu = (True, parent_window.bulk_column_prefilled_manu.currentText())
        else:
            self.manu = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_manu.text()))
        if parent_window.bulk_column_number_serial.text() == "":
            self.serial = (True, parent_window.bulk_column_prefilled_serial.text())
        else:
            self.serial = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_serial.text()))
        if parent_window.bulk_column_number_model.text() == "":
            self.model = (True, parent_window.bulk_column_prefilled_model.text())
        else:
            self.model = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_model.text()))
        if parent_window.bulk_column_number_cost.text() == "":
            self.cost = (True, parent_window.bulk_column_prefilled_cost.text())
        else:
            self.cost = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_cost.text()))
        if parent_window.bulk_column_number_assigned.text() == "":
            self.assigned = (True, parent_window.bulk_column_prefilled_assigned.text())
        else:
            self.assigned = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_assigned.text()))
        if parent_window.bulk_column_number_name.text() == "":
            self.name = (True, parent_window.bulk_column_prefilled_device.text())
        else:
            self.name = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_name.text()))
        if parent_window.bulk_column_number_category.text() == "":
            self.category = (True, parent_window.bulk_column_prefilled_category.currentText())
        else:
            self.category = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_category.text()))
        if parent_window.bulk_column_number_location.text() == "":
            self.location = (True, parent_window.bulk_column_prefilled_location.currentText())
        else:
            self.location = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_location.text()))
        if parent_window.bulk_column_number_deployment.text() == "":
            self.deployment = (True, parent_window.bulk_column_prefilled_deployment.date().toPyDate())
        else:
            self.deployment = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_deployment.text()))
        if parent_window.bulk_column_number_local.text() == "":
            yes_check = parent_window.bulk_column_prefilled_is_local_yes.isChecked()
            no_check = parent_window.bulk_column_prefilled_is_local_no.isChecked()
            if yes_check:
                self.is_local = (True, True)
            elif no_check:
                self.is_local = (True, False)
            else:
                parent_window.parent_window.display_message("Error!", "'is local' does not have a value supplied")
                return
        else:
            self.is_local = (False, parent_window.bulk_column_number_deployment.text())
        if parent_window.bulk_column_number_retired.text() == "":
            yes_check = parent_window.bulk_column_prefilled_is_retired_yes.isChecked()
            no_check = parent_window.bulk_column_prefilled_is_retired_no.isChecked()
            if yes_check:
                self.is_retired = (True, True)
            elif no_check:
                self.is_retired = (True, False)
            else:
                parent_window.parent_window.display_message("Error!", "'is retired' does not have a value supplied")
                return
        else:
            self.is_retired = (False, parent_window.bulk_column_number_retired.text())
        if parent_window.bulk_column_number_notes.text() == "":
            self.notes = (True, parent_window.bulk_column_prefilled_notes.text())
        else:
            self.notes = (False, parent_window.translate_word_to_column_num(parent_window.bulk_column_number_notes.text()))
        return self


    def __str__(self) -> str:
        x = ""
        for item in self.__dict__.items():
            x += f"{item}\n"
        return x
