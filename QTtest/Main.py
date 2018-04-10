# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_Main import Ui_MainWindow
from PyQt5 import QtWidgets
import OpenOPC
import time
arrayGetOpc = []
arraySetOpc = []

remotehost='10.104.6.89'
opcserver='PCS7.OPCDAServer'
tagList=['OS_Server1::P5702aAR1/P5702aAR1.MV','OS_Server1::P57PF01/P57PF01.MV','OS_Server1::S5702aAR1/S5702aAR1.MV','OS_Server1::C5704AR/C5704AR.MV','OS_Server1::T5701T01/T5701T01.MV']
sampletime = 2



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.graphicsView.mousePressEvent = self.myEventTest
        self.initLabel()
    
    
    def myEventTest(self, e):
        print('---------->')
        
    def initLabel(self):
        for i in range(1, 6):
            strName = 'lab_Opc'+ str(i)
            lab1 = self.findChild(QLabel,strName)
            arrayGetOpc.append(lab1)
        for i in range(1, 5):
            strName = 'setOpc'+ str(i)
            
    @pyqtSlot()
    def on_btn_Start_clicked(self):
        #print(arrayGetOpc[1].text())
        while  1>0:
            opc=OpenOPC.client
            opc.connect('Matrikon.OPC.Simulation', 'localhost')
            (opcvalue,opcstat,opctime) = opc.read(tagList[0])
            arrayGetOpc[1].setText(opcvalue)
            opc.close()
            time.sleep(sampletime)
        
    
    @pyqtSlot()
    def on_btn_dalog_clicked(self):
        #input_value, sta = QInputDialog.getText(self, '输入一个字符串', '在此输入', QLineEdit.Normal, '请输入！')
        input_value, sta = QInputDialog.getInt(self, '输入一个字符串', '在此输入',23, 0, 50)
        #QMessageBox.information(self, '信息提示','保存成功！')
        #QMessageBox.question(self, '信息提示','确定保存？',QMessageBox.Yes | QMessageBox.No)
        print(input_value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

