# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QObject
from PyQt5.QtWidgets import QFileDialog
import middleware_steg


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.inpath = ""
        self.outpath = ""
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 92, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 92, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 231, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 30, 111, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 50, 92, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 190, 241, 361))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 30, 131, 23))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 50, 92, 23))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 110, 131, 23))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 90, 121, 23))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 70, 92, 23))
        self.checkBox_10.setObjectName("checkBox_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(140, 20, 631, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 130, 451, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 141, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 131, 25))
        self.pushButton.setObjectName("pushButton")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 60, 221, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 131, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 30, 451, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 90, 451, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(520, 370, 241, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.inSlot)
        self.pushButton_2.clicked.connect(self.outSlot)     
        self.pushButton_3.clicked.connect(self.runTool)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Media"))
        self.checkBox.setText(_translate("MainWindow", "Video"))
        self.checkBox_2.setText(_translate("MainWindow", "Image"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image Algorithms"))
        self.checkBox_3.setText(_translate("MainWindow", "StegExpose"))
        self.checkBox_4.setText(_translate("MainWindow", "PixelKnot "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Video Algorithms"))
        self.checkBox_6.setText(_translate("MainWindow", "Generalised EOF"))
        self.checkBox_7.setText(_translate("MainWindow", "Openpuff"))
        self.checkBox_8.setText(_translate("MainWindow", "BDV DataHider"))
        self.checkBox_9.setText(_translate("MainWindow", "OmniHide Pro"))
        self.checkBox_10.setText(_translate("MainWindow", "OurSecret"))
        self.groupBox_4.setTitle(_translate("MainWindow", "I/O Directories"))
        self.label_2.setText(_translate("MainWindow", "Custom Prefix"))
        self.pushButton.setText(_translate("MainWindow", "Input Directory"))
        self.checkBox_5.setText(_translate("MainWindow", "Recursive Search for media"))
        self.pushButton_2.setText(_translate("MainWindow", "Output Directory"))
        self.pushButton_3.setText(_translate("MainWindow", "Run Tool"))
        
    @pyqtSlot( )
    def runTool( self ):
        prefix = self.lineEdit_3.text()
        
        self.groupBox_3.toggled.connect(self.onToggled)
        self.groupBox_2.toggled.connect(self.onToggled)
            
        run_tool(inpath,outpath,prefix,v_algo,i_algo)
        
        refreshAll()

    @pyqtSlot( )
    def outSlot( self ):
        ''' Called when the user presses the output dir button
        '''
        path = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.outpath = path
        self.lineEdit_4.setText(path)
        
        refreshAll()

    @pyqtSlot( )
    def inSlot( self ):
        ''' Called when the user presses the input dir button
        '''        
        path = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.inpath = path
        self.lineEdit_5.setText(path)
        
        refreshAll()
    
    def refreshAll( self ):
        '''
        Updates the widgets whenever an interaction happens.
        Typically some interaction takes place, the UI responds,
        and informs the model of the change.  Then this method
        is called, pulling from the model information that is
        updated in the GUI.
        '''
        self.lineEdit.setText( self.model.getFileName() )
        self.textEdit.setText( self.model.getFileContents() )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
