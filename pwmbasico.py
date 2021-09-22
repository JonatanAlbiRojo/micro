from machine import Pin, PWM
from time import sleep


led = PWM(Pin(4), freq=50)  

while True:
    for duty_cycle in range(0, 65535):
        led.duty(duty_cycle)
        sleep(0.5)