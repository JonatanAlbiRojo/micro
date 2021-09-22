from machine import Pin, PWM
import utime

def main():
    
    servo = PWM(Pin(27), freq = 50)        
    
    
    while True:
        angulo = float(input('Ingrese un ángulo: '))
        if angulo >= 0 and angulo <= 180:
            ciclo = (0.0111*angulo + 0.5)
            ciclo = int(ciclo*1023/20)
            servo.duty(ciclo)
            print(ciclo)
        else:
            print('Digite un ángulo entre 0 y 180')
    
if __name__ == '__main__':
    main()