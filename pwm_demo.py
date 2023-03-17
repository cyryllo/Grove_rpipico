from machine import Pin, PWM
from utime import sleep

dioda = PWM(Pin(5))

dioda.freq(1000)

while True:
    for duty in range(65025):
        dioda.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        dioda.duty_u16(duty)
        sleep(0.0001)
