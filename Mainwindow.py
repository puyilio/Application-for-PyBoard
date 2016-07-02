#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import time
from time import *

import threading
from threading import *

from pylab import *

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import Ui_mainwindow

from About_app import AboutWindow
from About_author import AboutWindow2
from About_contributed import AboutWindow3

da_li_cita = 0


# StoppableThread is from user Dolphin, from http://stackoverflow.com/questions/5849484/how-to-exit-a-multithreaded-program
class StoppableThread(Thread):  

    def __init__(self):
        Thread.__init__(self)
        self.stop_event = Event()        

    def stop(self):
        if self.isAlive() == True:
            # set event to signal thread to terminate
            self.stop_event.set()
            # block calling thread until thread really has terminated
            self.join()

class IntervalTimer(StoppableThread):

    def __init__(self, interval, worker_func):
        super(IntervalTimer, self).__init__()
        self._interval = interval
        self._worker_func = worker_func

    def run(self):
        while not self.stop_event.is_set():
            self._worker_func()
            sleep(self._interval)

            

class MainWindow(QMainWindow, Ui_mainwindow.Ui_MainWindow):
    filename = 'Data.txt'
    threshold = 0
    timer1 = 200
    timer2 = 200
    dosave = 0
    savep = 'values'
    loadp = 'values'
    i = 0

    values1 = ['0']
    values2 = ['0']
    values3 = ['0']

    counter = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # About_app
        self._about_app_dlg = AboutWindow()

        # About_author
        self._about_author_dlg = AboutWindow2()

        # About_author
        self._about_contributed_dlg = AboutWindow3()


    def print_hw (self):
        global da_li_cita
        
        if da_li_cita == 1:
            try:
                self.values1 = load('{}1.npy'.format(self.loadp))
            except IOError:
                pass
            try:
                self.values2 = load('{}2.npy'.format(self.loadp))
            except IOError:
                pass
            try:
                self.values3 = load('{}3.npy'.format(self.loadp))
            except IOError:
                pass
            try:
                self.values4 = load('{}4.npy'.format(self.loadp))
            except IOError:
                pass
            try:
                self.values1 = self.values1[-1:]
                
            except UnboundLocalError:
                pass
            try:
                self.values2 = self.values2[-1:]
                
            except UnboundLocalError:
                pass
            try:
                self.values3 = self.values3[-1:]
            except UnboundLocalError:
                pass
            try:
                self.values4 = self.values4[-1:]
            except UnboundLocalError:
                pass

            self.values1 = self.values1[0]
            self.values2 = self.values2[0]
            self.values3 = self.values3[0]
            self.values4 = self.values4[0]

            if (self.counter == 1):
                self.lineEdit_1.setText(self.values4)
                self.lineEdit_4.setText(self.values1)
                self.lineEdit_5.setText(self.values2)
                self.lineEdit_6.setText(self.values3)
                pass


    def processData(self):

        self.counter += 1 
        self.i = 0
        target = open(self.filename, 'w')
        target.write("%f %i %i %i %s" %(self.threshold, self.timer1, self.timer2, self.dosave, self.savep))
        target.close()

        self.threshold = float(self.lineEdit_1.text())

        self.workerThread = WorkerThread()
        self.connect(self.workerThread, SIGNAL("threadDone(QString, QString)"), self.threadDone, Qt.DirectConnection)
        self.workerThread.start()

        sleep(1)
       
        self.interval =  IntervalTimer((self.timer1/1000.0), self.print_hw)
        self.interval.start()

        #QMessageBox.information(self, "Done!", "Done.")

    def threadDone(self, text, text2):

        da_li_cita = 0

        self.interval.stop()

        self.lineEdit_1.setText(self.values4)
        
        self.lineEdit_4.setText("finished processing.")

        self.lineEdit_5.setText("finished processing.")

        self.lineEdit_6.setText("finished processing.")

        self.remove()


    def restart(self):
        sleep(1)
        self.close()
        subprocess.call(["sudo", "python", "Mainwindow.py"])
        

    def save(self):
        self.dosave = 1
        self.savep = self.lineEdit_2.text()
        print 'cuvamo', self.dosave
        print 'gde', self.savep
        

    def load(self):
        self.loadp = self.lineEdit_3.text()
        print self.loadp


    def t1(self):
        self.timer1 = int(self.lineEdit_7.text())
        print self.timer1

    def t2(self):
        self.timer2 = int(self.lineEdit_8.text())
        print self.timer2
        

    def plot(self):
        print 'plot'
        
        values1 = load('{}1.npy'.format(self.loadp))
        values2 = load('{}2.npy'.format(self.loadp))
        values3 = load('{}3.npy'.format(self.loadp))
        values4 = load('{}4.npy'.format(self.loadp))
        
        print 'ovo je values 1', values1
        print len(values1)
        print 'ovo je values 2', values2
        print len(values2)
        print 'ovo je values 3', values3
        print len(values3)
        close('all')
        figure(1)
        plot(values1, linewidth = 2, color = 'r', label = 'x-axis')
        plot(values2, linewidth = 2, color = 'g', label = 'y-axis')
        plot(values3, linewidth = 2, color = 'b', label = 'z-axis')
        plot(values4, linewidth = 1, color = 'k', label = 'threshold')
        legend(loc = 'lower left')
        show()


    def uradi(self):
        print 'mora neko da uradi'
        self.dosave = 1


    def remove(self):

        if self.dosave == 0:
            os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/Data.txt')
            os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/{}1.npy'.format(self.savep))
            os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/{}2.npy'.format(self.savep))
            os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/{}3.npy'.format(self.savep))
            os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/{}4.npy'.format(self.savep))


    def close_application(self):

        try:
            os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/Ui_mainwindow.pyc')
        except OSError:
            pass
        try:
            os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/Mainwindow.pyc')
        except OSError:
            pass

        os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/Ui_about_app.pyc')
        os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/About_app.pyc')

        os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/Ui_about_author.pyc')
        os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/About_author.pyc')

        os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/Ui_about_contributed.pyc')
        os.remove('/home/bojan3/Desktop/Bojan_Ilic_2010_431/About_contributed.pyc')

        sys.exit()

    def set_threshold(self):
        self.threshold = float(self.lineEdit_1.text())
        print self.threshold

class WorkerThread(QThread):

    def __init__(self):
        super(WorkerThread, self).__init__()

    def run(self):
        global da_li_cita

        da_li_cita = 1
        
        subprocess.call(["sudo", "python", "ploting.py"])
        
        self.emit(SIGNAL("threadDone(QString, QString)"), "Confirmation that the thread is finished.", "Another confirmation that the thread has been completed.")


def main():
    
               
    app = QtGui.QApplication(sys.argv)
    
    form = MainWindow()

    # Push button
    form.pushButton_1.clicked.connect(form.t1)
    form.pushButton_2.clicked.connect(form.t2)
    form.pushButton_3.clicked.connect(form.set_threshold)
    form.pushButton_4.clicked.connect(form.uradi)
    form.pushButton_5.clicked.connect(form.processData)
    form.pushButton_6.clicked.connect(form.load)
    form.pushButton_7.clicked.connect(form.plot)

    # Checkbox
    form.checkBox.clicked.connect(form.save)

    form.actionAbout_app.triggered.connect(form._about_app_dlg.show)
    form.actionAbout_author.triggered.connect(form._about_author_dlg.show)
    form.actionAbout_contributed.triggered.connect(form._about_contributed_dlg.show)
    form.actionExit.triggered.connect(form.close_application)

    # Toolbar
    form.plt1.triggered.connect(form.processData)
    form.plt2.triggered.connect(form.plot)
    form.reset.triggered.connect(form.restart)
    form.exitAction.triggered.connect(form.close)
    
    form.show()
    sys.exit(app.exec_())
   
if __name__ == "__main__":
    main()
    
    



