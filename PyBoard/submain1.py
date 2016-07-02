# main.py -- put your code here!

import pyb

# Ucitavamo led
crvena = pyb.LED(1)
zelena = pyb.LED(2)
zuta = pyb.LED(3)
plava = pyb.LED(4)

zelena.toggle()                 # Palimo led kao oznaku da se nalazimo u submain1  

serial = pyb.USB_VCP()          # Ucitavamo objekat serijeske komunikacije

accel = pyb.Accel()             # Ucitavamo objekat akcelerometra 

switch = pyb.Switch()           # Ucitavamo objekat tastera

while True:
    data = serial.recv(1)                     # Ocitavamo sta se nalazi na magistrali

    if data == b'\xff':                       # Ako je to sto smo zeleli
        data2 = accel.filtered_xyz()          # Ocitaj tuple vrednosti x,y,z
        print("%s"%(data2,))                  # Posalji


