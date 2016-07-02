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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(400, 80)

        self.verticalLayout = QtGui.QVBoxLayout(About)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.lblVersion = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName(_fromUtf8("lblVersion"))
        self.verticalLayout.addWidget(self.lblVersion)
        
        self.lblURL = QtGui.QLabel(About)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblURL.setFont(font)
        self.lblURL.setAlignment(QtCore.Qt.AlignCenter)
        self.lblURL.setOpenExternalLinks(True)
        self.lblURL.setObjectName(_fromUtf8("lblURL"))
        self.verticalLayout.addWidget(self.lblURL)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About_app", None))
        self.lblVersion.setText(_translate("About", "PyBSM", None))
        self.lblURL.setText(_translate("About", "https://", None))

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_About()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()




