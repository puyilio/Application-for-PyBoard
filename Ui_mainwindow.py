#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Pravimo glavni prozor.
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(891, 650)
        MainWindow.setMinimumSize(QtCore.QSize(891, 650))
        MainWindow.setMaximumSize(QtCore.QSize(891, 650))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TeX Gyre Schola"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)

        # Postavljamo u glavni prozor widget, tek po postavljanju objekata u njega.
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # Naslov
        self.lbl_1 = QtGui.QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(20, 30, 851, 55))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Linux Biolinum Keyboard O"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_1.setFont(font)

        self.lbl_1.setObjectName(_fromUtf8("lbl_1"))

        # Timer1
        self.lbl_2 = QtGui.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(20, 120, 150, 30))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_2.setFont(font)

        self.lbl_2.setObjectName(_fromUtf8("lbl_2"))

        # Timer2
        self.lbl_3 = QtGui.QLabel(self.centralwidget)
        self.lbl_3.setGeometry(QtCore.QRect(20, 200, 150, 30))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_3.setFont(font)
        
        self.lbl_3.setObjectName(_fromUtf8("lbl_3"))

        # Threshold
        self.lbl_4 = QtGui.QLabel(self.centralwidget)
        self.lbl_4.setGeometry(QtCore.QRect(370, 120, 150, 30))
        self.lbl_4.setObjectName(_fromUtf8("lbl_4"))

        # Set threshold auto
        self.lbl_5 = QtGui.QLabel(self.centralwidget)
        self.lbl_5.setGeometry(QtCore.QRect(340, 170, 150, 30))
        self.lbl_5.setObjectName(_fromUtf8("lbl_5"))

        # Wher to save measure
        self.lbl_6 = QtGui.QLabel(self.centralwidget)
        self.lbl_6.setGeometry(QtCore.QRect(290, 240, 150, 30))
        self.lbl_6.setObjectName(_fromUtf8("lbl_6"))

        # Check if you want to save
        self.lbl_7 = QtGui.QLabel(self.centralwidget)
        self.lbl_7.setGeometry(QtCore.QRect(290, 280, 180, 30))
        self.lbl_7.setObjectName(_fromUtf8("lbl_7"))

        # Set threshold manual
        self.lbl_8 = QtGui.QLabel(self.centralwidget)
        self.lbl_8.setGeometry(QtCore.QRect(600, 95, 150, 30))
        self.lbl_8.setObjectName(_fromUtf8("lbl_8"))

        # Start ploting
        self.lbl_9 = QtGui.QLabel(self.centralwidget)
        self.lbl_9.setEnabled(True)
        self.lbl_9.setGeometry(QtCore.QRect(680, 195, 150, 30))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_9.setFont(font)

        self.lbl_9.setObjectName(_fromUtf8("lbl_9"))

        # Load measure
        self.lbl_10 = QtGui.QLabel(self.centralwidget)
        self.lbl_10.setGeometry(QtCore.QRect(20, 340, 201, 91))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_10.setFont(font)

        self.lbl_10.setObjectName(_fromUtf8("lbl_10"))

        # What file
        self.lbl_11 = QtGui.QLabel(self.centralwidget)
        self.lbl_11.setGeometry(QtCore.QRect(270, 385, 150, 30))
        self.lbl_11.setObjectName(_fromUtf8("lbl_11"))

        # Load data
        self.lbl_12 = QtGui.QLabel(self.centralwidget)
        self.lbl_12.setGeometry(QtCore.QRect(500, 360, 150, 30))
        self.lbl_12.setObjectName(_fromUtf8("lbl_12"))

        # Start plot
        self.lbl_13 = QtGui.QLabel(self.centralwidget)
        self.lbl_13.setGeometry(QtCore.QRect(680, 360, 150, 30))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_13.setFont(font)

        self.lbl_13.setObjectName(_fromUtf8("lbl_13"))

        # Real time measure
        self.lbl_14 = QtGui.QLabel(self.centralwidget)
        self.lbl_14.setGeometry(QtCore.QRect(20, 460, 301, 121))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_14.setFont(font)

        self.lbl_14.setObjectName(_fromUtf8("lbl_14"))

        # X axis measure
        self.lbl_15 = QtGui.QLabel(self.centralwidget)
        self.lbl_15.setGeometry(QtCore.QRect(400, 480, 150, 30))
        self.lbl_15.setObjectName(_fromUtf8("lbl_15"))

        # Y axis measure
        self.lbl_16 = QtGui.QLabel(self.centralwidget)
        self.lbl_16.setGeometry(QtCore.QRect(550, 480, 150, 30))
        self.lbl_16.setObjectName(_fromUtf8("lbl_16"))

        # Y axis measure
        self.lbl_17 = QtGui.QLabel(self.centralwidget)
        self.lbl_17.setGeometry(QtCore.QRect(700, 480, 150, 30))
        self.lbl_17.setObjectName(_fromUtf8("lbl_17"))

        # Set timer for f of plot
        self.lbl_18 = QtGui.QLabel(self.centralwidget)
        self.lbl_18.setGeometry(QtCore.QRect(180, 95, 160, 30))
        self.lbl_18.setObjectName(_fromUtf8("lbl_18"))

        # Set timer for f of values
        self.lbl_19 = QtGui.QLabel(self.centralwidget)
        self.lbl_19.setGeometry(QtCore.QRect(180, 175, 160, 30))
        self.lbl_19.setObjectName(_fromUtf8("lbl_19"))


        #
        self.line_1 = QtGui.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(20, 85, 851, 20))
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))

        #
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 320, 851, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        #
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 440, 851, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))


        # Set timer1
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(180, 120, 150, 30))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))

        # Set timer2
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 200, 150, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        # Set threshold
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 120, 150, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        # Auto
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 170, 110, 30))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        # Ploting
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(680, 220, 151, 91))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        # Load
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 385, 94, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        # Plot
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(680, 385, 151, 51))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))



        # Threshold value
        self.lineEdit_1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(460, 120, 130, 30))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))

        # Save name
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 240, 130, 30))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        # Load name
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 385, 130, 30))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        # X value
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 505, 130, 30))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        # Y value
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(550, 505, 130, 30))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        # Z value
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(700, 505, 130, 30))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))

        # Timer1 value
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 120, 60, 30))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_6"))

        # Timer2 value
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 200, 60, 30))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_6"))


        # Do you want to save
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(530, 280, 59, 26))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))


        MainWindow.setCentralWidget(self.centralwidget)


        # Statusbar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)


        # Menu
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 29))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))

        # File
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setGeometry(QtCore.QRect(1656, 167, 138, 99))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))

        # About
        self.menuAbout = QtGui.QMenu(self.menuFile)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))

        # About se deli na 3 about
	# About_app
        self.actionAbout_app = QtGui.QAction(MainWindow)
        self.actionAbout_app.setObjectName(_fromUtf8("actionAbout_app"))
        self.actionAbout_app.setShortcut('Ctrl+A')
        self.actionAbout_app.setStatusTip('About application')

        # About_author
        self.actionAbout_author = QtGui.QAction(MainWindow)
        self.actionAbout_author.setObjectName(_fromUtf8("actionAbout_author"))
        self.actionAbout_author.setShortcut('Ctrl+B')
        self.actionAbout_author.setStatusTip('About author')

        # About_contributed
        self.actionAbout_contributed = QtGui.QAction(MainWindow)
        self.actionAbout_contributed.setObjectName(_fromUtf8("actionAbout_author"))
        self.actionAbout_contributed.setShortcut('Ctrl+P')
        self.actionAbout_contributed.setStatusTip('About contributed')


        # Exit
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')

        # Postavljamo menu
        self.menuAbout.addAction(self.actionAbout_app)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_author)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_contributed)

        #
        self.menuFile.addAction(self.menuAbout.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        MainWindow.setMenuBar(self.menubar)

	# Definisemo sta stavljamo u toolbar
        # Exit
        self.exitAction = QtGui.QAction(QtGui.QIcon('Exit.png'), 'Exit', MainWindow)
        self.exitAction.setObjectName(_fromUtf8("actionExit"))
        self.exitAction.setShortcut('Ctrl+C')
        self.exitAction.setStatusTip('Exit application')

        # Plot 1
        self.plt1 = QtGui.QAction(QtGui.QIcon('plt1.png'), 'Plot1', MainWindow)
        self.plt1.setObjectName(_fromUtf8("actionPlt1"))
        self.plt1.setShortcut('Ctrl+P+1')
        self.plt1.setStatusTip('Plot1')

        # Plot 2
        self.plt2 = QtGui.QAction(QtGui.QIcon('plt1.png'), 'Plot2', MainWindow)
        self.plt2.setObjectName(_fromUtf8("actionPlt2"))
        self.plt2.setShortcut('Ctrl+P+2')
        self.plt2.setStatusTip('Plot2')

        # Reset
        self.reset = QtGui.QAction(QtGui.QIcon('reboot.png'), 'Reset', MainWindow)
        self.reset.setObjectName(_fromUtf8("actionReset"))
        self.reset.setShortcut('Ctrl+R')
        self.reset.setStatusTip('Reset')

	# Postavljamo toolbar
        # Toolbar
        toolbar_1 = MainWindow.addToolBar('Plot1')
        toolbar_1.addAction(self.plt1)
        toolbar_1.addAction(self.plt2)
        toolbar_1.addAction(self.reset)

        toolbar_2 = MainWindow.addToolBar('Exit')
        toolbar_2.addAction(self.exitAction)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBSM", None))
        
        self.lbl_1.setText(_translate("MainWindow", "PyBoard   and   Serial   communication:    \n     Real   time   accelerometer   measure", None))
        self.lbl_2.setText(_translate("MainWindow", "Timer1: ", None))
        self.lbl_3.setText(_translate("MainWindow", "Timer2: ", None))
        self.lbl_4.setText(_translate("MainWindow", "Threshold:", None))
        self.lbl_5.setText(_translate("MainWindow", "Set threshold auto", None))
        self.lbl_6.setText(_translate("MainWindow", "Wher to save measure:", None))
        self.lbl_7.setText(_translate("MainWindow", "Check if you want to save:", None))
        self.lbl_8.setText(_translate("MainWindow", "Set threshold manual", None))
        self.lbl_9.setText(_translate("MainWindow", "Start ploting", None))
        self.lbl_10.setText(_translate("MainWindow", "Load measure", None))
        self.lbl_11.setText(_translate("MainWindow", "What file:", None))
        self.lbl_12.setText(_translate("MainWindow", "Load data", None))
        self.lbl_13.setText(_translate("MainWindow", "Start plot", None))
        self.lbl_14.setText(_translate("MainWindow", "Real time measure", None))
        self.lbl_15.setText(_translate("MainWindow", "X axis measure", None))
        self.lbl_16.setText(_translate("MainWindow", "Y axis measure", None))
        self.lbl_17.setText(_translate("MainWindow", "Z axis measure", None))
        self.lbl_18.setText(_translate("MainWindow", "Set timer for f of plot ", None))
        self.lbl_19.setText(_translate("MainWindow", "Set timer for f of values", None))

        self.pushButton_1.setText(_translate("MainWindow", "Set", None))
        self.pushButton_2.setText(_translate("MainWindow", "Set", None))
        self.pushButton_3.setText(_translate("MainWindow", "Set", None))
        self.pushButton_4.setText(_translate("MainWindow", "Auto", None))
        self.pushButton_5.setText(_translate("MainWindow", "Plot", None))
        self.pushButton_6.setText(_translate("MainWindow", "Load", None))
        self.pushButton_7.setText(_translate("MainWindow", "Plot", None))

        self.lineEdit_1.setText(_translate("MainWindow", "0.0", None))
        self.lineEdit_2.setText(_translate("MainWindow", "values", None))
        self.lineEdit_3.setText(_translate("MainWindow", "values", None))
        self.lineEdit_4.setText(_translate("MainWindow", "0.0", None))
        self.lineEdit_5.setText(_translate("MainWindow", "0.0", None))
        self.lineEdit_6.setText(_translate("MainWindow", "0.0", None))
        self.lineEdit_7.setText(_translate("MainWindow", "200", None))
        self.lineEdit_8.setText(_translate("MainWindow", "200", None))

        self.checkBox.setText(_translate("MainWindow", "Yes?", None))
        
        # Menu
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionAbout_app.setText(_translate("MainWindow", "About_app", None))
        self.actionAbout_author.setText(_translate("MainWindow", "About_author", None))
        self.actionAbout_contributed.setText(_translate("MainWindow", "About_contributed", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

        # Toolbar
        self.plt1.setText(_translate("MainWindow", "Plot1", None))
        self.plt2.setText(_translate("MainWindow", "Plot2", None))
        self.reset.setText(_translate("MainWindow", "Reset", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))



def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
