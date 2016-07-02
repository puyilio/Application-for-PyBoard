# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import pyb

# Ucitavamo led
crvena = pyb.LED(1)             
plava = pyb.LED(4)
zuta = pyb.LED(3)


crvena.on()                     # Palimo led kao oznaku da cekamo da neko pritisne taster   
pyb.delay(2000)                 # Dajemo 2 sekunde da neko pritisne
switch_value = pyb.Switch()()   # Ocitavamo da li je pritisnuto
crvena.off()                    # Gasimo led da bi oznacili kraj izbora moda u kome radi

plava.on()                      # Oznaka da selektujemo mod   

if switch_value:
    #crvena.on()
    pyb.usb_mode('CDC+MSC')     # act as a serial and a storage device
    crvena.on()
    pyb.main('submain1.py')     # Skripta koja se izvrsava ako je taster bio pritisnut
else:
    zuta = pyb.LED(3)
    pyb.usb_mode('CDC+HID')     # act as a serial device and a mouse
    pyb.main('submain2.py')     # Skripta koja se izvrsava ako taster nije bio pritisnut

