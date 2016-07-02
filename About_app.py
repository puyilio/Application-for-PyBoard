#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


from PyQt4 import QtGui,QtCore
from Ui_about_app import Ui_About

_VERSION = "0.0.0"
_URL = "<a href = ""https://github.com/puyilio/Application-for-PyBoard</a>"

#-------------------------------------------------------------------------------
class AboutWindow(QtGui.QDialog):
    """ Class wrapper for about window ui """

    def __init__(self):
        super(AboutWindow,self).__init__()
        #print 'tu'
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_About()
        self.ui.setupUi(self)
        self.ui.lblVersion.setText("PyBSM v{0}".format(_VERSION))
        self.ui.lblURL.setText(_URL)
#-------------------------------------------------------------------------------

def main():
    app = QtGui.QApplication(sys.argv)
    form = AboutWindow()

    form.show()
    sys.exit(app.exec_())
   
if __name__ == "__main__":
    main()
