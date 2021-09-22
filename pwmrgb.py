from machine import Pin, PWM
from time import sleep

led_r = PWM(Pin(13), freq=10000)
led_g = PWM(Pin(12), freq=10000)
led_b = PWM(Pin(14), freq=10000)

while True:
    
    factor = (65530/255)
    led_r.duty(int (factor* 255))
    led_g.duty(int (factor* 0))
    led_b.duty(int (factor* 0))
    sleep(4)
    led_r.duty(int (factor* 0))
    led_g.duty(int (factor* 255))
    led_b.duty(int (factor* 0))
    sleep(4)
    led_r.duty(int (factor* 0))
    led_g.duty(int (factor* 0))
    led_b.duty(int (factor* 255))
    sleep(4)
    
    
    
      
