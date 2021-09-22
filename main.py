from machine import Pin,
import time
led_25 = Pin(25,Pin.OUT)
while True:
        led_25.value(1)
        time.sleep(0.5)
        led_25.value(0)
        time.sleep(0.5)