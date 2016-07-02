# main.py -- put your code here!

import pyb

# Ucitavamo led
crvena = pyb.LED(1)
zelena = pyb.LED(2)
zuta = pyb.LED(3)
plava = pyb.LED(4)

zuta.toggle()                   # Palimo led kao oznaku da se nalazimo u submain2 
zelena.toggle()

serial = pyb.USB_VCP()          # Ucitavamo objekat serijeske komunikacije

accel = pyb.Accel()             # Ucitavamo objekat akcelerometra 

switch = pyb.Switch()           # Ucitavamo objekat tastera

while True:
    x = accel.x()        # Ocitaj vrednosti x
    y = accel.y()        # Ocitaj vrednosti y
    y = y
    plava.intensity(x*2) # u zavisnosti od x ose setujemo intenzitet led diode
    if (y < 20):
	zelena.on()      # u zavisnosti od y ose palimo led
    if (y > 20):
	zelena.off()     # u zavisnosti od y ose gasimo led


