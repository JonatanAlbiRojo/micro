from machine import Pin, PWM
from time import sleep

# servo = PWM(Pin(27), freq = 50)


def map(x):
    return int((x - 0) * (1023 - 0) / (180 - 0) + 0)

m = map(180)

    
print(m)

    