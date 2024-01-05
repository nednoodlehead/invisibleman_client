# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory_managerRztnyK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 700)
        self.actionInsert = QAction(MainWindow)
        self.actionInsert.setObjectName(u"actionInsert")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionCreate_Backup = QAction(MainWindow)
        self.actionCreate_Backup.setObjectName(u"actionCreate_Backup")
        self.actionClose_ALT_F4 = QAction(MainWindow)
        self.actionClose_ALT_F4.setObjectName(u"actionClose_ALT_F4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ham_menu_button = QPushButton(self.centralwidget)
        self.ham_menu_button.setObjectName(u"ham_menu_button")
        self.ham_menu_button.setGeometry(QRect(0, 0, 80, 50))
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(100, 50, 1160, 550))
        self.ham_button_insert = QPushButton(self.centralwidget)
        self.ham_button_insert.setObjectName(u"ham_button_insert")
        self.ham_button_insert.setGeometry(QRect(0, 47, 75, 50))
        self.ham_button_analytics = QPushButton(self.centralwidget)
        self.ham_button_analytics.setObjectName(u"ham_button_analytics")
        self.ham_button_analytics.setGeometry(QRect(0, 90, 75, 50))
        self.ham_button_analytics_2 = QPushButton(self.centralwidget)
        self.ham_button_analytics_2.setObjectName(u"ham_button_analytics_2")
        self.ham_button_analytics_2.setGeometry(QRect(0, 130, 75, 50))
        self.view_columns_button = QPushButton(self.centralwidget)
        self.view_columns_button.setObjectName(u"view_columns_button")
        self.view_columns_button.setGeometry(QRect(100, 20, 75, 23))
        self.sort_by_button = QPushButton(self.centralwidget)
        self.sort_by_button.setObjectName(u"sort_by_button")
        self.sort_by_button.setGeometry(QRect(290, 20, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1300, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionCreate_Backup)
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionClose_ALT_F4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionInsert.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionCreate_Backup.setText(QCoreApplication.translate("MainWindow", u"Create Backup", None))
        self.actionClose_ALT_F4.setText(QCoreApplication.translate("MainWindow", u"Close                  ALT-F4", None))
        self.ham_menu_button.setText(QCoreApplication.translate("MainWindow", u"ham menu", None))
        self.ham_button_insert.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.ham_button_analytics.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.ham_button_analytics_2.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.view_columns_button.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.sort_by_button.setText(QCoreApplication.translate("MainWindow", u"Sort by...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

