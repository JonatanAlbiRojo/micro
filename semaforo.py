from machine import Pin
import utime

led_rojo = Pin(32, Pin.OUT)
led_amarillo = Pin(33, Pin.OUT)
led_verde = Pin(25, Pin.OUT)

while True:
    led_rojo.value(1)
    led_amarillo.value(0)
    led_verde.value(0)
    print("Rojo")
    utime.sleep(1)
    
    led_rojo.value(0)
    led_amarillo.value(1)
    led_verde.value(0)
    print("amarillo")
    utime.sleep(0.5)
    
    led_rojo.value(0)
    led_amarillo.value(0)
    led_verde.value(1)
    print("verde")
    utime.sleep(1)
    
    led_rojo.value(0)
    led_amarillo.value(1)
    led_verde.value(0)
    print("amarillo")
    utime.sleep(0.5)
    
    
if __name__==("__main__"):
    main()
    