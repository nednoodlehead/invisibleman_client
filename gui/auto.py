# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_managerkUrqFY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (
    QCoreApplication,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QUrl,
    Qt,
)
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 725)
        self.actionInsert = QAction(MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCreate_Backup = QAction(MainWindow)
        self.actionCreate_Backup.setObjectName("actionCreate_Backup")
        self.actionClose_ALT_F4 = QAction(MainWindow)
        self.actionClose_ALT_F4.setObjectName("actionClose_ALT_F4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ham_menu_frame = QFrame(self.centralwidget)
        self.ham_menu_frame.setObjectName("ham_menu_frame")
        self.ham_menu_frame.setGeometry(QRect(0, 20, 81, 250))
        self.ham_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.ham_menu_frame.setFrameShadow(QFrame.Raised)
        self.ham_menu_button = QPushButton(self.ham_menu_frame)
        self.ham_menu_button.setObjectName("ham_menu_button")
        self.ham_menu_button.setGeometry(QRect(0, 0, 81, 50))
        self.ham_menu_button.setFlat(False)
        self.ham_button_insert = QPushButton(self.ham_menu_frame)
        self.ham_button_insert.setObjectName("ham_button_insert")
        self.ham_button_insert.setGeometry(QRect(0, 100, 81, 50))
        self.ham_button_insert.setFlat(False)
        self.ham_button_analytics = QPushButton(self.ham_menu_frame)
        self.ham_button_analytics.setObjectName("ham_button_analytics")
        self.ham_button_analytics.setGeometry(QRect(0, 150, 81, 50))
        self.ham_button_analytics.setFlat(False)
        self.ham_button_reports = QPushButton(self.ham_menu_frame)
        self.ham_button_reports.setObjectName("ham_button_reports")
        self.ham_button_reports.setGeometry(QRect(0, 200, 81, 50))
        self.ham_button_reports.setFlat(False)
        self.ham_button_view = QPushButton(self.ham_menu_frame)
        self.ham_button_view.setObjectName("ham_button_view")
        self.ham_button_view.setGeometry(QRect(0, 50, 81, 50))
        self.ham_button_view.setFlat(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 0, 1171, 661))
        self.stacked_view_db_page = QWidget()
        self.stacked_view_db_page.setObjectName("stacked_view_db_page")
        self.main_table = QTableWidget(self.stacked_view_db_page)
        self.main_table.setObjectName("main_table")
        self.main_table.setGeometry(QRect(10, 60, 1151, 550))
        self.refresh_table_button = QPushButton(self.stacked_view_db_page)
        self.refresh_table_button.setObjectName("refresh_table_button")
        self.refresh_table_button.setGeometry(QRect(10, 30, 75, 23))
        self.view_toggle_frame = QFrame(self.stacked_view_db_page)
        self.view_toggle_frame.setObjectName("view_toggle_frame")
        self.view_toggle_frame.setGeometry(QRect(10, 610, 80, 41))
        self.view_toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.view_toggle_frame.setFrameShadow(QFrame.Raised)
        self.view_columns_button = QPushButton(self.view_toggle_frame)
        self.view_columns_button.setObjectName("view_columns_button")
        self.view_columns_button.setGeometry(QRect(0, 10, 75, 23))
        self.checkbox_name = QCheckBox(self.view_toggle_frame)
        self.checkbox_name.setObjectName("checkbox_name")
        self.checkbox_name.setGeometry(QRect(100, 0, 71, 21))
        self.checkbox_serial = QCheckBox(self.view_toggle_frame)
        self.checkbox_serial.setObjectName("checkbox_serial")
        self.checkbox_serial.setGeometry(QRect(100, 20, 71, 21))
        self.checkbox_manufacturer = QCheckBox(self.view_toggle_frame)
        self.checkbox_manufacturer.setObjectName("checkbox_manufacturer")
        self.checkbox_manufacturer.setGeometry(QRect(170, 0, 91, 21))
        self.checkbox_price = QCheckBox(self.view_toggle_frame)
        self.checkbox_price.setObjectName("checkbox_price")
        self.checkbox_price.setGeometry(QRect(170, 20, 71, 21))
        self.checkbox_assetcategory = QCheckBox(self.view_toggle_frame)
        self.checkbox_assetcategory.setObjectName("checkbox_assetcategory")
        self.checkbox_assetcategory.setGeometry(QRect(350, 0, 101, 21))
        self.checkbox_assettype = QCheckBox(self.view_toggle_frame)
        self.checkbox_assettype.setObjectName("checkbox_assettype")
        self.checkbox_assettype.setGeometry(QRect(260, 20, 91, 21))
        self.checkbox_assignedto = QCheckBox(self.view_toggle_frame)
        self.checkbox_assignedto.setObjectName("checkbox_assignedto")
        self.checkbox_assignedto.setGeometry(QRect(450, 0, 101, 21))
        self.checkbox_assetlocation = QCheckBox(self.view_toggle_frame)
        self.checkbox_assetlocation.setObjectName("checkbox_assetlocation")
        self.checkbox_assetlocation.setGeometry(QRect(350, 20, 91, 21))
        self.checkbox_purchasedate = QCheckBox(self.view_toggle_frame)
        self.checkbox_purchasedate.setObjectName("checkbox_purchasedate")
        self.checkbox_purchasedate.setGeometry(QRect(550, 0, 91, 21))
        self.checkbox_installdate = QCheckBox(self.view_toggle_frame)
        self.checkbox_installdate.setObjectName("checkbox_installdate")
        self.checkbox_installdate.setGeometry(QRect(450, 20, 91, 21))
        self.checkbox_replacementdate = QCheckBox(self.view_toggle_frame)
        self.checkbox_replacementdate.setObjectName("checkbox_replacementdate")
        self.checkbox_replacementdate.setGeometry(QRect(550, 20, 111, 21))
        self.checkbox_notes = QCheckBox(self.view_toggle_frame)
        self.checkbox_notes.setObjectName("checkbox_notes")
        self.checkbox_notes.setGeometry(QRect(660, 0, 71, 21))
        self.checkbox_model = QCheckBox(self.view_toggle_frame)
        self.checkbox_model.setObjectName("checkbox_model")
        self.checkbox_model.setGeometry(QRect(260, 0, 71, 21))
        self.filter_column_button = QPushButton(self.stacked_view_db_page)
        self.filter_column_button.setObjectName("filter_column_button")
        self.filter_column_button.setGeometry(QRect(100, 30, 75, 23))
        self.filter_options_combobox = QComboBox(self.stacked_view_db_page)
        self.filter_options_combobox.setObjectName("filter_options_combobox")
        self.filter_options_combobox.setGeometry(QRect(180, 30, 101, 22))
        self.filter_user_text = QLineEdit(self.stacked_view_db_page)
        self.filter_user_text.setObjectName("filter_user_text")
        self.filter_user_text.setGeometry(QRect(290, 30, 151, 20))
        self.filter_clear_button = QPushButton(self.stacked_view_db_page)
        self.filter_clear_button.setObjectName("filter_clear_button")
        self.filter_clear_button.setGeometry(QRect(440, 30, 21, 20))
        self.stackedWidget.addWidget(self.stacked_view_db_page)
        self.stacked_add_to_db_page = QWidget()
        self.stacked_add_to_db_page.setObjectName("stacked_add_to_db_page")
        self.insert_bold_equals_required_info = QLabel(self.stacked_add_to_db_page)
        self.insert_bold_equals_required_info.setObjectName(
            "insert_bold_equals_required_info"
        )
        self.insert_bold_equals_required_info.setGeometry(QRect(30, 40, 161, 21))
        self.insert_name_text = QLineEdit(self.stacked_add_to_db_page)
        self.insert_name_text.setObjectName("insert_name_text")
        self.insert_name_text.setGeometry(QRect(140, 110, 145, 25))
        self.insert_name_label = QLabel(self.stacked_add_to_db_page)
        self.insert_name_label.setObjectName("insert_name_label")
        self.insert_name_label.setGeometry(QRect(20, 110, 110, 13))
        font = QFont()
        font.setPointSize(10)
        self.insert_name_label.setFont(font)
        self.insert_name_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_serial_label = QLabel(self.stacked_add_to_db_page)
        self.insert_serial_label.setObjectName("insert_serial_label")
        self.insert_serial_label.setGeometry(QRect(20, 153, 110, 13))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.insert_serial_label.setFont(font1)
        self.insert_serial_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_serial_text = QLineEdit(self.stacked_add_to_db_page)
        self.insert_serial_text.setObjectName("insert_serial_text")
        self.insert_serial_text.setGeometry(QRect(140, 150, 145, 25))
        self.insert_manufacture_label = QLabel(self.stacked_add_to_db_page)
        self.insert_manufacture_label.setObjectName("insert_manufacture_label")
        self.insert_manufacture_label.setGeometry(QRect(20, 190, 110, 20))
        self.insert_manufacture_label.setFont(font1)
        self.insert_manufacture_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_manufacturer_text = QLineEdit(self.stacked_add_to_db_page)
        self.insert_manufacturer_text.setObjectName("insert_manufacturer_text")
        self.insert_manufacturer_text.setGeometry(QRect(140, 190, 145, 25))
        self.insert_price_label = QLabel(self.stacked_add_to_db_page)
        self.insert_price_label.setObjectName("insert_price_label")
        self.insert_price_label.setGeometry(QRect(20, 270, 110, 20))
        self.insert_price_label.setFont(font)
        self.insert_price_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_asset_category_label = QLabel(self.stacked_add_to_db_page)
        self.insert_asset_category_label.setObjectName("insert_asset_category_label")
        self.insert_asset_category_label.setGeometry(QRect(20, 300, 110, 20))
        self.insert_asset_category_label.setFont(font1)
        self.insert_asset_category_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_asset_category_combobox = QComboBox(self.stacked_add_to_db_page)
        self.insert_asset_category_combobox.setObjectName(
            "insert_asset_category_combobox"
        )
        self.insert_asset_category_combobox.setGeometry(QRect(140, 300, 145, 25))
        self.insert_asset_type_label = QLabel(self.stacked_add_to_db_page)
        self.insert_asset_type_label.setObjectName("insert_asset_type_label")
        self.insert_asset_type_label.setGeometry(QRect(20, 340, 110, 20))
        self.insert_asset_type_label.setFont(font1)
        self.insert_asset_type_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_asset_location_label = QLabel(self.stacked_add_to_db_page)
        self.insert_asset_location_label.setObjectName("insert_asset_location_label")
        self.insert_asset_location_label.setGeometry(QRect(20, 380, 110, 20))
        self.insert_asset_location_label.setFont(font1)
        self.insert_asset_location_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_asset_location_combobox = QComboBox(self.stacked_add_to_db_page)
        self.insert_asset_location_combobox.setObjectName(
            "insert_asset_location_combobox"
        )
        self.insert_asset_location_combobox.setGeometry(QRect(140, 380, 145, 25))
        self.insert_assigned_to_label = QLabel(self.stacked_add_to_db_page)
        self.insert_assigned_to_label.setObjectName("insert_assigned_to_label")
        self.insert_assigned_to_label.setGeometry(QRect(20, 420, 110, 21))
        self.insert_assigned_to_label.setFont(font)
        self.insert_assigned_to_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_assigned_to_text = QLineEdit(self.stacked_add_to_db_page)
        self.insert_assigned_to_text.setObjectName("insert_assigned_to_text")
        self.insert_assigned_to_text.setGeometry(QRect(140, 420, 145, 25))
        self.insert_asset_type_combobox = QComboBox(self.stacked_add_to_db_page)
        self.insert_asset_type_combobox.setObjectName("insert_asset_type_combobox")
        self.insert_asset_type_combobox.setGeometry(QRect(140, 340, 145, 25))
        self.insert_purchase_date_label = QLabel(self.stacked_add_to_db_page)
        self.insert_purchase_date_label.setObjectName("insert_purchase_date_label")
        self.insert_purchase_date_label.setGeometry(QRect(20, 460, 110, 21))
        self.insert_purchase_date_label.setFont(font)
        self.insert_purchase_date_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_purchase_date_fmt = QDateEdit(self.stacked_add_to_db_page)
        self.insert_purchase_date_fmt.setObjectName("insert_purchase_date_fmt")
        self.insert_purchase_date_fmt.setGeometry(QRect(140, 460, 110, 22))
        self.insert_install_date_label = QLabel(self.stacked_add_to_db_page)
        self.insert_install_date_label.setObjectName("insert_install_date_label")
        self.insert_install_date_label.setGeometry(QRect(20, 500, 110, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.insert_install_date_label.setFont(font2)
        self.insert_install_date_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_install_date_fmt = QDateEdit(self.stacked_add_to_db_page)
        self.insert_install_date_fmt.setObjectName("insert_install_date_fmt")
        self.insert_install_date_fmt.setGeometry(QRect(140, 500, 110, 22))
        self.insert_replacement_date_fmt = QDateEdit(self.stacked_add_to_db_page)
        self.insert_replacement_date_fmt.setObjectName("insert_replacement_date_fmt")
        self.insert_replacement_date_fmt.setGeometry(QRect(140, 540, 110, 22))
        self.insert_replacement_date_label = QLabel(self.stacked_add_to_db_page)
        self.insert_replacement_date_label.setObjectName(
            "insert_replacement_date_label"
        )
        self.insert_replacement_date_label.setGeometry(QRect(20, 540, 110, 21))
        self.insert_replacement_date_label.setFont(font)
        self.insert_replacement_date_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_notes_label = QLabel(self.stacked_add_to_db_page)
        self.insert_notes_label.setObjectName("insert_notes_label")
        self.insert_notes_label.setGeometry(QRect(350, 110, 110, 13))
        self.insert_notes_label.setFont(font)
        self.insert_notes_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_notes_text = QTextEdit(self.stacked_add_to_db_page)
        self.insert_notes_text.setObjectName("insert_notes_text")
        self.insert_notes_text.setGeometry(QRect(480, 110, 291, 191))
        self.insert_status_label = QLabel(self.stacked_add_to_db_page)
        self.insert_status_label.setObjectName("insert_status_label")
        self.insert_status_label.setGeometry(QRect(350, 330, 110, 21))
        self.insert_status_label.setFont(font)
        self.insert_status_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_status_bool = QComboBox(self.stacked_add_to_db_page)
        self.insert_status_bool.setObjectName("insert_status_bool")
        self.insert_status_bool.setGeometry(QRect(480, 330, 91, 22))
        self.insert_price_spinbox = QDoubleSpinBox(self.stacked_add_to_db_page)
        self.insert_price_spinbox.setObjectName("insert_price_spinbox")
        self.insert_price_spinbox.setGeometry(QRect(140, 270, 111, 22))
        self.insert_asset_category_add_option = QPushButton(self.stacked_add_to_db_page)
        self.insert_asset_category_add_option.setObjectName(
            "insert_asset_category_add_option"
        )
        self.insert_asset_category_add_option.setGeometry(QRect(290, 300, 25, 25))
        self.insert_asset_type_add_option = QPushButton(self.stacked_add_to_db_page)
        self.insert_asset_type_add_option.setObjectName("insert_asset_type_add_option")
        self.insert_asset_type_add_option.setGeometry(QRect(290, 340, 25, 25))
        self.insert_asset_location_add_option = QPushButton(self.stacked_add_to_db_page)
        self.insert_asset_location_add_option.setObjectName(
            "insert_asset_location_add_option"
        )
        self.insert_asset_location_add_option.setGeometry(QRect(290, 380, 25, 25))
        self.insert_asset_location_add_option.setLayoutDirection(Qt.LeftToRight)
        self.insert_insert_button = QPushButton(self.stacked_add_to_db_page)
        self.insert_insert_button.setObjectName("insert_insert_button")
        self.insert_insert_button.setGeometry(QRect(420, 410, 61, 23))
        self.insert_uuid_label = QLabel(self.stacked_add_to_db_page)
        self.insert_uuid_label.setObjectName("insert_uuid_label")
        self.insert_uuid_label.setGeometry(QRect(350, 370, 110, 21))
        self.insert_uuid_label.setFont(font)
        self.insert_uuid_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_uuid_text = QLineEdit(self.stacked_add_to_db_page)
        self.insert_uuid_text.setObjectName("insert_uuid_text")
        self.insert_uuid_text.setGeometry(QRect(480, 370, 145, 25))
        self.insert_uuid_text.setReadOnly(True)
        self.insert_clear_selections_button = QPushButton(self.stacked_add_to_db_page)
        self.insert_clear_selections_button.setObjectName(
            "insert_clear_selections_button"
        )
        self.insert_clear_selections_button.setGeometry(QRect(1070, 590, 75, 23))
        self.insert_model_label = QLabel(self.stacked_add_to_db_page)
        self.insert_model_label.setObjectName("insert_model_label")
        self.insert_model_label.setGeometry(QRect(20, 230, 110, 21))
        self.insert_model_label.setFont(font)
        self.insert_model_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.insert_model_text = QLineEdit(self.stacked_add_to_db_page)
        self.insert_model_text.setObjectName("insert_model_text")
        self.insert_model_text.setGeometry(QRect(140, 230, 145, 25))
        self.stackedWidget.addWidget(self.stacked_add_to_db_page)
        self.insert_purchase_date_fmt.raise_()
        self.insert_bold_equals_required_info.raise_()
        self.insert_name_label.raise_()
        self.insert_serial_label.raise_()
        self.insert_manufacture_label.raise_()
        self.insert_price_label.raise_()
        self.insert_asset_category_label.raise_()
        self.insert_asset_type_label.raise_()
        self.insert_asset_location_label.raise_()
        self.insert_assigned_to_label.raise_()
        self.insert_purchase_date_label.raise_()
        self.insert_install_date_label.raise_()
        self.insert_replacement_date_label.raise_()
        self.insert_notes_label.raise_()
        self.insert_status_label.raise_()
        self.insert_status_bool.raise_()
        self.insert_asset_category_add_option.raise_()
        self.insert_asset_type_add_option.raise_()
        self.insert_asset_location_add_option.raise_()
        self.insert_insert_button.raise_()
        self.insert_uuid_label.raise_()
        self.insert_uuid_text.raise_()
        self.insert_clear_selections_button.raise_()
        self.insert_model_label.raise_()
        self.insert_notes_text.raise_()
        self.insert_replacement_date_fmt.raise_()
        self.insert_install_date_fmt.raise_()
        self.insert_assigned_to_text.raise_()
        self.insert_asset_location_combobox.raise_()
        self.insert_asset_type_combobox.raise_()
        self.insert_asset_category_combobox.raise_()
        self.insert_price_spinbox.raise_()
        self.insert_model_text.raise_()
        self.insert_manufacturer_text.raise_()
        self.insert_serial_text.raise_()
        self.insert_name_text.raise_()
        self.stacked_analytic_page = QWidget()
        self.stacked_analytic_page.setObjectName("stacked_analytic_page")
        self.analytics_graph_frame_top = QFrame(self.stacked_analytic_page)
        self.analytics_graph_frame_top.setObjectName("analytics_graph_frame_top")
        self.analytics_graph_frame_top.setGeometry(QRect(20, 30, 1141, 310))
        self.analytics_graph_frame_top.setFrameShape(QFrame.StyledPanel)
        self.analytics_graph_frame_top.setFrameShadow(QFrame.Raised)
        self.analytics_field_combobox_top = QComboBox(self.analytics_graph_frame_top)
        self.analytics_field_combobox_top.setObjectName("analytics_field_combobox_top")
        self.analytics_field_combobox_top.setGeometry(QRect(20, 20, 161, 22))
        self.analytics_graph_top = QFrame(self.analytics_graph_frame_top)
        self.analytics_graph_top.setObjectName("analytics_graph_top")
        self.analytics_graph_top.setGeometry(QRect(190, 5, 921, 291))
        self.analytics_graph_top.setFrameShape(QFrame.StyledPanel)
        self.analytics_graph_top.setFrameShadow(QFrame.Raised)
        self.analytics_field_combobox_top_2 = QComboBox(self.analytics_graph_frame_top)
        self.analytics_field_combobox_top_2.setObjectName(
            "analytics_field_combobox_top_2"
        )
        self.analytics_field_combobox_top_2.setGeometry(QRect(20, 70, 161, 22))
        self.analytics_export_top_button = QPushButton(self.analytics_graph_frame_top)
        self.analytics_export_top_button.setObjectName("analytics_export_top_button")
        self.analytics_export_top_button.setGeometry(QRect(20, 110, 75, 23))
        self.analytics_x_axis_label = QLabel(self.analytics_graph_frame_top)
        self.analytics_x_axis_label.setObjectName("analytics_x_axis_label")
        self.analytics_x_axis_label.setGeometry(QRect(20, 150, 71, 16))
        self.analytics_x_axis_label.setToolTipDuration(-1)
        self.analytics_x_axis_text = QLineEdit(self.analytics_graph_frame_top)
        self.analytics_x_axis_text.setObjectName("analytics_x_axis_text")
        self.analytics_x_axis_text.setGeometry(QRect(20, 170, 161, 20))
        self.analytics_x_axis_text.setToolTipDuration(-1)
        self.analytics_y_axis_text = QLineEdit(self.analytics_graph_frame_top)
        self.analytics_y_axis_text.setObjectName("analytics_y_axis_text")
        self.analytics_y_axis_text.setGeometry(QRect(20, 220, 161, 20))
        self.analytics_y_axis_label = QLabel(self.analytics_graph_frame_top)
        self.analytics_y_axis_label.setObjectName("analytics_y_axis_label")
        self.analytics_y_axis_label.setGeometry(QRect(20, 200, 71, 16))
        self.analytics_update_top_view_button = QPushButton(
            self.analytics_graph_frame_top
        )
        self.analytics_update_top_view_button.setObjectName(
            "analytics_update_top_view_button"
        )
        self.analytics_update_top_view_button.setGeometry(QRect(20, 260, 91, 21))
        self.analytics_graph_frame_top_2 = QFrame(self.stacked_analytic_page)
        self.analytics_graph_frame_top_2.setObjectName("analytics_graph_frame_top_2")
        self.analytics_graph_frame_top_2.setGeometry(QRect(620, 350, 541, 310))
        self.analytics_graph_frame_top_2.setFrameShape(QFrame.StyledPanel)
        self.analytics_graph_frame_top_2.setFrameShadow(QFrame.Raised)
        self.analytics_field_combobox_bottom = QComboBox(
            self.analytics_graph_frame_top_2
        )
        self.analytics_field_combobox_bottom.setObjectName(
            "analytics_field_combobox_bottom"
        )
        self.analytics_field_combobox_bottom.setGeometry(QRect(20, 20, 161, 22))
        self.analytics_field_combobox_bottom_2 = QComboBox(
            self.analytics_graph_frame_top_2
        )
        self.analytics_field_combobox_bottom_2.setObjectName(
            "analytics_field_combobox_bottom_2"
        )
        self.analytics_field_combobox_bottom_2.setGeometry(QRect(20, 70, 161, 22))
        self.analytics_graph_bottom = QFrame(self.analytics_graph_frame_top_2)
        self.analytics_graph_bottom.setObjectName("analytics_graph_bottom")
        self.analytics_graph_bottom.setGeometry(QRect(10, 5, 521, 301))
        self.analytics_graph_bottom.setFrameShape(QFrame.StyledPanel)
        self.analytics_graph_bottom.setFrameShadow(QFrame.Raised)
        self.analytics_export_bottom_button = QPushButton(
            self.analytics_graph_frame_top_2
        )
        self.analytics_export_bottom_button.setObjectName(
            "analytics_export_bottom_button"
        )
        self.analytics_export_bottom_button.setGeometry(QRect(20, 110, 75, 23))
        self.analytics_graph_bottom.raise_()
        self.analytics_field_combobox_bottom_2.raise_()
        self.analytics_field_combobox_bottom.raise_()
        self.analytics_export_bottom_button.raise_()
        self.calendarWidget = QCalendarWidget(self.stacked_analytic_page)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 340, 590, 311))
        self.stackedWidget.addWidget(self.stacked_analytic_page)
        self.stacked_reports_page = QWidget()
        self.stacked_reports_page.setObjectName("stacked_reports_page")
        self.reports_total_asset_value_label = QLabel(self.stacked_reports_page)
        self.reports_total_asset_value_label.setObjectName(
            "reports_total_asset_value_label"
        )
        self.reports_total_asset_value_label.setGeometry(QRect(880, 20, 251, 41))
        font3 = QFont()
        font3.setFamily("Arial")
        font3.setPointSize(24)
        self.reports_total_asset_value_label.setFont(font3)
        self.reports_dollarsign_label = QLabel(self.stacked_reports_page)
        self.reports_dollarsign_label.setObjectName("reports_dollarsign_label")
        self.reports_dollarsign_label.setGeometry(QRect(880, 60, 16, 41))
        font4 = QFont()
        font4.setPointSize(24)
        self.reports_dollarsign_label.setFont(font4)
        self.reports_asset_integer_label = QLabel(self.stacked_reports_page)
        self.reports_asset_integer_label.setObjectName("reports_asset_integer_label")
        self.reports_asset_integer_label.setGeometry(QRect(900, 60, 221, 41))
        self.reports_asset_integer_label.setFont(font3)
        self.reports_asset_integer_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.reports_export_frame = QFrame(self.stacked_reports_page)
        self.reports_export_frame.setObjectName("reports_export_frame")
        self.reports_export_frame.setGeometry(QRect(40, 30, 361, 621))
        self.reports_export_frame.setStyleSheet("")
        self.reports_export_frame.setFrameShape(QFrame.StyledPanel)
        self.reports_export_frame.setFrameShadow(QFrame.Raised)
        self.reports_export_main_label = QLabel(self.reports_export_frame)
        self.reports_export_main_label.setObjectName("reports_export_main_label")
        self.reports_export_main_label.setGeometry(QRect(10, 20, 341, 31))
        self.reports_export_main_label.setFont(font3)
        self.reports_export_main_label.setAlignment(Qt.AlignCenter)
        self.reports_export_export_file_label = QLabel(self.reports_export_frame)
        self.reports_export_export_file_label.setObjectName(
            "reports_export_export_file_label"
        )
        self.reports_export_export_file_label.setGeometry(QRect(20, 70, 61, 16))
        self.reports_export_file_combobox = QComboBox(self.reports_export_frame)
        self.reports_export_file_combobox.setObjectName("reports_export_file_combobox")
        self.reports_export_file_combobox.setGeometry(QRect(90, 70, 69, 22))
        self.line = QFrame(self.reports_export_frame)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(10, 110, 341, 2))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.reports_export_frame)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(10, 170, 341, 2))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.reports_export_export_all_info_label = QLabel(self.reports_export_frame)
        self.reports_export_export_all_info_label.setObjectName(
            "reports_export_export_all_info_label"
        )
        self.reports_export_export_all_info_label.setGeometry(QRect(150, 120, 201, 41))
        self.reports_export_export_all_info_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.reports_export_export_all_info_label.setWordWrap(True)
        self.reports_export_export_all_radio = QRadioButton(self.reports_export_frame)
        self.reports_export_export_all_radio.setObjectName(
            "reports_export_export_all_radio"
        )
        self.reports_export_export_all_radio.setGeometry(QRect(10, 130, 82, 17))
        self.reports_export_export_EOL_radio = QRadioButton(self.reports_export_frame)
        self.reports_export_export_EOL_radio.setObjectName(
            "reports_export_export_EOL_radio"
        )
        self.reports_export_export_EOL_radio.setGeometry(QRect(10, 210, 131, 17))
        self.reports_export_EOL_text = QLineEdit(self.reports_export_frame)
        self.reports_export_EOL_text.setObjectName("reports_export_EOL_text")
        self.reports_export_EOL_text.setGeometry(QRect(160, 210, 101, 20))
        self.line_3 = QFrame(self.reports_export_frame)
        self.line_3.setObjectName("line_3")
        self.line_3.setGeometry(QRect(10, 270, 341, 2))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.reports_export_export_location_radio = QRadioButton(
            self.reports_export_frame
        )
        self.reports_export_export_location_radio.setObjectName(
            "reports_export_export_location_radio"
        )
        self.reports_export_export_location_radio.setGeometry(QRect(10, 300, 141, 17))
        self.reports_export_location_combobox = QComboBox(self.reports_export_frame)
        self.reports_export_location_combobox.setObjectName(
            "reports_export_location_combobox"
        )
        self.reports_export_location_combobox.setGeometry(QRect(160, 300, 101, 22))
        self.line_4 = QFrame(self.reports_export_frame)
        self.line_4.setObjectName("line_4")
        self.line_4.setGeometry(QRect(10, 360, 341, 2))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.reports_export_export_retired_radio = QRadioButton(
            self.reports_export_frame
        )
        self.reports_export_export_retired_radio.setObjectName(
            "reports_export_export_retired_radio"
        )
        self.reports_export_export_retired_radio.setGeometry(QRect(10, 390, 101, 17))
        self.reports_export_retired_assets_combobox = QComboBox(
            self.reports_export_frame
        )
        self.reports_export_retired_assets_combobox.setObjectName(
            "reports_export_retired_assets_combobox"
        )
        self.reports_export_retired_assets_combobox.setGeometry(
            QRect(160, 390, 101, 22)
        )
        self.line_5 = QFrame(self.reports_export_frame)
        self.line_5.setObjectName("line_5")
        self.line_5.setGeometry(QRect(10, 450, 341, 2))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.reports_export_main_export_button = QPushButton(self.reports_export_frame)
        self.reports_export_main_export_button.setObjectName(
            "reports_export_main_export_button"
        )
        self.reports_export_main_export_button.setGeometry(QRect(70, 490, 201, 31))
        self.reports_export_status_label = QLabel(self.reports_export_frame)
        self.reports_export_status_label.setObjectName("reports_export_status_label")
        self.reports_export_status_label.setGeometry(QRect(10, 550, 51, 16))
        self.reports_export_status_content = QLabel(self.reports_export_frame)
        self.reports_export_status_content.setObjectName(
            "reports_export_status_content"
        )
        self.reports_export_status_content.setGeometry(QRect(10, 570, 241, 41))
        self.export_file_path_choice = QLineEdit(self.reports_export_frame)
        self.export_file_path_choice.setObjectName("export_file_path_choice")
        self.export_file_path_choice.setGeometry(QRect(70, 460, 181, 20))
        self.export_file_dialog = QPushButton(self.reports_export_frame)
        self.export_file_dialog.setObjectName("export_file_dialog")
        self.export_file_dialog.setGeometry(QRect(250, 460, 31, 20))
        self.stackedWidget.addWidget(self.stacked_reports_page)
        self.stacked_settings_page = QWidget()
        self.stacked_settings_page.setObjectName("stacked_settings_page")
        self.settings_backup_dir_label = QLabel(self.stacked_settings_page)
        self.settings_backup_dir_label.setObjectName("settings_backup_dir_label")
        self.settings_backup_dir_label.setGeometry(QRect(10, 70, 181, 21))
        self.settings_backup_dir_label.setFont(font)
        self.settings_backup_dir_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.settings_backup_dir_text = QLineEdit(self.stacked_settings_page)
        self.settings_backup_dir_text.setObjectName("settings_backup_dir_text")
        self.settings_backup_dir_text.setGeometry(QRect(200, 70, 311, 20))
        self.settings_darkmode_label = QLabel(self.stacked_settings_page)
        self.settings_darkmode_label.setObjectName("settings_darkmode_label")
        self.settings_darkmode_label.setGeometry(QRect(10, 100, 181, 21))
        self.settings_darkmode_label.setFont(font)
        self.settings_darkmode_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.settings_darkmode_checkbox = QCheckBox(self.stacked_settings_page)
        self.settings_darkmode_checkbox.setObjectName("settings_darkmode_checkbox")
        self.settings_darkmode_checkbox.setGeometry(QRect(200, 103, 16, 17))
        self.settings_update_button = QPushButton(self.stacked_settings_page)
        self.settings_update_button.setObjectName("settings_update_button")
        self.settings_update_button.setGeometry(QRect(1060, 610, 75, 23))
        self.settings_report_auto_open_label = QLabel(self.stacked_settings_page)
        self.settings_report_auto_open_label.setObjectName(
            "settings_report_auto_open_label"
        )
        self.settings_report_auto_open_label.setGeometry(QRect(10, 127, 181, 21))
        self.settings_report_auto_open_label.setFont(font)
        self.settings_report_auto_open_label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.settings_report_auto_open_checkbox = QCheckBox(self.stacked_settings_page)
        self.settings_report_auto_open_checkbox.setObjectName(
            "settings_report_auto_open_checkbox"
        )
        self.settings_report_auto_open_checkbox.setGeometry(QRect(200, 130, 16, 17))
        self.stackedWidget.addWidget(self.stacked_settings_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1302, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.insert_name_text, self.insert_serial_text)
        QWidget.setTabOrder(self.insert_serial_text, self.insert_manufacturer_text)
        QWidget.setTabOrder(self.insert_manufacturer_text, self.insert_model_text)
        QWidget.setTabOrder(self.insert_model_text, self.insert_price_spinbox)
        QWidget.setTabOrder(
            self.insert_price_spinbox, self.insert_asset_category_combobox
        )
        QWidget.setTabOrder(
            self.insert_asset_category_combobox, self.insert_asset_type_combobox
        )
        QWidget.setTabOrder(
            self.insert_asset_type_combobox, self.insert_asset_location_combobox
        )
        QWidget.setTabOrder(
            self.insert_asset_location_combobox, self.insert_assigned_to_text
        )
        QWidget.setTabOrder(self.insert_assigned_to_text, self.insert_purchase_date_fmt)
        QWidget.setTabOrder(self.insert_purchase_date_fmt, self.insert_install_date_fmt)
        QWidget.setTabOrder(
            self.insert_install_date_fmt, self.insert_replacement_date_fmt
        )
        QWidget.setTabOrder(self.insert_replacement_date_fmt, self.insert_notes_text)
        QWidget.setTabOrder(self.insert_notes_text, self.insert_insert_button)
        QWidget.setTabOrder(
            self.insert_insert_button, self.insert_clear_selections_button
        )
        QWidget.setTabOrder(
            self.insert_clear_selections_button, self.checkbox_assignedto
        )
        QWidget.setTabOrder(self.checkbox_assignedto, self.checkbox_assetlocation)
        QWidget.setTabOrder(self.checkbox_assetlocation, self.checkbox_purchasedate)
        QWidget.setTabOrder(self.checkbox_purchasedate, self.checkbox_installdate)
        QWidget.setTabOrder(self.checkbox_installdate, self.checkbox_replacementdate)
        QWidget.setTabOrder(self.checkbox_replacementdate, self.checkbox_notes)
        QWidget.setTabOrder(self.checkbox_notes, self.checkbox_model)
        QWidget.setTabOrder(self.checkbox_model, self.filter_column_button)
        QWidget.setTabOrder(self.filter_column_button, self.filter_options_combobox)
        QWidget.setTabOrder(self.filter_options_combobox, self.filter_user_text)
        QWidget.setTabOrder(self.filter_user_text, self.filter_clear_button)
        QWidget.setTabOrder(self.filter_clear_button, self.ham_menu_button)
        QWidget.setTabOrder(self.ham_menu_button, self.ham_button_insert)
        QWidget.setTabOrder(self.ham_button_insert, self.ham_button_analytics)
        QWidget.setTabOrder(self.ham_button_analytics, self.main_table)
        QWidget.setTabOrder(self.main_table, self.refresh_table_button)
        QWidget.setTabOrder(self.refresh_table_button, self.view_columns_button)
        QWidget.setTabOrder(self.view_columns_button, self.checkbox_name)
        QWidget.setTabOrder(self.checkbox_name, self.checkbox_serial)
        QWidget.setTabOrder(self.checkbox_serial, self.checkbox_manufacturer)
        QWidget.setTabOrder(self.checkbox_manufacturer, self.checkbox_price)
        QWidget.setTabOrder(self.checkbox_price, self.insert_status_bool)
        QWidget.setTabOrder(self.insert_status_bool, self.ham_button_view)
        QWidget.setTabOrder(self.ham_button_view, self.insert_asset_category_add_option)
        QWidget.setTabOrder(
            self.insert_asset_category_add_option, self.insert_asset_type_add_option
        )
        QWidget.setTabOrder(
            self.insert_asset_type_add_option, self.insert_asset_location_add_option
        )
        QWidget.setTabOrder(
            self.insert_asset_location_add_option, self.checkbox_assetcategory
        )
        QWidget.setTabOrder(self.checkbox_assetcategory, self.insert_uuid_text)
        QWidget.setTabOrder(self.insert_uuid_text, self.checkbox_assettype)
        QWidget.setTabOrder(self.checkbox_assettype, self.ham_button_reports)
        QWidget.setTabOrder(self.ham_button_reports, self.analytics_field_combobox_top)
        QWidget.setTabOrder(
            self.analytics_field_combobox_top, self.analytics_field_combobox_top_2
        )
        QWidget.setTabOrder(
            self.analytics_field_combobox_top_2, self.analytics_export_top_button
        )
        QWidget.setTabOrder(
            self.analytics_export_top_button, self.analytics_x_axis_text
        )
        QWidget.setTabOrder(self.analytics_x_axis_text, self.analytics_y_axis_text)
        QWidget.setTabOrder(
            self.analytics_y_axis_text, self.analytics_update_top_view_button
        )
        QWidget.setTabOrder(
            self.analytics_update_top_view_button, self.analytics_field_combobox_bottom
        )
        QWidget.setTabOrder(
            self.analytics_field_combobox_bottom, self.analytics_field_combobox_bottom_2
        )
        QWidget.setTabOrder(
            self.analytics_field_combobox_bottom_2, self.analytics_export_bottom_button
        )
        QWidget.setTabOrder(self.analytics_export_bottom_button, self.calendarWidget)
        QWidget.setTabOrder(self.calendarWidget, self.reports_export_file_combobox)
        QWidget.setTabOrder(
            self.reports_export_file_combobox, self.reports_export_export_all_radio
        )
        QWidget.setTabOrder(
            self.reports_export_export_all_radio, self.reports_export_export_EOL_radio
        )
        QWidget.setTabOrder(
            self.reports_export_export_EOL_radio, self.reports_export_EOL_text
        )
        QWidget.setTabOrder(
            self.reports_export_EOL_text, self.reports_export_export_location_radio
        )
        QWidget.setTabOrder(
            self.reports_export_export_location_radio,
            self.reports_export_location_combobox,
        )
        QWidget.setTabOrder(
            self.reports_export_location_combobox,
            self.reports_export_export_retired_radio,
        )
        QWidget.setTabOrder(
            self.reports_export_export_retired_radio,
            self.reports_export_retired_assets_combobox,
        )
        QWidget.setTabOrder(
            self.reports_export_retired_assets_combobox,
            self.reports_export_main_export_button,
        )
        QWidget.setTabOrder(
            self.reports_export_main_export_button, self.export_file_path_choice
        )
        QWidget.setTabOrder(self.export_file_path_choice, self.export_file_dialog)
        QWidget.setTabOrder(self.export_file_dialog, self.settings_backup_dir_text)
        QWidget.setTabOrder(
            self.settings_backup_dir_text, self.settings_darkmode_checkbox
        )
        QWidget.setTabOrder(
            self.settings_darkmode_checkbox, self.settings_update_button
        )
        QWidget.setTabOrder(
            self.settings_update_button, self.settings_report_auto_open_checkbox
        )

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionCreate_Backup)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionClose_ALT_F4)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Invisible Man", None)
        )
        self.actionInsert.setText(
            QCoreApplication.translate("MainWindow", "Insert", None)
        )
        self.actionSettings.setText(
            QCoreApplication.translate("MainWindow", "Settings", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.actionCreate_Backup.setText(
            QCoreApplication.translate("MainWindow", "Create Backup", None)
        )
        self.actionClose_ALT_F4.setText(
            QCoreApplication.translate(
                "MainWindow", "Close                  ALT-F4", None
            )
        )
        self.ham_menu_button.setText(
            QCoreApplication.translate("MainWindow", "ham menu", None)
        )
        self.ham_button_insert.setText(
            QCoreApplication.translate("MainWindow", "Insert", None)
        )
        self.ham_button_analytics.setText(
            QCoreApplication.translate("MainWindow", "Analytics", None)
        )
        self.ham_button_reports.setText(
            QCoreApplication.translate("MainWindow", "Reports", None)
        )
        self.ham_button_view.setText(
            QCoreApplication.translate("MainWindow", "View", None)
        )
        self.refresh_table_button.setText(
            QCoreApplication.translate("MainWindow", "Refresh", None)
        )
        self.view_columns_button.setText(
            QCoreApplication.translate("MainWindow", "View", None)
        )
        self.checkbox_name.setText(
            QCoreApplication.translate("MainWindow", "Name", None)
        )
        self.checkbox_serial.setText(
            QCoreApplication.translate("MainWindow", "Serial", None)
        )
        self.checkbox_manufacturer.setText(
            QCoreApplication.translate("MainWindow", "Manufacturer", None)
        )
        self.checkbox_price.setText(
            QCoreApplication.translate("MainWindow", "Price", None)
        )
        self.checkbox_assetcategory.setText(
            QCoreApplication.translate("MainWindow", "Asset Category", None)
        )
        self.checkbox_assettype.setText(
            QCoreApplication.translate("MainWindow", "Asset Type", None)
        )
        self.checkbox_assignedto.setText(
            QCoreApplication.translate("MainWindow", "Assigned To", None)
        )
        self.checkbox_assetlocation.setText(
            QCoreApplication.translate("MainWindow", "Asset Location", None)
        )
        self.checkbox_purchasedate.setText(
            QCoreApplication.translate("MainWindow", "Purchase Date", None)
        )
        self.checkbox_installdate.setText(
            QCoreApplication.translate("MainWindow", "Install Date", None)
        )
        self.checkbox_replacementdate.setText(
            QCoreApplication.translate("MainWindow", "Replacement Date", None)
        )
        self.checkbox_notes.setText(
            QCoreApplication.translate("MainWindow", "Notes", None)
        )
        self.checkbox_model.setText(
            QCoreApplication.translate("MainWindow", "Model", None)
        )
        self.filter_column_button.setText(
            QCoreApplication.translate("MainWindow", "Filter", None)
        )
        self.filter_clear_button.setText(
            QCoreApplication.translate("MainWindow", "X", None)
        )
        self.insert_bold_equals_required_info.setText(
            QCoreApplication.translate(
                "MainWindow", "Bold indicates a required field", None
            )
        )
        self.insert_name_text.setText("")
        self.insert_name_label.setText(
            QCoreApplication.translate("MainWindow", "Name", None)
        )
        self.insert_serial_label.setText(
            QCoreApplication.translate("MainWindow", "Serial #", None)
        )
        self.insert_serial_text.setText("")
        self.insert_manufacture_label.setText(
            QCoreApplication.translate("MainWindow", "Manufacturer", None)
        )
        self.insert_manufacturer_text.setText("")
        self.insert_price_label.setText(
            QCoreApplication.translate("MainWindow", "Price", None)
        )
        self.insert_asset_category_label.setText(
            QCoreApplication.translate("MainWindow", "Asset Category", None)
        )
        self.insert_asset_type_label.setText(
            QCoreApplication.translate("MainWindow", "Asset Type", None)
        )
        self.insert_asset_location_label.setText(
            QCoreApplication.translate("MainWindow", "Asset Location", None)
        )
        self.insert_assigned_to_label.setText(
            QCoreApplication.translate("MainWindow", "Assigned To", None)
        )
        self.insert_assigned_to_text.setText("")
        self.insert_purchase_date_label.setText(
            QCoreApplication.translate("MainWindow", "Purchase Date", None)
        )
        self.insert_install_date_label.setText(
            QCoreApplication.translate("MainWindow", "Install Date", None)
        )
        self.insert_replacement_date_label.setText(
            QCoreApplication.translate("MainWindow", "Replacement Date", None)
        )
        self.insert_notes_label.setText(
            QCoreApplication.translate("MainWindow", "Notes", None)
        )
        self.insert_status_label.setText(
            QCoreApplication.translate("MainWindow", "Status", None)
        )
        self.insert_asset_category_add_option.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.insert_asset_type_add_option.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.insert_asset_location_add_option.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.insert_insert_button.setText(
            QCoreApplication.translate("MainWindow", "Insert!", None)
        )
        self.insert_uuid_label.setText(
            QCoreApplication.translate("MainWindow", "UUID", None)
        )
        self.insert_uuid_text.setText("")
        self.insert_clear_selections_button.setText(
            QCoreApplication.translate("MainWindow", "Clear", None)
        )
        self.insert_model_label.setText(
            QCoreApplication.translate("MainWindow", "Model", None)
        )
        self.insert_model_text.setText("")
        self.analytics_export_top_button.setText(
            QCoreApplication.translate("MainWindow", "Export", None)
        )
        # if QT_CONFIG(tooltip)
        self.analytics_x_axis_label.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.analytics_x_axis_label.setText(
            QCoreApplication.translate("MainWindow", "X Axis Values", None)
        )
        # if QT_CONFIG(tooltip)
        self.analytics_x_axis_text.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.analytics_y_axis_text.setText("")
        self.analytics_y_axis_label.setText(
            QCoreApplication.translate("MainWindow", "Y Axis Values", None)
        )
        self.analytics_update_top_view_button.setText(
            QCoreApplication.translate("MainWindow", "Update View", None)
        )
        self.analytics_export_bottom_button.setText(
            QCoreApplication.translate("MainWindow", "Export", None)
        )
        self.reports_total_asset_value_label.setText(
            QCoreApplication.translate("MainWindow", "Total Asset Value", None)
        )
        self.reports_dollarsign_label.setText(
            QCoreApplication.translate("MainWindow", "$", None)
        )
        self.reports_asset_integer_label.setText(
            QCoreApplication.translate("MainWindow", "10,000", None)
        )
        self.reports_export_main_label.setText(
            QCoreApplication.translate("MainWindow", "Export", None)
        )
        self.reports_export_export_file_label.setText(
            QCoreApplication.translate("MainWindow", "Export File", None)
        )
        self.reports_export_export_all_info_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Exports every field, every entry into the\n" "file type of choice",
                None,
            )
        )
        self.reports_export_export_all_radio.setText(
            QCoreApplication.translate("MainWindow", "Export All", None)
        )
        self.reports_export_export_EOL_radio.setText(
            QCoreApplication.translate("MainWindow", "Export End of Life in:", None)
        )
        self.reports_export_export_location_radio.setText(
            QCoreApplication.translate("MainWindow", "Export Asset by Location:", None)
        )
        self.reports_export_export_retired_radio.setText(
            QCoreApplication.translate("MainWindow", "Retired Assets", None)
        )
        self.reports_export_main_export_button.setText(
            QCoreApplication.translate("MainWindow", "Export!", None)
        )
        self.reports_export_status_label.setText(
            QCoreApplication.translate("MainWindow", "Status:", None)
        )
        self.reports_export_status_content.setText("")
        self.export_file_dialog.setText(
            QCoreApplication.translate("MainWindow", "..", None)
        )
        self.settings_backup_dir_label.setText(
            QCoreApplication.translate("MainWindow", "Backup Directory Path", None)
        )
        self.settings_darkmode_label.setText(
            QCoreApplication.translate("MainWindow", "Dark Mode", None)
        )
        self.settings_darkmode_checkbox.setText(
            QCoreApplication.translate("MainWindow", "CheckBox", None)
        )
        self.settings_update_button.setText(
            QCoreApplication.translate("MainWindow", "Update", None)
        )
        self.settings_report_auto_open_label.setText(
            QCoreApplication.translate(
                "MainWindow", "Auto-open report in explorer", None
            )
        )
        self.settings_report_auto_open_checkbox.setText(
            QCoreApplication.translate("MainWindow", "CheckBox", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))

    # retranslateUi
