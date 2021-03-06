# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 710)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("backgrond-image:url(/newPrefix/dossier sans titre/image/image.jpeg) ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 20, 211, 24))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 80, 291, 31))
        self.label_2.setStyleSheet("border : 1px solid gray")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 110, 151, 51))
        self.lineEdit.setStyleSheet("border : 1px solid gray\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 110, 141, 51))
        self.lineEdit_2.setStyleSheet("border : 1px solid gray\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 180, 291, 31))
        self.label_3.setStyleSheet("border : 1px solid gray")
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 210, 291, 61))
        self.lineEdit_4.setStyleSheet("border : 1px solid gray\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 290, 291, 31))
        self.label_4.setStyleSheet("border : 1px solid gray")
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 320, 291, 61))
        self.lineEdit_6.setStyleSheet("border : 1px solid gray\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(430, 430, 291, 91))
        self.lineEdit_7.setStyleSheet("border : 1px solid gray\n"
"")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 400, 291, 31))
        self.label_5.setStyleSheet("border : 1px solid gray")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(472, 560, 171, 32))
        self.pushButton.setStyleSheet("background : rgb(0, 183, 0);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 30, 391, 611))
        self.label_12.setStyleSheet("background-image: url(:/newPrefix/assets/image/DSz8alfXkAE6sYW.jpeg)")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 190, 91, 31))
        self.label_13.setStyleSheet("color : white;\n"
"font-size : 20px;\n"
"font-weigth: bold;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(80, 240, 171, 61))
        self.label_14.setStyleSheet("color : white;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 340, 91, 31))
        self.label_15.setStyleSheet("color : white;\n"
"font-size : 20px;\n"
"font-weigth: bold;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(80, 380, 171, 41))
        self.label_16.setStyleSheet("color :white;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 460, 161, 31))
        self.label_17.setStyleSheet("color : white;\n"
"font-size : 20px;\n"
"font-weigth: bold;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(100, 520, 171, 41))
        self.label_18.setStyleSheet("color :white;")
        self.label_18.setObjectName("label_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact Form"))
        self.label.setText(_translate("MainWindow", "SEND US A MESSAGE"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Tell us your name *</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "first name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Last name"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Enter your Email *</p></body></html>"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Ex: nan@gmail.com"))
        self.label_4.setText(_translate("MainWindow", "Enter your Number"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Ex: +123456567890"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Write us a message"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Message *</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "SEND MESSAGE"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>Address</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>Mada Center 25 AVenu 15,</p><p>New York, NY 24578 US</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Lets talk</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p>+12446789076</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">General Support</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>contact@gmail.com</p></body></html>"))
import ressource_rc
