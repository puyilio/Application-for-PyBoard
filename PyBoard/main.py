# main.py -- put your code here!

import pyb

crvena = pyb.LED(1)
zelena = pyb.LED(2)
zuta = pyb.LED(3)
plava = pyb.LED(4)

plava.toggle()

serial = pyb.USB_VCP()

accel = pyb.Accel()

switch = pyb.Switch()
