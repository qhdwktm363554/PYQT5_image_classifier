# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\09.python\19.Pyqt5_data_classification\second_stuff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        font.setPointSize(20)
        self.B1_to_OK_folder.setFont(font)
        self.B1_to_OK_folder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B1_to_OK_folder.setObjectName("B1_to_OK_folder")
        self.B2_to_NG_folder = QtWidgets.QPushButton(self.centralwidget)
        self.B2_to_NG_folder.setGeometry(QtCore.QRect(760, 710, 681, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B2_to_NG_folder.setFont(font)
        self.B2_to_NG_folder.setStyleSheet("background-color: rgb(198, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.B2_to_NG_folder.setObjectName("B2_to_NG_folder")
        self.B3_to_SUSPEND_folder = QtWidgets.QPushButton(self.centralwidget)
        self.B3_to_SUSPEND_folder.setGeometry(QtCore.QRect(60, 680, 1381, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.B3_to_SUSPEND_folder.setFont(font)
        self.B3_to_SUSPEND_folder.setStyleSheet("background-color: rgb(255, 216, 211);\n"
"color: rgb(0, 0, 0);")
        self.B3_to_SUSPEND_folder.setObjectName("B3_to_SUSPEND_folder")
        self.Showing_pic = QtWidgets.QWidget(self.centralwidget)
        self.Showing_pic.setGeometry(QtCore.QRect(60, 70, 1381, 601))
        self.Showing_pic.setStyleSheet("background-color: rgb(94, 94, 94);\n"
"\n"
"border-color: rgb(68, 68, 68);")
        self.Showing_pic.setObjectName("Showing_pic")
        self.what_the_hell = QtWidgets.QLabel(self.Showing_pic)
        self.what_the_hell.setGeometry(QtCore.QRect(290, 20, 721, 541))
        self.what_the_hell.setAlignment(QtCore.Qt.AlignCenter)
        self.what_the_hell.setObjectName("what_the_hell")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 0, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 30pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(990, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

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

        ##########!@수정한 부분###########################################
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(list[0])
        self.what_the_hell.setPixmap(self.qPixmapFileVar)

        self.B1_to_OK_folder.clicked.connect(self.go_to_OK)
        self.B2_to_NG_folder.clicked.connect(self.go_to_NG)
        self.B3_to_SUSPEND_folder.clicked.connect(self.go_to_suspend)
        ################################################################

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
        MainWindow.setWindowTitle(_translate("MainWindow", "ImageClassifier_V0 / BH Kim"))
        self.B1_to_OK_folder.setText(_translate("MainWindow", "OK (left key)"))
        self.B2_to_NG_folder.setText(_translate("MainWindow", "NG (right key)"))
        self.B3_to_SUSPEND_folder.setText(_translate("MainWindow", "SUSPEND (up key)"))
        self.what_the_hell.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "IMAGE CLASSIFIER"))
        self.label_2.setText(_translate("MainWindow", "information: to be updated"))

# import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

