# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\09.python\19.Pyqt5_data_classification\first_stuff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout


##################!@수정한 부분###############################################################################
from PyQt5.QtGui import QPixmap
import os
import NTF_Classification as NTF
import shutil as sh

current_directory = os.getcwd()
sub_directory = os.path.join(current_directory, NTF.created_folder_name)
list = []
files = os.listdir(sub_directory)
for file in files:
    path = os.path.join(sub_directory, file)
    if path.endswith('JPG'):
        list.append(path)
bong2 = list[0]
############################################################################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1534, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.B1_to_OK_folder = QtWidgets.QPushButton(self.centralwidget)
        self.B1_to_OK_folder.setGeometry(QtCore.QRect(60, 710, 681, 121))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B1_to_OK_folder.setFont(font)
        self.B1_to_OK_folder.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.B1_to_OK_folder.setObjectName("B1_to_OK_folder")
        self.B2_to_NG_folder = QtWidgets.QPushButton(self.centralwidget)
        self.B2_to_NG_folder.setGeometry(QtCore.QRect(760, 710, 681, 121))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.B2_to_NG_folder.setFont(font)
        self.B2_to_NG_folder.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.B2_to_NG_folder.setObjectName("B2_to_NG_folder")
        self.To_show_info = QtWidgets.QTextEdit(self.centralwidget)
        self.To_show_info.setGeometry(QtCore.QRect(550, 10, 891, 51))
        self.To_show_info.setObjectName("To_show_info")
        self.B3_to_SUSPEND_folder = QtWidgets.QPushButton(self.centralwidget)
        self.B3_to_SUSPEND_folder.setGeometry(QtCore.QRect(60, 680, 1381, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.B3_to_SUSPEND_folder.setFont(font)
        self.B3_to_SUSPEND_folder.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.B3_to_SUSPEND_folder.setObjectName("B3_to_SUSPEND_folder")
        self.To_show_info_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.To_show_info_2.setGeometry(QtCore.QRect(60, 10, 481, 51))
        self.To_show_info_2.setObjectName("To_show_info_2")

        self.Showing_pic = QtWidgets.QWidget(self.centralwidget)
        self.Showing_pic.setGeometry(QtCore.QRect(60, 70, 1381, 601))
        self.Showing_pic.setObjectName("Showing_pic")

        self.what_the_hell = QtWidgets.QLabel(self.Showing_pic)
        self.what_the_hell.setGeometry(QtCore.QRect(290, 20, 721, 541))
        self.what_the_hell.setObjectName("what_the_hell")

        ##########!@수정한 부분###########################################
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(list[0])
        self.what_the_hell.setPixmap(self.qPixmapFileVar)

        self.B1_to_OK_folder.clicked.connect(self.go_to_OK)
        self.B2_to_NG_folder.clicked.connect(self.go_to_NG)
        self.B3_to_SUSPEND_folder.clicked.connect(self.go_to_suspend)
        ################################################################


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1534, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ##########!@수정한 부분#####################################
    def go_to_OK(self):
        print("ok")
        NTF.createFolder(sub_directory + '\\' +  'OK_folder')
        sh.move(list[0],sub_directory + '\\' +  'OK_folder' + '\\' + os.path.basename(list[0]))
        del list[0]
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(list[0])
        self.what_the_hell.setPixmap(self.qPixmapFileVar)
    def go_to_NG(self):
        print("ng")
        NTF.createFolder(sub_directory + '\\' + 'NG_folder')
        sh.move(list[0], sub_directory + '\\' + 'NG_folder' + '\\' + os.path.basename(list[0]))
        del list[0]
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(list[0])
        self.what_the_hell.setPixmap(self.qPixmapFileVar)
    def go_to_suspend(self):
        print("suspend")
        NTF.createFolder(sub_directory + '\\' + 'SUSPEND_folder')
        sh.move(list[0], sub_directory + '\\' + 'SUSPEND_folder' + '\\' + os.path.basename(list[0]))
        del list[0]
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(list[0])
        self.what_the_hell.setPixmap(self.qPixmapFileVar)
    ###########################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.B1_to_OK_folder.setText(_translate("MainWindow", "OK (left key)"))
        self.B2_to_NG_folder.setText(_translate("MainWindow", "NG(right key)"))
        self.B3_to_SUSPEND_folder.setText(_translate("MainWindow", "SUSPEND(up key)"))
        self.To_show_info_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CLASSIFICATION</p></body></html>"))
        ##########!@수정한 부분#####################################
        # self.what_the_hell.setText(_translate("MainWindow", "TextLabel"))
        ##########################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())









