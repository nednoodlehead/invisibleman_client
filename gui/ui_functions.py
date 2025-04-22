import psycopg2
from gui.auto import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QPushButton,
    QMessageBox,
    QMenu,
    QTableWidget,
    QCheckBox,
    QAction,
    QStyleFactory,
    QFileDialog,
)
from PyQt5.QtCore import QDate, Qt, QDate, QFile, QTextStream, QRect, pyqtSignal
from PyQt5.QtGui import QCursor, QPainter, QColor, QTextCharFormat
from util.data_types import InventoryObject, TableObject, create_inventory_object
from util.db_util import patch_dates
from util.export import export_active, export_retired, export_loc, export_replacementdate
from db.fetch import fetch_all, fetch_all_enabled_for_table, fetch_from_uuid_to_update, fetch_all_for_table, fetch_all_serial, fetch_by_serial
from db.insert import new_entry
from db.update import update_full_obj, delete_from_uuid, retire_from_uuid, unretire_from_uuid
from gui.notes_window import NotesWindow
from gui.export_graph_window import ExportGraph
from gui.settings import dark_light_mode_switch, set_dark
from util.export import create_backup
from volatile.write_to_volatile import write_to_config, read_from_config
from data.visualization import DataCanvas
from types import MethodType
from gui.insert_functions import (
    fetch_categories_and_years,
    force_json_sync,
    update_replacement_date,
    refresh_asset_types,
    add_asset_type,
    refresh_asset_categories,
    fetch_all_asset_types,
    refresh_asset_location,
    refresh_manufacturer
)
from gui.add_item_window import GenericAddJsonWindow
from datetime import datetime
from psycopg2 import connect
from sshtunnel import SSHTunnelForwarder, BaseSSHTunnelForwarderError
from gui.thread import PostgresListen
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from keyring import get_password
from gui.overrides import InvisManItem
# DEFAULT_DATE = datetime.strptime("2000-01-01", "%Y-%m-%d")

class MainProgram(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.config = read_from_config()
        self.imported_methods()  # call the imported methods into scope of the class
        # we must check config to see if there are (at all!!) settings for the invisman server and stuff
        # because someone booting for the first time wont have the configurations configured..
        # we also have to do checks for where self.connection is used, so it doesn't goof everything if the person doesn't
        # have anything configured yet
        self.connection = self.create_db_connection(self.config["invisman_username"], self.config["ssh_path"], self.config["invisman_ip"])
        self.worker_signal = pyqtSignal(str)
        # patch_dates(self.connection, self.fetch_categories_and_years()) # was a o
        self.active_notes_window = None
        self.active_json_window = None
        self.active_export_graph_window = None
        self.insert_active_uuid = ""  # this is our variable for knowing if we are
        # editing an entry, or adding a new one. depends if it is empty string, or uuid4
        self.default_columns = [
            "Asset Type",
            "Manufacturer",
            "Serial Number",
            "Model",
            "Cost",
            "Assigned To",
            "Name",
            "Asset Location",
            "Asset Category",
            "Deployment Date",
            "Replacement Date",
            # retirement date would go here...
            "Notes",
        ]
        self.when_can_assets_retire = [
            "3 Months",
            "6 Months",
            "9 Months",
            "12 Months",
            "24 Months"
        ]
        # self.setStyle(QStyleFactory.create("Fusion"))
        # there is some argument to use a QTableView instead of a QTableWidget, since the view better supports
        # M/V style programming, which would (in theory) significantly improve the performance of certain
        # operations, namely filtering. would require quite a lot of refactoring though. so maybe another time :)
        # https://stackoverflow.com/questions/6785481/how-to-implement-a-filter-option-in-qtablewidget
        # the concept is that QTableWidget has a built-in model, and a QTableView does not, so you can edit it
        # ui functions
        if self.connection is not False: # this is when the connection is made successfully!
            self.force_json_sync(self.connection)
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.populate_table_with(fetch_all_enabled_for_table(self.connection), False)
        self.ham_button_insert.clicked.connect(lambda: self.swap_to_window(1))
        self.ham_button_view.clicked.connect(lambda: self.swap_to_window(0))
        self.ham_button_analytics.clicked.connect(lambda: self.swap_to_window(2))
        self.ham_button_reports.clicked.connect(self.swap_reports_refresh)
        self.ham_button_settings.clicked.connect(lambda: self.swap_to_window(4))
        self.insert_asset_category_combobox.currentIndexChanged.connect(
            self.update_replacement_date
        )
        self.insert_conditional_retirement_date_fmt.setDate(QDate.currentDate())
        self.insert_insert_button.clicked.connect(self.check_data_and_insert)
        self.insert_clear_selections_button.clicked.connect(
            self.set_insert_data_to_default
        )
        self.refresh_table_button.clicked.connect(
            # this just refreshes the assets, taking into account the checkbox for retired
            self.toggle_retired_assets
        )
        # self.main_table.setSortingEnabled(True) # YOU!! this causes the weird inconsistencies..
        # removed since i think it is a bit of over-engineering
        # self.view_columns_button.clicked.connect(self.view_button_reveal_checkboxes)
        self.checkbox_view_retired_assets.clicked.connect(self.toggle_retired_assets)
        self.settings_update_button.clicked.connect(self.write_config)
        self.filter_column_button.clicked.connect(self.handle_filter_request)
        self.filter_options_combobox.addItem("Global")
        self.filter_options_combobox.addItems(self.default_columns)
        self.reports_export_file_combobox.addItems(["Excel", "CSV"])
        self.reports_export_location_combobox.addItems(self.refresh_asset_location(self.connection))
        self.reports_export_export_due_replacement_combo.addItems(self.when_can_assets_retire)
        self.insert_deployment_date_fmt.setDisplayFormat(
            "yyyy-MM-dd"
        )  # thanks qt5 for randomly changing the default display format... commi #108
        self.export_file_dialog_button.clicked.connect(self.open_report_file_dialog)
        self.settings_file_dialog_button.clicked.connect(self.open_settings_file_dialog)
        self.setting_ssh_file_dialog_button.clicked.connect(self.open_settings_ssh_file_dialog)
        self.insert_replacement_date_fmt.setDisplayFormat("yyyy-MM-dd")
        self.insert_conditional_retirement_date_fmt.setDisplayFormat("yyyy-MM-dd")
        # when date is changed, update the replacement date accordingly
        self.insert_deployment_date_fmt.dateChanged.connect(self.update_replacement_date)
        self.analytics_export_top_button.clicked.connect(
            lambda: self.export_graph(True)
        )
        self.analytics_update_top_view_button.clicked.connect(
            self.update_analytics_top_graph
        )
        # allow us to reach settings
        self.settings_darkmode_checkbox.clicked.connect(
            lambda: dark_light_mode_switch(
                self, self.settings_darkmode_checkbox.isChecked()
            )
        )
        if self.config["dark_mode"] is True:
            self.settings_darkmode_checkbox.setChecked(True)
            set_dark(self)
        else:
            self.setStyleSheet(
                "QFrame#reports_export_frame{border: 1px solid black;\nborder-radius: 15px;}"
            )
        if self.config["auto_open_report_on_create"] is True:
            self.settings_report_auto_open_checkbox.setChecked(True)
        self.settings_backup_dir_text.setText(self.config["backup_path"])
        self.settings_invisman_username_text.setText(self.config["invisman_username"])
        self.settings_ssh_file_text.setText(self.config["ssh_path"])
        self.settings_ip_text.setText(self.config["invisman_ip"])
        # opens with height == 250, so no need to `else` set that..
        self.insert_widgets = [
            self.checkbox_assettype,
            self.checkbox_manufacturer,
            self.checkbox_serial,
            self.checkbox_model,
            self.checkbox_cost,
            self.checkbox_assignedto,
            self.checkbox_name,
            self.checkbox_assetlocation,
            self.checkbox_assetcategory,
            self.checkbox_deploymentdate,
            self.checkbox_replacementdate,
            self.checkbox_notes,
        ]
        # enabled by default, we will set the width to 0 :)
        self.insert_conditional_status_frame.setFixedWidth(0)
        self.insert_status_bool.activated.connect(self.hide_or_show_insert_conditional)
        for count, checkbox in enumerate(self.insert_widgets):
            self.handle_checkboxes_and_columns(count, checkbox)
        # populating combo boxes. "" is an empty default value
        cat, typ, loc, manu = self.fetch_all_asset_types()
        self.insert_asset_category_combobox.addItem("")
        self.insert_asset_type_combobox.addItem("")
        self.insert_asset_location_combobox.addItem("")
        self.insert_manufacturer_combobox.addItem("")
        self.insert_asset_category_combobox.addItems(cat)
        self.insert_asset_type_combobox.addItems(typ)
        self.insert_asset_location_combobox.addItems(loc)
        self.insert_manufacturer_combobox.addItems(manu)
        # true = retired, false = in use
        self.insert_status_bool.addItems(["Active", "Retired"])
        # thr possible? might be quicker to load "non-visible by defualt" content on sep thread
        self.insert_deployment_date_fmt.setDate(QDate.currentDate())
        self.insert_replacement_date_fmt.setDate(QDate.currentDate())
        self.insert_cost_spinbox.setMaximum(99999.99)
        # leave the insert_replacement_date_fmt for when the user selects the hardware type
        self.insert_asset_category_add_option.clicked.connect(
            lambda: self.display_generic_json("Category")
        )
        self.insert_asset_type_add_option.clicked.connect(
            lambda: self.display_generic_json("Type")
        )
        self.insert_asset_location_add_option.clicked.connect(
            lambda: self.display_generic_json("Location")
        )
        self.insert_manufacturer_add_option.clicked.connect(
            lambda: self.display_generic_json("Manufacturer")
        )
        self.filter_clear_button.clicked.connect(self.clear_filter)
        self.export_file_path_choice.setText(self.config["default_report_path"])
        self.reports_export_main_export_button.clicked.connect(
            self.interface_handle_export
        )
        # edit buttons
        self.set_table_size_and_headers(self.default_columns)
        self.main_table.setContextMenuPolicy(Qt.CustomContextMenu)  # error for no reason..?
        self.main_table.customContextMenuRequested.connect(
            self.display_table_context_menu
        )

        # threaded analyitics spawning :)
        self.graphs_and_charts_top = ["Line", "Bar"]
        self.acceptable_all_charts = [
            "Manufacturer",
            "Asset Category",
            "Asset Type",
            "Asset Location",
            "Deployment Date",
            "Replacement Date",
        ]
        self.acceptable_pie_charts = self.acceptable_all_charts.copy()
        self.acceptable_pie_charts.append("Notes")
        self.analytics_field_combobox_top.addItems(self.graphs_and_charts_top)
        self.analytics_field_combobox_bottom.addItems(self.acceptable_pie_charts)
        self.graph_1 = DataCanvas(
            conn=self.connection,
            parent=self.analytics_graph_top,
            width=10,
            height=4,
            dpi=100,
            height_2=290,
            width_2=790,
        )
        self.analytics_field_combobox_bottom.addItems(self.graphs_and_charts_top)
        # self.graph_2.figure.subplots_adjust(left=-0.1)  # was used to move the pie chart. Fine where is
        self.analytics_field_combobox_top.currentIndexChanged.connect(
            lambda: self.graph_1.change_graph(
                self.analytics_field_combobox_bottom.currentText(),
                self.analytics_field_combobox_top.currentText(),
            )
        )
        self.analytics_field_combobox_bottom.currentIndexChanged.connect(
            lambda: self.graph_1.change_graph(
                self.analytics_field_combobox_bottom.currentText(),
                self.analytics_field_combobox_top.currentText(),
            )
        )
        self.calendarWidget.clicked[QDate].connect(self.on_calendar_click)
        # configure the serial input to update the button next to it
        self.insert_serial_text.textChanged.connect(self.serial_input_typed)
        # set the button as disabled because it does not match a serial number
        # see self.serial_input_typed for more
        self.insert_serial_is_unique_button.setEnabled(False)
        self.insert_serial_is_unique_button.clicked.connect(self.pull_unique_uuid_data)
        # should be threaded?: edit: doesnt seem too bad on performance somehow...
        # okay, so if the connection isn't initialized, we can ignore this part
        # since the data doesn't matter, and the thread wont matter either
        # the user can use the "Test Connection"
        if self.connection is not False:
            self.graph_1.change_graph(
                self.config["top_graph_data"], self.config["top_graph_type"]
            )
            self.analytics_field_combobox_top.setCurrentText(self.config["top_graph_data"])
            self.update_calendar_colors_from_db()
            self.settings_update_button.clicked.connect(self.write_config_tell_user)

            # postgres thread...
            self.postgres_listen_thread = PostgresListen(self.connection)
            self.postgres_listen_thread.start()
            self.postgres_listen_thread.notifier.connect(self.force_sync)

    # overwritten methods

    def closeEvent(self, a0):
        self.write_config()
        if self.connection is not False:
            # in the first-startup case where the user hasn't set the ip correctly
            self.connection.close() # close connection after we exit app..
        a0.accept()  # another random complaint from pyright

    # regular methods
    def imported_methods(self):
        # for loop at some point? lmao
        self.update_replacement_date = MethodType(update_replacement_date, self)
        self.refresh_asset_types = MethodType(refresh_asset_types, self)
        self.refresh_asset_category = MethodType(refresh_asset_categories, self)
        self.refresh_asset_location = MethodType(refresh_asset_location, self)
        self.refresh_manufacturer = MethodType(refresh_manufacturer, self)
        self.fetch_all_asset_types = MethodType(fetch_all_asset_types, self)
        self.force_json_sync = MethodType(force_json_sync, self)
        self.fetch_categories_and_years = MethodType(fetch_categories_and_years, self)

    def display_message(self, title: str, information: str):
        msg = QMessageBox()
        msg.setText(information)
        msg.setWindowTitle(title)
        msg.exec_()

    def display_table_context_menu(self, position=None):
        menu = QMenu()
        # we need to determine if the select row is retired or normal
        # so we can add the correct button (retire / unretire) and the correct slot
        index = self.main_table.indexAt(position)
        row = index.row()
        # item will be none if the retirment date row is not shown
        retirement_option = self.main_table.item(row, 13)
        menu.addAction(
            "Update",
            lambda: self.try_update_row(
                position
            ),
        )
        our_uuid = self.main_table.item(row, 12).text()
        if retirement_option:
            if retirement_option.text() != "":
                menu.addAction("Unretire", lambda: self.try_unretire_row(our_uuid))
            else:
                # option when retired assets are visible, but we click on a non-retired asset
                menu.addAction(
                    "Retire",
                    lambda: self.try_retire_row(our_uuid),
                )
        else:
            menu.addAction(
                "Retire",
                lambda: self.try_retire_row(our_uuid),
            )
        menu.exec_(QCursor.pos())

    def delete_and_remove_row(self, row):
        id = self.main_table.item(row, 14).text()
        delete_from_uuid(self.connection, id)
        self.main_table.removeRow(row)

    def view_button_reveal_checkboxes(self):
        if self.view_toggle_frame.width() == 800:
            self.view_toggle_frame.setFixedWidth(80)
        else:
            self.view_toggle_frame.setFixedWidth(800)

    def handle_checkboxes_and_columns(
        self, column: int, box: QCheckBox
    ):  # creates the buttons for the checkboxes for disabling columns
        # box.clicked.connect(lambda: self.main_table.setColumnHidden(column, not box.isChecked))

        def button_target():  # silly nested method doesn't want to be a lambda...
            self.main_table.setColumnHidden(column, not box.isChecked())

        # if you replace this function and col with lambda, it does not work. on god
        box.clicked.connect(button_target)
        if self.config["checkboxes"][self.default_columns[column]] is True:
            box.setChecked(True)
        else:
            self.main_table.setColumnHidden(column, True)
            pass  # set setchecked false by default on startup?

    def tester(self):  # ignore this!
        print("here")

    def open_report_file_dialog(
        self,
    ):  # when selecting the directory to store backups, it calls this
        filedialog = QFileDialog(self)
        filedialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
        path = filedialog.getExistingDirectory(self)
        if path is not None and path != "":
            self.export_file_path_choice.setText(path)

    def open_settings_file_dialog(self):
        filedialog = QFileDialog(self)
        filedialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
        path = filedialog.getExistingDirectory(self)
        if path is not None and path != "":
            self.settings_backup_dir_text.setText(path)
            
    def open_settings_ssh_file_dialog(self):
        filedialog = QFileDialog(self)
        path = filedialog.getOpenFileName(self)
        if path is not None and path != "":
            try:
                self.settings_ssh_file_text.setText(path[0])
            except TypeError: # when the user exits out of the menu...
                print("type error lol", path) 
                pass

    def refresh_asset_value(
        self,
    ):  # refresh the asset value, called on startup, and when new obj is made
        # i dont see a scenario where the db would have different data than self.main_table
        # with a whole lot of rows this might be slower than db query...
        total = 0
        for row_count in range(self.main_table.rowCount()):
            for column_count in range(self.main_table.columnCount()):
                if column_count == 4:
                    item = self.main_table.item(row_count, column_count)
                    if (
                        item is not None
                    ):  # no reason to check for non int/float, since input is sanitized
                        total += float(item.text())
        # add commas between numbers...
        # we removed this for now...
        # self.reports_asset_integer_label.setText(f"{total:,.2f}")

    def update_calendar_colors_from_db(self):
        # should probably thread this...
        # ok maybe there is some way to create a new cell type, then add that to the stylesheets,
        # but i think this might require a hack and saw...
        raw_data = fetch_all(self.connection)
        mapping = {}
        dark = self.settings_darkmode_checkbox.isChecked()
        increment = 35 if dark else -35
        # different colors for dark vs light mode..
        default_color = (70, 0, 0) if dark else (255, 200, 200)
        for obj in raw_data:
            # i think that if a max color falls on a weekend, it will be hard to read...
            # TODO unnecessary type cast? probs a better functions to use from QDate
            date = QDate.fromString(str(obj.replacementdate), "yyyy-MM-dd")
            if date not in mapping.keys():
                mapping[date] = QColor(*default_color)
            else:
                if dark:
                    if mapping[date].red() > 220:
                        continue
                    mapping[date].setRed(
                        mapping[date].red() + increment
                    )  # no check for max?
                else:
                    if mapping[date].green() < 45:
                        continue
                    mapping[date].setGreen(
                        mapping[date].green() + increment
                    )  # no check for max?
                    mapping[date].setBlue(mapping[date].blue() + increment)
        for date, color in mapping.items():
            cell = QTextCharFormat()
            cell.setBackground(color)
            self.calendarWidget.setDateTextFormat(date, cell)

    def on_calendar_click(self, date: QDate):
        # hide table by the date string, and swap to main view
        color = self.calendarWidget.dateTextFormat(date).background().color().getHsv()
        if not color == (-1, 0, 0, 255):
            self.clear_filter()
            self.filter_certain_column(
                date.toString("yyyy-MM-dd"),
                self.default_columns.index("Replacement Date"),
            )  # 7 should be replacment..
            self.swap_to_window(0)  # should only swap if it is valid...
            self.filter_options_combobox.setCurrentIndex(10)
        # can you tell if it is valid without iteration? color!

    def update_analytics_top_graph(self):
        # self.graph_1.axes.cla()  # clear the graph
        # self.graph_1.axes.autoscale()
        # holy hell this is torture. these stupid graphs are sooo finicky and hard to control
        # like can u not just read my mind !?
        try:
            x_axis = list(map(int, self.analytics_x_axis_text.text().split(",")))
            self.graph_1.axes.set_xticks(x_axis)
            self.graph_1.axes.set_xticklabels(x_axis)
        except ValueError:
            x_axis = self.analytics_x_axis_text.text()
            if x_axis != "":
                self.graph_1.axes.set_xticks([])
                self.graph_1.axes.set_xlabel(x_axis)
        try:
            y_axis = list(map(int, self.analytics_y_axis_text.text().split(",")))
            self.graph_1.axes.set_yticks(y_axis)
            self.graph_1.axes.set_yticklabels(y_axis)
        except ValueError:
            y_axis = self.analytics_y_axis_text.text()
            if y_axis != "":
                self.graph_1.axes.set_yticks([])
                self.graph_1.axes.set_yticklabels(y_axis)

        data = self.graph_1.fetch_from_db_and_insert(
            self.analytics_field_combobox_top.currentText()
        )
        # self.graph_1.axes.set_title(self.analytics_field_combobox_top.currentText())
        if self.analytics_field_combobox_top_2.currentText() == "Line":
            self.graph_1.axes.plot(data.values())  # plot the
            names = list(data.keys())
            for count, val in enumerate(data.values()):
                self.graph_1.axes.text(count, val, names[count])
            self.graph_1.draw()

        else:  # bar graph
            # data.values = frequency
            # data.keys = name
            self.graph_1.axes.bar(
                data.keys(), data.values(), color="maroon", width=0.2, align="edge"
            )
            names = list(data.keys())
            self.graph_1.draw()

    def swap_reports_refresh(self):
        self.stackedWidget.setCurrentIndex(3)
        self.refresh_asset_value()

    def hide_or_show_insert_conditional(self):
        if self.insert_status_bool.currentIndex() == 0:  # its active...
            self.insert_conditional_status_frame.setFixedWidth(0)
        else:
            self.insert_conditional_status_frame.setFixedWidth(270)
        
    def interface_handle_export(self):
        csv_val = (
            True if self.reports_export_file_combobox.currentText() == "CSV" else False
        )
        # ensure there is a / at the end :)
        user_file = self.export_file_path_choice.text()
        user_file = user_file if user_file.endswith("/") is False else f"{user_file}/"
        filename = f'{user_file}/{str(datetime.now()).replace(":", "-")[:19]}'  # should always end in a /, need to validate elsewhere
        if self.reports_export_export_active_radio.isChecked():
            export_active(self, csv_val, filename)
        elif self.reports_export_export_retired_radio.isChecked():
            export_retired(self, csv_val, filename)
        elif self.reports_export_export_location_radio.isChecked():
            # cant be none...
            export_loc(
                self,
                csv_val,
                filename,
                self.reports_export_location_combobox.currentText(),
            )
        elif self.reports_export_export_due_replacement_radio.isChecked():
            # also cant be none, no null check required.. :)
            export_replacementdate(
                self,
                csv_val,
                filename,
                self.reports_export_export_due_replacement_combo.currentText()
            )  # retired assets by year
        else:  # edge case where the user selects none of them
            self.display_message("Error!", "Please select one of the radio buttons!")

    def send_update_data_to_insert(
        self, index
    ):  # prepare everything for update_insert_page_from_obj
        uuid = self.main_table.item(index, 12).text()
        obj = fetch_from_uuid_to_update(self.connection, uuid)
        self.swap_to_window(1)
        self.update_insert_page_from_obj(obj)

    def update_insert_page_from_obj(
        self, inventory_obj: InventoryObject
    ):  # fill the insert page with the
        # content given from choosen updated entry
        self.insert_serial_text.setText(inventory_obj.serial)
        self.insert_name_text.setText(inventory_obj.name)
        self.insert_model_text.setText(inventory_obj.model)
        self.insert_cost_spinbox.setValue(float(inventory_obj.cost))
        cat_index = self.insert_asset_category_combobox.findText(
            inventory_obj.assetcategory
        )
        self.insert_asset_category_combobox.setCurrentIndex(cat_index)
        type_index = self.insert_asset_type_combobox.findText(inventory_obj.assettype)
        self.insert_asset_type_combobox.setCurrentIndex(type_index)
        loc_index = self.insert_asset_location_combobox.findText(
            inventory_obj.assetlocation
        )
        self.insert_asset_location_combobox.setCurrentIndex(loc_index)
        manu_index = self.insert_manufacturer_combobox.findText(inventory_obj.manufacturer)
        self.insert_manufacturer_combobox.setCurrentIndex(manu_index)
        self.insert_assigned_to_text.setText(inventory_obj.assignedto)
        if not inventory_obj.replacementdate or inventory_obj.replacementdate == "":
            inventory_obj.replacementdate = datetime.fromisoformat("2000-01-01")
        print(inventory_obj.replacementdate, type(inventory_obj.replacementdate))
        self.insert_deployment_date_fmt.setDate(inventory_obj.deploymentdate)
        self.insert_replacement_date_fmt.setDate(
            inventory_obj.replacementdate
        )
        self.insert_notes_text.setText(inventory_obj.notes)
        if inventory_obj.status == 1:
            # retired
            self.insert_status_bool.setCurrentIndex(1)
            # same as self.hide_or_show_insert_conditional()
            # but we skip an if statement!
            self.insert_conditional_status_frame.setFixedWidth(210)
        else:
            # not retired
            self.insert_status_bool.setCurrentIndex(0)
        self.insert_active_uuid = inventory_obj.uniqueid
        # disable the fields that 'we dont want to edit'

    def toggle_burger(self):  # toggle burger menu. TODO give it the icon
        if self.ham_menu_frame.height() == 250:
            self.ham_menu_frame.setFixedHeight(50)

        else:
            self.ham_menu_frame.setFixedHeight(250)

    def swap_to_window(self, index: int):  # change stackedwiget index
        self.stackedWidget.setCurrentIndex(index)
        # grey out button that is selected by index?

    def write_config_tell_user(self):
        self.write_config()  # what if error?
        self.display_message("Success!", "Config saved!")
        self.swap_to_window(0)  # back to main window :)

    def write_config(
        self,
    ):  # writes everything to config, called on window close (and i think alt-f4)
        # get checkbox value
        to_write = {
            "Asset Type": self.checkbox_assettype.isChecked(),
            "Manufacturer": self.checkbox_manufacturer.isChecked(),
            "Serial Number": self.checkbox_serial.isChecked(),
            "Model": self.checkbox_model.isChecked(),
            "Cost": self.checkbox_cost.isChecked(),
            "Assigned To": self.checkbox_assignedto.isChecked(),
            "Name": self.checkbox_name.isChecked(),
            "Asset Location": self.checkbox_assetlocation.isChecked(),
            "Asset Category": self.checkbox_assetcategory.isChecked(),
            "Deployment Date": self.checkbox_deploymentdate.isChecked(),
            "Replacement Date": self.checkbox_replacementdate.isChecked(),
            "Notes": self.checkbox_notes.isChecked(),
        }
        write_to_config(
            to_write,
            self.settings_darkmode_checkbox.isChecked(),
            self.settings_backup_dir_text.text(),
            self.settings_report_auto_open_checkbox.isChecked(),
            self.export_file_path_choice.text(),
            self.analytics_field_combobox_top.currentText(),
            self.analytics_field_combobox_bottom.currentText(),
            self.settings_invisman_username_text.text(),
            self.settings_ssh_file_text.text(),
            self.settings_ip_text.text()
        )

    def populate_table_with(
        self, data: list[TableObject], retirement_bool: bool=False
    ):  # put all of the content in the table from the db, called on startup, and
        # when updated..
        if len(data) == 0:
            return  # is this sort of feral?
        self.main_table.setRowCount(len(data))
        if retirement_bool:
            # this is sort of sloppy. idk
            self.main_table.setColumnCount(
                14
            )  # set the column count to the size of the first data piece
            new_headers = self.default_columns.copy()
            new_headers.append("Retirement Date")
            self.main_table.setHorizontalHeaderLabels(new_headers)
        else:
            self.main_table.setColumnCount(
                13
            )  # set the column count to the size of the first data piece
        for row, rowdata in enumerate(data):
            for col, value in enumerate(rowdata):
                item = InvisManItem(str(value))
                if col == 11:
                    if value == None: # now stored as null instead of empty string
                        button = self.generate_notes_button(
                            data[row].uniqueid, "Add Notes"
                        )
                        self.main_table.setCellWidget(row, col, button)
                    else:
                        button = self.generate_notes_button(
                            data[row].uniqueid, "View Notes"
                        )
                        self.main_table.setCellWidget(row, col, button)
                else:
                    self.main_table.setItem(row, col, item)
            # if our row is retired, we'll make that known by changing the background color of the cell!            
        # ok the concept now is that if there is a retirement date, it is retired.
        # this stupid color *stuff* is horrible. impossible to set it correctly. keeps bugging
        # for row, rowdata in enumerate(data):
        #     item = QTableWidgetItem(str(row))
        #     print(f'statu: {rowdata.status}')
        #     if rowdata.status == 1:
        #         item.setForeground(QColor(200, 0, 0))
        #     self.main_table.setVerticalHeaderItem(row, item)
        # print("\n")
    def generate_notes_button(
        self, uuid: str, display: str
    ):  # uuid so we can update to the right column
        button = QPushButton()
        button.setText(display)
        button.clicked.connect(lambda: self.display_notes(uuid))
        return button

    def display_notes(self, uuid: str):  # open the note-editing window
        # will be a text box
        self.active_notes_window = NotesWindow(self.connection, uuid)
        self.active_notes_window.show()
        position = self.pos()
        position.setX(position.x() + 250)
        position.setY(position.y() + 250)
        self.active_notes_window.move(position)

    def display_generic_json(self, target: str):  # open the json editing window
        self.active_json_window = GenericAddJsonWindow(target, self)
        self.active_json_window.show()
        position = self.pos()
        position.setX(position.x() + 250)
        position.setY(position.y() + 250)
        self.active_json_window.move(position)

    def export_graph(self, top: bool):
        if top:
            data = self.analytics_field_combobox_top.currentText()
            chart_type = self.analytics_field_combobox_top_2.currentText()
        else:
            data = self.analytics_field_combobox_bottom.currentText()
            chart_type = self.analytics_field_combobox_bottom_2.currentText()
        # TODO what is the logic here ? ^^^^
        self.active_export_graph_window = ExportGraph(self, top)
        self.active_export_graph_window.show()
        position = self.pos()
        position.setX(position.x() + 250)
        position.setY(position.y() + 250)
        self.active_export_graph_window.move(position)

    def refresh_combobox(self, target: str):  # give the comboboxes their items
        # also i dont think its possible to have a placeholder value (e.g. "") which disapears on click
        if target == "Category":
            self.insert_asset_category_combobox.clear()
            self.insert_asset_category_combobox.addItem("")
            self.insert_asset_category_combobox.addItems(self.refresh_asset_category(self.connection))
        elif target == "Type":
            self.insert_asset_type_combobox.clear()
            self.insert_asset_type_combobox.addItem("")
            self.insert_asset_type_combobox.addItems(self.refresh_asset_types(self.connection))
        elif target == "Manufacturer":
            self.insert_manufacturer_combobox.clear()
            self.insert_manufacturer_combobox.addItem("")
            self.insert_manufacturer_combobox.addItems(self.refresh_manufacturer(self.connection))
        else:
            self.insert_asset_location_combobox.clear()
            self.insert_asset_location_combobox.addItem("")
            self.insert_asset_location_combobox.addItems(self.refresh_asset_location(self.connection))

    def check_data_and_insert(
        self,
    ):  # either inserts or updtes based on uuid field presence
        if self.insert_active_uuid == "":

            obj = create_inventory_object(
                self.insert_asset_type_combobox.currentText(),
                self.insert_manufacturer_combobox.currentText(),
                self.insert_serial_text.text(),
                self.insert_model_text.text(),
                self.insert_cost_spinbox.text(),
                self.insert_assigned_to_text.text(),
                self.insert_name_text.text(),
                self.insert_asset_location_combobox.currentText(),
                self.insert_asset_category_combobox.currentText(),
                self.insert_deployment_date_fmt.text(),
                self.insert_replacement_date_fmt.text(),
                None if self.insert_status_bool.currentText() == "Active" else self.insert_conditional_retirement_date_fmt.text(),
                self.insert_notes_text.toPlainText(),
                self.insert_status_bool.currentText(),
            )
            new_entry(self.connection, obj)
        else:
            # we are updating an existing entry! (since the uuid string was set)
            obj = InventoryObject(
                self.insert_asset_type_combobox.currentText(),
                self.insert_manufacturer_combobox.currentText(),
                self.insert_serial_text.text(),
                self.insert_model_text.text(),
                self.insert_cost_spinbox.text(),
                self.insert_assigned_to_text.text(),
                self.insert_name_text.text(),
                self.insert_asset_location_combobox.currentText(),
                self.insert_asset_category_combobox.currentText(),
                self.insert_deployment_date_fmt.text(),
                self.insert_replacement_date_fmt.text(),
                None if self.insert_status_bool.currentText() == "Active" else self.insert_conditional_retirement_date_fmt.text(),
                self.insert_notes_text.toPlainText(),
                self.insert_status_bool.currentText(),
                self.insert_active_uuid,
            )
            update_full_obj(self.connection, obj)
        self.set_insert_data_to_default()
        # intentional choice here to not update the graphs, seems too expensive to call each time, and to see if data was even changed
        # from the current view.
        self.populate_table_with(
            fetch_all_enabled_for_table(self.connection), False
        )  # this will overwrite any filters / views

    def set_insert_data_to_default(
        self,
    ):  # reset the insert data. Called when clearing page (btn) or inserting / updating
        today = QDate.currentDate()
        # order still persists from pre-revamp. doesnt matter!
        self.insert_serial_text.setText("")
        self.insert_manufacturer_combobox.setCurrentIndex(0)
        self.insert_model_text.setText("")
        self.insert_cost_spinbox.setValue(0.00)
        self.insert_asset_category_combobox.setCurrentIndex(0)  # to the empty string!
        self.insert_asset_type_combobox.setCurrentIndex(0)
        self.insert_asset_location_combobox.setCurrentIndex(0)
        self.insert_assigned_to_text.setText("")
        self.insert_deployment_date_fmt.setDate(today)
        self.insert_replacement_date_fmt.setDate(today)
        self.insert_conditional_retirement_date_fmt.setDate(today)
        self.insert_notes_text.setText("")
        self.insert_status_bool.setCurrentIndex(0)
        self.insert_active_uuid = ""  # reset the uuid, so it doesn't persist
        self.insert_name_text.setText("")
        self.hide_or_show_insert_conditional()  # ig the program won't know when to redraw it?
        # so in theory, if you insert with it visible, 
        # also re-enable all the potentially disabled boxes:
        self.insert_asset_type_combobox.setDisabled(False)
        self.insert_asset_category_combobox.setDisabled(False)
        self.insert_manufacturer_combobox.setDisabled(False)
        self.insert_serial_text.setDisabled(False)
        self.insert_model_text.setDisabled(False)
        self.insert_cost_spinbox.setDisabled(False)
        self.insert_asset_category_combobox.setDisabled(False)
        self.insert_deployment_date_fmt.setDisabled(False)

    def set_table_size_and_headers(self, headers: list[str]):  # only called on startup
        # kept sort of abigious since headers can be changed. if it was always all the headers it could be hardcoded
        headers.append(
            "UUID"
        )  # appended since other parts rely on the headers passed in, and they don't want that
        length = len(headers)
        self.main_table.setColumnCount(length)
        self.main_table.setHorizontalHeaderLabels(headers)
        # set the sizes of certain columns as needed
        for count, column_title in enumerate(headers):
            if column_title == "Asset Category":
                # maybe value should be calculated based off the longest string from the relevant json
                self.main_table.setColumnWidth(count, 150)
            elif column_title == "Replacement Date":
                self.main_table.setColumnWidth(count, 120)
        # alternating row colors :D
        self.main_table.setAlternatingRowColors(True)
        # sets the UUID to be hidden
        self.main_table.setColumnHidden(length - 1, True)  # must be done here

    def filter_all_columns(
        self, word: str
    ):  # filters the columns. doesn't check notes.
        for row_num in range(self.main_table.rowCount()):
            match = False
            for col_num in range(self.main_table.columnCount()):
                cell = self.main_table.item(row_num, col_num)
                if cell is None:
                    continue
                else:
                    cell_content = cell.text()
                    if word in cell_content:
                        match = True
                        break
            if match is False:
                self.main_table.setRowHidden(row_num, True)

    def filter_certain_column(self, word: str, column: int):  # also cannot check notes
        for row_num in range(self.main_table.rowCount()):
            match = False
            for col_num in range(self.main_table.columnCount()):
                if col_num != column:
                    continue
                cell = self.main_table.item(row_num, col_num)
                if word.lower() in cell.text().lower():
                    match = True
                    break  # break is logically implied, but since it would search meaningless columns...
            if match is False:
                self.main_table.setRowHidden(row_num, True)

    def handle_filter_request(self):  # what the filter button calls
        # we don't want to filter already filtered content, so we reset the stuff to default
        for count in range(self.main_table.rowCount()):
            self.main_table.setRowHidden(count, False)
        word = self.filter_user_text.text()
        category = self.filter_options_combobox.currentText()
        if category != "Global":
            column = self.default_columns.index(category)
            self.filter_certain_column(word, column)
        else:
            self.filter_all_columns(word)

    def clear_filter(
        self,
    ):  # clear the text in the filter, and un-hide the columns, called by button
        for count in range(self.main_table.rowCount()):
            self.main_table.setRowHidden(count, False)
        self.filter_user_text.setText("")
        self.filter_options_combobox.setCurrentIndex(0)

    def toggle_retired_assets(self):
        if self.checkbox_view_retired_assets.isChecked():
            self.populate_table_with(fetch_all_for_table(self.connection), True)  # lets view all content
        else:
            self.populate_table_with(fetch_all_enabled_for_table(self.connection), False)  # only enabled content!
            
    def try_retire_row(self, uuid):
        try:
            retire_from_uuid(self.connection, uuid)
            self.toggle_retired_assets()
        except AttributeError as e:
            print("fail!!", e)
            # this is the case where the user.. misses? a row
            pass

    def try_unretire_row(self, uuid):
        try:
            unretire_from_uuid(self.connection, uuid)
            self.toggle_retired_assets()
            # refresh table...?
        except AttributeError:
            pass

    def try_update_row(self, position):
        try:
            self.send_update_data_to_insert(self.main_table.itemAt(position).row())
        except AttributeError:
            # this is the case where the user.. misses? a row
            pass

    def serial_input_typed(self):
        # this is what we call when the serial number field is typed in
        # we do a check to see if that serial number exists in our db.
        # if it does exist, we enable the button & allow the user to import from that serial number
        serial_str = self.insert_serial_text.text()
        da_list = fetch_all_serial(self.connection)
        if serial_str == "":
            self.insert_serial_is_unique_button.setEnabled(False)
            self.insert_serial_is_unique_button.setText("cant import empty SN")
        elif serial_str in da_list:
            self.insert_serial_is_unique_button.setEnabled(True)
            self.insert_serial_is_unique_button.setText("S/N Exists. Click to import")
        else:
            self.insert_serial_is_unique_button.setEnabled(False)
            self.insert_serial_is_unique_button.setText("Unique")

    def pull_unique_uuid_data(self):
        # this happens when the user clicks the button next to "serial #" on the add page when
        # the text inside the serial # lineedit already exists.
        # it invites the user to edit that gives object, based on the serial number identifier
        obj = fetch_by_serial(self.connection, self.insert_serial_text.text())
        self.update_insert_page_from_obj(obj)
        self.swap_to_window(1)

    def create_db_connection(self, invisman_username, ssh_key_location, invisman_server_ip) -> bool | psycopg2.extensions.connection:
        # okay, so we create our ssh tunnel, and our connection through it. we return the connection. I don't see why this won't live long...
        # maybe we can't do this in a function? maybe? idk.
        # ok secondary problem (that will be solved soon i hope) is credentials. i think the best way to do it is to
        # force users to set some credentials in windows cred manager (ssh password. for now)
        # and we can pull them out with keyring
        try:
            invisman_pw = get_password("invisman", invisman_username)
            ssh_pw = get_password("invisman_sshkey", ssh_key_location)
            server = SSHTunnelForwarder((invisman_server_ip, 22), ssh_pkey=ssh_key_location, ssh_username=invisman_username, ssh_private_key_password=ssh_pw, remote_bind_address=("127.0.0.1", 5432))
            server.start()
            print("returning db connection!!")
            return connect(dbname="invisman", user=invisman_username, password=invisman_pw, host="127.0.0.1", port=server.local_bind_port)
        except (AttributeError, PermissionError, BaseSSHTunnelForwarderError): # when the settings are not valid..
            return False
        # ok so user and pw need to both be pulled, not just pw
        # these will live inside of windows credentials manager "invisman". has both username and password
            
    def force_sync(self):
        # this is only called from the thread function.
        print("we are forcing sync!!")
        self.populate_table_with(fetch_all_enabled_for_table(self.connection), False)
