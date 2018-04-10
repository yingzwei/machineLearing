# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QTproject\Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 665)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btn_Start = QtWidgets.QPushButton(self.centralWidget)
        self.btn_Start.setGeometry(QtCore.QRect(160, 90, 61, 23))
        self.btn_Start.setObjectName("btn_Start")
        self.setOpc1 = QtWidgets.QLineEdit(self.centralWidget)
        self.setOpc1.setGeometry(QtCore.QRect(160, 60, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setOpc1.setFont(font)
        self.setOpc1.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.setOpc1.setObjectName("setOpc1")
        self.btn_dalog = QtWidgets.QPushButton(self.centralWidget)
        self.btn_dalog.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.btn_dalog.setObjectName("btn_dalog")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 71, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_Opc1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_Opc1.setFont(font)
        self.lab_Opc1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lab_Opc1.setStyleSheet("border-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 143);\n"
"color: rgb(85, 170, 255);")
        self.lab_Opc1.setObjectName("lab_Opc1")
        self.verticalLayout.addWidget(self.lab_Opc1)
        self.lab_Opc2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_Opc2.setFont(font)
        self.lab_Opc2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lab_Opc2.setStyleSheet("border-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 143);\n"
"color: rgb(85, 170, 255);")
        self.lab_Opc2.setObjectName("lab_Opc2")
        self.verticalLayout.addWidget(self.lab_Opc2)
        self.lab_Opc3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_Opc3.setFont(font)
        self.lab_Opc3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lab_Opc3.setStyleSheet("border-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 143);\n"
"color: rgb(85, 170, 255);")
        self.lab_Opc3.setObjectName("lab_Opc3")
        self.verticalLayout.addWidget(self.lab_Opc3)
        self.lab_Opc4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_Opc4.setFont(font)
        self.lab_Opc4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lab_Opc4.setStyleSheet("border-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 143);\n"
"color: rgb(85, 170, 255);")
        self.lab_Opc4.setObjectName("lab_Opc4")
        self.verticalLayout.addWidget(self.lab_Opc4)
        self.lab_Opc5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lab_Opc5.setFont(font)
        self.lab_Opc5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lab_Opc5.setStyleSheet("border-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 143);\n"
"color: rgb(85, 170, 255);")
        self.lab_Opc5.setObjectName("lab_Opc5")
        self.verticalLayout.addWidget(self.lab_Opc5)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Start.setText(_translate("MainWindow", "启   动"))
        self.setOpc1.setText(_translate("MainWindow", "0.00"))
        self.btn_dalog.setText(_translate("MainWindow", "输入对话框"))
        self.lab_Opc1.setText(_translate("MainWindow", "0.00"))
        self.lab_Opc2.setText(_translate("MainWindow", "0.00"))
        self.lab_Opc3.setText(_translate("MainWindow", "0.00"))
        self.lab_Opc4.setText(_translate("MainWindow", "0.00"))
        self.lab_Opc5.setText(_translate("MainWindow", "0.00"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

