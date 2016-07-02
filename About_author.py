#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui,QtCore
from Ui_about_author import Ui_About



_IME = "<p>Author: Bojan Ili""&#263;</p>"
_FAKULTET = "Faculty of Electrical Engineering, University of Belgrade - ETF"
_MAIL = "https.rs@gmail.com"
_URL = "<a href = ""https://www.facebook.com/puzicius>Facebook link</a>"

#-------------------------------------------------------------------------------
class AboutWindow2(QtGui.QDialog):
    """ Class wrapper for about window ui """

    def __init__(self):
        super(AboutWindow2,self).__init__()
        self.setupUI()
        #print sys.stdout.encoding


    def setupUI(self):
        #create window from ui
        self.ui=Ui_About()
        self.ui.setupUi(self)
        self.ui.lblVersion.setText("{}".format(_IME))
        self.ui.lblVersion2.setText("{}".format(_FAKULTET))
        self.ui.lblVersion3.setText("E-mail: {}".format(_MAIL))
        self.ui.lblURL.setText(_URL)
#-------------------------------------------------------------------------------

def main():
    app = QtGui.QApplication(sys.argv)
    form = AboutWindow2()

    form.show()
    sys.exit(app.exec_())
   
if __name__ == "__main__":
    main()
