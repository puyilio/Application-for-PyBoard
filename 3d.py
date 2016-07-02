# -*- coding: utf-8 -*-
"""
Demonstrate use of GLLinePlotItem to draw cross-sections of a surface.

"""
## Add path to library (just for examples; you do not need this)
#import initExample

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import scipy.ndimage as ndi
from time import *

xyz1 = int(0)
xyz2 = int(0)
xyz3 = int(0)

counter1 = 0
counter2 = 0
counter3 = 0

phase = 0

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 40
w.show()
w.setWindowTitle('pyqtgraph example: GLLinePlotItem')

gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-10, 0, 0)

w.addItem(gx)

gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -10, 0)

w.addItem(gy)

gz = gl.GLGridItem()
gz.translate(0, 0, -10)

w.addItem(gz)

## Manually specified colors
#z = ndi.gaussian_filter(np.random.normal(size=(100,100)), (1,1))
z = np.ones((21, 21))
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

counter1 = int(0)
print counter1

print 'x', x

print 'y', y

print 'z', z
colors = np.ones((100,100,4), dtype=float)
colors[...,0] = np.clip(np.cos(((x.reshape(100,1) ** 2) + (y.reshape(1,100) ** 2)) ** 0.5), 0, 1)
colors[...,1] = colors[...,0]

p3 = gl.GLSurfacePlotItem(z=z, colors=colors.reshape(100*100,4), shader='shaded', smooth=False)
#p3.scale(-1 , 1, 1)
p3.translate(-10, -10, 0)
w.addItem(p3)



def update():
    global p3, z, counter1, counter2, counter3
    print 'update' '\n'

    sleep(0.4)
    
    values1 = np.load('values1.npy')
    values2 = np.load('values2.npy')
    values3 = np.load('values3.npy')
    values4 = np.load('values4.npy')

    values1 = values1[-1:]
    values2 = values2[-1:]
    values3 = values3[-1:]
    values4 = values4[-1:]

    values1 = values1[0]
    values2 = values2[0]
    values3 = values3[0]
    values4 = values4[0]
    print int(values1)
    print int(values2)
    print int(values3)

    
    

    #1
    
    if (int(values1) > 85) & (counter1 == 0) :
        counter1 += 1
        print 'ROTATEEE'
        p3.rotate(90,0,10,0) # po 45 u levo centar y = 10
        
    
    if ((abs(int(values1)) < 15)) & (counter1 == 1):
        print 'ovde 0'
        p3.rotate(-90,0,10,0) # po 45 u desno centar y = 10
        counter1 -= 1
  

    if (int(values1) < -73) & (counter1 == 0):
        counter1 += 1
        p3.rotate(-90,0,10,0) # po 45 u desno centar y = 10

    #2

    if (int(values2) > 75) & (counter2 == 0) :
        counter2 += 1
        print 'ROTATEEE'
        p3.rotate(90,10,0,0) # po 45 u levo centar y = 10
        
    
    if ((abs(int(values2)) < 15)) & (counter2 == 1):
        print 'ovde 0'
        p3.rotate(-90,10,0,0) # po 45 u levo centar y = 10
        counter2 -= 1
        
        
    if (int(values2) < -75) & (counter2 == 0):
        counter2 += 1
        p3.rotate(-90,10,0,0) # po 45 u levo centar y = 10



timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)
print 'startovao'


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

