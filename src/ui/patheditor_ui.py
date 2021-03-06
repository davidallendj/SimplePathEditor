# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/patheditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 625)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1280))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropOverwriteMode(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_SortDirectories = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_SortDirectories.setObjectName("checkBox_SortDirectories")
        self.horizontalLayout.addWidget(self.checkBox_SortDirectories)
        self.checkBox_RemoveDuplicates = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_RemoveDuplicates.setObjectName("checkBox_RemoveDuplicates")
        self.horizontalLayout.addWidget(self.checkBox_RemoveDuplicates)
        self.pushButton_RemoveDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RemoveDirectory.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_RemoveDirectory.setObjectName("pushButton_RemoveDirectory")
        self.horizontalLayout.addWidget(self.pushButton_RemoveDirectory)
        self.pushButton_AddDirectory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AddDirectory.setMinimumSize(QtCore.QSize(150, 0))
        self.pushButton_AddDirectory.setObjectName("pushButton_AddDirectory")
        self.horizontalLayout.addWidget(self.pushButton_AddDirectory)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_PathOutput = QtWidgets.QLabel(self.centralwidget)
        self.label_PathOutput.setWordWrap(True)
        self.label_PathOutput.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_PathOutput.setObjectName("label_PathOutput")
        self.gridLayout_2.addWidget(self.label_PathOutput, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Path Editor"))
        self.listWidget.setSortingEnabled(False)
        self.checkBox_SortDirectories.setText(_translate("MainWindow", "Sort"))
        self.checkBox_RemoveDuplicates.setText(_translate("MainWindow", "Remove Duplicates"))
        self.pushButton_RemoveDirectory.setText(_translate("MainWindow", "Remove Directory"))
        self.pushButton_AddDirectory.setText(_translate("MainWindow", "Add Directory"))
        self.label.setText(_translate("MainWindow", "Path Entries"))
        self.label_PathOutput.setText(_translate("MainWindow", "PATH="))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
import images_rc
