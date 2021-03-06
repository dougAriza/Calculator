# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from email import message
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    #FUNCTIONS
    def ckeckFields(self):
        self.label.hide()
        company:str
        product:str
        startCycle:int
        finalCycle:int
        message = ""
        tablets:int
        fails:int
        flagMessage = False

        company = self.company_lineEdit.text()
        product = self.product_lineEdit.text()

        if company == "":
                message = "Company is empty!"
                flagMessage = True
        if product == "":
                message += " Product is empty!\n"
                flagMessage = True
        if self.startCycle_lineEdit.text() == "":
                message += " Start cycle is empty!"
                flagMessage = True
        else:
                try:
                        startCycle = int(self.startCycle_lineEdit.text())
                except:
                        message += " Start cycle is not a number!"
                        self.startCycle_lineEdit.setText("")
                        flagMessage = True
        if self.finalCycle_lineEdit.text() == "":
                message += " Final cycle is empty!"
                flagMessage = True
        else:
                try:
                        finalCycle = int(self.finalCycle_lineEdit.text())
                        if finalCycle < startCycle:
                                flagMessage = True
                                message += "Final cycle is smaller than start cycle!"
                except:
                        message += " Final cycle is not a number!"
                        self.finalCycle_lineEdit.setText("")
                        flagMessage = True
        if self.tablets_lineEdit.text() == "":
                message += " Tablets is empty!"
                flagMessage = True
        else:
                try:
                        tablets = int(self.tablets_lineEdit.text())
                except:
                        message += "\nTablets is not a number!"
                        self.tablets_lineEdit.setText("")
                        flagMessage = True
        if self.fails_lineEdit.text() == "":
                message += " Fails is empty!"
                flagMessage = True
        else:
                try:
                        fails = int(self.fails_lineEdit.text())
                except:
                        message += " Fails is not a number!"
                        self.fails_lineEdit.setText("")
                        flagMessage = True
                
        if flagMessage:
                self.label.show()
                self.label.setText(message)
                self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
        else:
                result = float((finalCycle - startCycle) * tablets - fails) / ((finalCycle - startCycle) * tablets) * 100
                message = "The " + product + " got " + str(result) + "% of efficience!"
                self.label.setStyleSheet("background-color: rgb(0, 128, 0);")
                self.label.show()
                self.label.setText(message)
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 465)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color: rgb(180, 180, 180);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content.setStyleSheet(";background-color: rgb(15, 15, 15); ")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setLineWidth(0)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info_frame = QtWidgets.QFrame(self.content)
        self.info_frame.setMaximumSize(QtCore.QSize(350, 350))
        self.info_frame.setStyleSheet("background-color: rgb(15, 15, 15); ")
        self.info_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setLineWidth(0)
        self.info_frame.setObjectName("info_frame")
        self.startCycle_lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.startCycle_lineEdit.setGeometry(QtCore.QRect(75, 98, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.startCycle_lineEdit.setFont(font)
        self.startCycle_lineEdit.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);    \n"
        "    border: 2px solid rgb(45, 45, 45);\n"
        "    padding-left: 15px;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    background-color: rgb(35, 35, 35);    \n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    background-color: rgb(45, 45, 45);    \n"
        "    border: 2px solid rgb(255, 241, 32);\n"
        "}")
        self.startCycle_lineEdit.setObjectName("startCycle_lineEdit")
        self.finalCycle_lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.finalCycle_lineEdit.setGeometry(QtCore.QRect(75, 140, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.finalCycle_lineEdit.setFont(font)
        self.finalCycle_lineEdit.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);    \n"
        "    border: 2px solid rgb(45, 45, 45);\n"
        "    padding-left: 15px;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    background-color: rgb(35, 35, 35);    \n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    background-color: rgb(45, 45, 45);    \n"
        "    border: 2px solid rgb(255, 241, 32);\n"
        "}")
        self.finalCycle_lineEdit.setObjectName("finalCycle_lineEdit")

        ##############################################################
        self.tablets_lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.tablets_lineEdit.setGeometry(QtCore.QRect(75, 182, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.tablets_lineEdit.setFont(font)
        self.tablets_lineEdit.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);    \n"
        "    border: 2px solid rgb(45, 45, 45);\n"
        "    padding-left: 15px;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    background-color: rgb(35, 35, 35);    \n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    background-color: rgb(45, 45, 45);    \n"
        "    border: 2px solid rgb(255, 241, 32);\n"
        "}")
        self.tablets_lineEdit.setObjectName("tablets_lineEdit")

        ##############################################################

        ##############################################################
        self.fails_lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.fails_lineEdit.setGeometry(QtCore.QRect(75, 224, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.fails_lineEdit.setFont(font)
        self.fails_lineEdit.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);    \n"
        "    border: 2px solid rgb(45, 45, 45);\n"
        "    padding-left: 15px;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    background-color: rgb(35, 35, 35);    \n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    background-color: rgb(45, 45, 45);    \n"
        "    border: 2px solid rgb(255, 241, 32);\n"
        "}")
        self.fails_lineEdit.setObjectName("fails_lineEdit")

        ##############################################################

        self.company_lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.company_lineEdit.setGeometry(QtCore.QRect(75, 14, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.company_lineEdit.setFont(font)
        self.company_lineEdit.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);    \n"
        "    border: 2px solid rgb(45, 45, 45);\n"
        "    padding-left: 15px;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    background-color: rgb(35, 35, 35);    \n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    background-color: rgb(45, 45, 45);    \n"
        "    border: 2px solid rgb(255, 241, 32);\n"
        "}")
        self.company_lineEdit.setObjectName("company_lineEdit")
        self.product_lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.product_lineEdit.setGeometry(QtCore.QRect(75, 56, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.product_lineEdit.setFont(font)
        self.product_lineEdit.setStyleSheet("QLineEdit {\n"
        "    background-color: rgb(30, 30, 30);    \n"
        "    border: 2px solid rgb(45, 45, 45);\n"
        "    padding-left: 15px;\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QLineEdit:hover {\n"
        "    background-color: rgb(35, 35, 35);    \n"
        "    border: 2px solid rgb(60, 60, 60);\n"
        "}\n"
        "QLineEdit:focus {\n"
        "    background-color: rgb(45, 45, 45);    \n"
        "    border: 2px solid rgb(255, 241, 32);\n"
        "}")
        self.product_lineEdit.setObjectName("product_lineEdit")
        self.calcule_pushButton = QtWidgets.QPushButton(self.info_frame)
        self.calcule_pushButton.setGeometry(QtCore.QRect(120, 280, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.calcule_pushButton.setFont(font)
        self.calcule_pushButton.setStyleSheet("QPushButton {\n"
        "    background-color: rgb(130, 130, 130);\n"
        "    border: 1px solid rgb(95, 95, 95);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(140, 140, 140);\n"
        "    border: 1px solid rgb(115, 115, 115);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: rgb(255, 241, 32);\n"
        "    \n"
        "    color: rgb(255, 0, 0);\n"
        "    border: 1px solid rgb(120, 120, 120);\n"
        "}\n"
        "")
        self.calcule_pushButton.setObjectName("calcule_pushButton")
        self.horizontalLayout.addWidget(self.info_frame)
        self.verticalLayout.addWidget(self.content)
        self.result_frame = QtWidgets.QFrame(self.centralwidget)
        self.result_frame.setMaximumSize(QtCore.QSize(16777215, 85))
        self.result_frame.setStyleSheet("background-color: rgb(15, 15, 15); ")
        self.result_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setLineWidth(0)
        self.result_frame.setObjectName("result_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.result_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.result_frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
        "border-radius: 5px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.result_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #INITIAL SETTINGS
        self.company_lineEdit.setFocus()
        self.label.hide()

        #BUTTONS
        self.calcule_pushButton.clicked.connect(lambda: self.ckeckFields())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startCycle_lineEdit.setPlaceholderText(_translate("MainWindow", "START CYCLE"))
        self.finalCycle_lineEdit.setPlaceholderText(_translate("MainWindow", "FINAL CYCLE"))
        self.tablets_lineEdit.setPlaceholderText(_translate("MainWindow", "TABLETS PER STEP"))
        self.fails_lineEdit.setPlaceholderText(_translate("MainWindow", "FAILS"))
        self.company_lineEdit.setPlaceholderText(_translate("MainWindow", "COMPANY"))
        self.product_lineEdit.setPlaceholderText(_translate("MainWindow", "PRODUCT"))
        self.calcule_pushButton.setText(_translate("MainWindow", "Calcule"))
        self.label.setText(_translate("MainWindow", "Result"))

    def showPage(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
