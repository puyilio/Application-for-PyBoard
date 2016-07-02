#!/usr/bin/python
# -*- coding: utf-8 -*-

import pylab
from pylab import *
import sys

import serial




s = serial.Serial('/dev/ttyACM0', timeout = 3)

filename = "Data.txt"
target = open(filename, 'r')
zez = target.read()
zez = zez.split()
print zez[0]
print zez[1]
print zez[2]
print zez[3]
print zez[4]

xAchse = arange(0, 100, 1)
yAchse = array([0] * 100)

fig = figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Plot")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0, 100, -100, 100])
line1 = ax.plot(xAchse, yAchse, '-')
line2 = ax.plot(xAchse, yAchse, '-')
line3 = ax.plot(xAchse, yAchse, '-')
line4 = ax.plot(xAchse, yAchse, '-')
setp(line1, linewidth = 2, color = 'r', label = 'x-axis')
setp(line2, linewidth = 2, color = 'g', label = 'y-axis')
setp(line3, linewidth = 2, color = 'b', label = 'z-axis')
setp(line4, linewidth = 1, color = 'k', label = 'threshold')
legend(loc = 'lower left')
manager = get_current_fig_manager()

timer1 = fig.canvas.new_timer(interval = zez[1])
timer2 = fig.canvas.new_timer(interval = zez[2])

values1 = []
values2 = []
values3 = []
values4 = []
values1 = [ 0 for x in  range(100)]
values2 = [ 0 for x in  range(100)]
values3 = [ 0 for x in  range(100)]
values4 = [ 0 for x in  range(100)]

threshold = zez[0]
 
def LiveGraph(arg):
    #print 'in LiveGraph'
    global values1, threshold, values2, values3
 
    xaxis = arange(len(values1) - 100, len(values1), 1)

    line1[0].set_data(xaxis, array(values1[-100:]))
    line2[0].set_data(xaxis, array(values2[-100:]))
    line3[0].set_data(xaxis, array(values3[-100:]))
    line4[0].set_data(xaxis, threshold)

    ax.axis([xaxis.min(), xaxis.max(), -100, 100])

    manager.canvas.draw()



def SinwaveformGenerator(arg):
    #print 'in SinwaveformGenerator'
    global values1, values2, values3, values4, threshold
    
    s.write('\xff')
    
    x = s.readline()
    x = x.replace('\r\n','')
    x = x.replace('(','')
    x = x.replace(')','')
    x = x.split(',')
    
    values1.append(x[0])
    values2.append(x[1])
    values3.append(x[2])
    
    if zez[3] == '1' :
        threshold = max(values1)

    values4.append(threshold)
    save(zez[4] + '1.npy', values1)
    save(zez[4] + '2.npy', values2)
    save(zez[4] + '3.npy', values3)
    save(zez[4] + '4.npy', values4)
    print x[0]
    print x[1]
    print x[2]
    
    
def graphstart():
    #print 'in graphstart'
    global timer1, timer2
    timer1.add_callback(LiveGraph, ())
    timer2.add_callback(SinwaveformGenerator, ())
    timer1.start()
    timer2.start()
    plt.show()
    #plt.pause(0.1)



def main():
    graphstart()
        
if __name__ == "__main__":
    main()
    



