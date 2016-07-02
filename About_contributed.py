#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui,QtCore
from Ui_about_contributed import Ui_About

_IME = "<p>Contributed: <i>Professor Dr. Predrag Pejovi""&#263;<i></p>"
_FAKULTET = "Faculty of Electrical Engineering, University of Belgrade - ETF"
_URL = "<a href = ""http://tnt.etf.rs/~peja>Professor link</a>"

#-------------------------------------------------------------------------------
class AboutWindow3(QtGui.QDialog):
    """ Class wrapper for about window ui """

    def __init__(self):
        super(AboutWindow3,self).__init__()
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_About()
        self.ui.setupUi(self)
        self.ui.lblVersion.setText("{}".format(_IME))
        self.ui.lblVersion2.setText("{}".format(_FAKULTET))
        self.ui.lblURL.setText(_URL)
#-------------------------------------------------------------------------------

def main():
    app = QtGui.QApplication(sys.argv)
    form = AboutWindow3()

    form.show()
    sys.exit(app.exec_())
   
if __name__ == "__main__":
    main()
