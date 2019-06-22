# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QRadioButton
import os
import json
import base64
import middleware_steg

token = ""
usrnm = ""
files = []
usrid = ""
p = ""


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self, placeholderText="Username")
        self.textPass = QtWidgets.QLineEdit(self, placeholderText="Password")
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

        self.b1 = QRadioButton("Public")
        self.b1.toggled.connect(lambda: self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QRadioButton("Agency")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        layout.addWidget(self.b2)

        self.b3 = QRadioButton("Private")
        self.b3.toggled.connect(lambda: self.btnstate(self.b3))
        layout.addWidget(self.b3)

    def btnstate(self, b):
        global p

        if b.text() == "Public":
            if b.isChecked() == True:
                p = 'public'
                #print(p)

        if b.text() == "Agency":
            if b.isChecked() == True:
                p = 'agency'
                #print(p)

        if b.text() == "Private":
            if b.isChecked() == True:
                p = 'private'
                #print(p)

    def handleLogin(self):
        global token
        global usrnm
        global usrid

        usrnm = self.textName.text()
        temp = middleware_steg.authenticate(self.textName.text(), self.textPass.text())
        access_cred = temp.content
        if (temp.status_code == 200):
            access_cred = json.loads(access_cred.decode())
            token = access_cred["access_token"]
            token_split = token.split('.')[1]
            x = json.loads(base64.b64decode(token_split + "=" * ((4 - len(token_split) % 4) % 4)))
            usrid = x['sub']
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Select CSV Files for Upload'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.openFileNameDialog()
        self.openFileNamesDialog()
        # self.saveFileDialog()

        self.show()

    def openFileNamesDialog(self):
        global files
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;CSV Files (*csv)", options=options)
        if files:
            return files


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(560, 250, 161, 51))
        self.checkBox_11.setObjectName("checkBox_11")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 375, 161, 51))
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 450, 161, 51))
        
        self.inpath = os.getcwd() + "/TestMediaRam"
        self.outpath = os.getcwd() + "/Results"

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.inSlot)
        self.pushButton_2.clicked.connect(self.outSlot)     
        self.pushButton_3.clicked.connect(self.runTool)
        self.pushButton_4.clicked.connect(self.uploadFiles)
        self.pushButton_5.clicked.connect(self.deleteFiles)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RAMSES StegAware"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image Algorithms"))
        self.checkBox_3.setText(_translate("MainWindow", "StegExpose"))
        self.checkBox_4.setText(_translate("MainWindow", "PixelKnot "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Video Algorithms"))
        self.checkBox_6.setText(_translate("MainWindow", "Generalised EOF"))
        self.checkBox_7.setText(_translate("MainWindow", "Openpuff"))
        self.checkBox_8.setText(_translate("MainWindow", "BDV DataHider"))
        self.checkBox_9.setText(_translate("MainWindow", "OmniHide Pro"))
        self.checkBox_10.setText(_translate("MainWindow", "OurSecret"))
        self.checkBox_11.setText(_translate("MainWindow", "Push results to RAMSES"))
        self.groupBox_4.setTitle(_translate("MainWindow", "I/O Directories"))
        self.label_2.setText(_translate("MainWindow", "Custom Prefix"))
        self.pushButton.setText(_translate("MainWindow", "Input Directory"))
        self.checkBox_5.setText(_translate("MainWindow", "Recursive Search for media"))
        self.pushButton_2.setText(_translate("MainWindow", "Output Directory"))
        self.pushButton_3.setText(_translate("MainWindow", "Run Tool"))
        self.pushButton_4.setText(_translate("MainWindow", "Upload Existing File"))
        self.pushButton_5.setText(_translate("MainWindow", "Remove Records"))
        self.lineEdit_5.setText(_translate("MainWindow", str(os.getcwd()) + "/TestMediaRam"))
        self.lineEdit_4.setText(_translate("MainWindow", str(os.getcwd()) + "/Results"))

        
    @pyqtSlot( )
    def runTool(self):
        i_algo = []
        v_algo = []
        recurse = False
        prefix = self.lineEdit_3.text()
        global token
        global files
        global p
        global usrid

        if self.checkBox_11.isChecked() == True:
            while p == '' or token == '':
                login_page = Login()
                login_page.exec_()
        
        # check image steg algorithms to be used
        if self.checkBox_3.isChecked() == True:
            i_algo.append("StegExpose")        
        if self.checkBox_4.isChecked() == True:
            i_algo.append("PixelKnot")
            
        # check video steg algorithms to be used
        if self.checkBox_6.isChecked() == True:
            v_algo.append("EOF")
        if self.checkBox_7.isChecked() == True:
            v_algo.append("Openpuff")
        if self.checkBox_8.isChecked() == True:
            v_algo.append("BDV")
        if self.checkBox_9.isChecked() == True:
            v_algo.append("OmniHide")
        if self.checkBox_10.isChecked() == True:
            v_algo.append("OurSecret")

        # check whether recursive search is enabled
        if self.checkBox_5.isChecked() == True:
            recurse = True

        resPath = middleware_steg.run_tool(self.inpath, self.outpath, v_algo, i_algo, recurse)

        if self.checkBox_11.isChecked() == True:
            middleware_steg.pushResults(token, usrid, resPath, p, 'testMalware')
        
        #refreshAll( self )

    @pyqtSlot( )
    def outSlot( self ):
        ''' Called when the user presses the output dir button
        '''
        path = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.outpath = path
        self.lineEdit_4.setText(path)
        
        #refreshAll( self )

    @pyqtSlot( )
    def inSlot( self ):
        ''' Called when the user presses the input dir button
        '''        
        path = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.inpath = path
        self.lineEdit_5.setText(path)
        
        #refreshAll( self )

    def uploadFiles(self):
        global p
        global token
        global usrid

        while p == '' or token == '':
            login_page = Login()
            login_page.exec_()
            App()

            for file in files:
                middleware_steg.pushResults(token, usrid, file, p, 'testMalware_previous')


    def deleteFiles(self):
        itemlist = ['all']
        while True:
            if token != "":
                middleware_steg.deleteRecords(token, usrid, itemlist)
                break
            else:
                login_page = Login()
                login_page.exec_()


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
