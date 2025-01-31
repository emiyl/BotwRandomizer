# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomizer_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browseButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton1.setGeometry(QtCore.QRect(640, 10, 150, 24))
        self.browseButton1.setObjectName("browseButton1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 12, 160, 20))
        self.label.setObjectName("label")
        self.baseFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.baseFolder.setEnabled(False)
        self.baseFolder.setGeometry(QtCore.QRect(190, 12, 441, 20))
        self.baseFolder.setObjectName("baseFolder")
        self.browseButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton2.setGeometry(QtCore.QRect(640, 38, 150, 24))
        self.browseButton2.setObjectName("browseButton2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 160, 20))
        self.label_2.setObjectName("label_2")
        self.updateFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.updateFolder.setEnabled(False)
        self.updateFolder.setGeometry(QtCore.QRect(190, 40, 441, 20))
        self.updateFolder.setObjectName("updateFolder")
        self.browseButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton3.setGeometry(QtCore.QRect(640, 68, 150, 24))
        self.browseButton3.setObjectName("browseButton3")
        self.dlcFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.dlcFolder.setEnabled(False)
        self.dlcFolder.setGeometry(QtCore.QRect(190, 70, 441, 20))
        self.dlcFolder.setObjectName("dlcFolder")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 160, 20))
        self.label_3.setObjectName("label_3")
        self.browseButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton4.setGeometry(QtCore.QRect(640, 120, 150, 24))
        self.browseButton4.setObjectName("browseButton4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 122, 160, 20))
        self.label_4.setObjectName("label_4")
        self.graphicPacksFolder = QtWidgets.QLineEdit(self.centralwidget)
        self.graphicPacksFolder.setEnabled(False)
        self.graphicPacksFolder.setGeometry(QtCore.QRect(190, 122, 441, 20))
        self.graphicPacksFolder.setObjectName("graphicPacksFolder")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 781, 51))
        self.pushButton.setObjectName("pushButton")
        self.logBox = QtWidgets.QTextEdit(self.centralwidget)
        self.logBox.setEnabled(False)
        self.logBox.setGeometry(QtCore.QRect(10, 210, 781, 161))
        self.logBox.setObjectName("logBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOTW Randomizer Tool"))
        self.browseButton1.setText(_translate("MainWindow", "Browse..."))
        self.label.setText(_translate("MainWindow", "BOTW Base Content Folder: "))
        self.browseButton2.setText(_translate("MainWindow", "Browse..."))
        self.label_2.setText(_translate("MainWindow", "BOTW Update Content Folder: "))
        self.browseButton3.setText(_translate("MainWindow", "Browse..."))
        self.label_3.setText(_translate("MainWindow", "BOTW DLC Content Folder: "))
        self.browseButton4.setText(_translate("MainWindow", "Browse..."))
        self.label_4.setText(_translate("MainWindow", "Cemu Graphic Packs Folder: "))
        self.pushButton.setText(_translate("MainWindow", "Randomize Game!"))
