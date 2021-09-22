from machine import Pin
import utime
import _thread


uno = Pin(2, Pin.OUT)
dos = Pin(4, Pin.OUT)
tres = Pin(14, Pin.OUT)
cuatro = Pin(27, Pin.OUT)

def nucleo_dos():
    
    while True:
        dos.value(1)
        utime.sleep(0.05)
        dos.value(0)
        utime.sleep(0.05)

_thread.start_new_thread(nucleo_dos, () )

def nucleo_tres():
    
    while True:
        tres.value(1)
        utime.sleep(0.2)
        tres.value(0)
        utime.sleep(0.2)

_thread.start_new_thread(nucleo_tres, () )

def nucleo_cuatro():
    
    while True:
        cuatro.value(1)
        utime.sleep(0.2)
        cuatro.value(0)
        utime.sleep(0.2)

_thread.start_new_thread(nucleo_cuatro, () )

while True:
    uno.value(1)
    utime.sleep(0.4)
    uno.value(0)
    utime.sleep(0.4)    
     
if __name__==("__main__"):
    main()
